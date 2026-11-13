import os
import re
import json

import os
import re
import json
import glob

html_files = (
    ['index.html', 'variant.html', 'about.html', 'contact.html', 'academy.html']
    + sorted(glob.glob('projects/*/index.html'))
    + sorted(glob.glob('projects/*/variant/index.html'))
)
errors = []


def resolve_local_target(hf, ref):
    clean_ref = ref.split('?')[0].split('#')[0]
    if not clean_ref:
        return hf
    base_dir = os.path.dirname(hf)
    joined = os.path.normpath(os.path.join(base_dir, clean_ref))
    if clean_ref.endswith('/') or os.path.isdir(joined):
        joined = os.path.join(joined, 'index.html')
    return joined


for hf in html_files:
    if not os.path.exists(hf):
        errors.append(f"Missing file: {hf}")
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip <script> tags for raw HTML image checks
    html_no_scripts = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)

    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_no_scripts)
    for src in srcs:
        if src.startswith(('http', 'data:')):
            continue
        target = resolve_local_target(hf, src)
        if not os.path.exists(target):
            errors.append(f"Broken static img src in {hf}: {src} -> {target}")

    # Check favicon / link hrefs
    links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
    for l in links:
        if l.startswith(('http', 'data:')):
            continue
        target = resolve_local_target(hf, l)
        if not os.path.exists(target):
            errors.append(f"Broken link in {hf}: {l} -> {target}")

    # Check internal <a> hrefs
    a_hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html_no_scripts)
    for href in a_hrefs:
        if href.startswith(('http', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        clean_href = href.split('?')[0].split('#')[0]
        if not clean_href:
            continue
        target = resolve_local_target(hf, href)
        if not os.path.exists(target):
            errors.append(f"Broken a href in {hf}: {href} -> {target}")

# Check all images in projects.json
with open('assets/official/projects.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

for p in projects:
    if not os.path.exists(p['primary_image']):
        errors.append(f"Missing primary image for {p['id']}: {p['primary_image']}")
    for img in p.get('images', []):
        if not os.path.exists(img):
            errors.append(f"Missing gallery image for {p['id']}: {img}")

print(f"Total HTML files checked: {len(html_files)}")
print(f"Total projects in JSON: {len(projects)}")
if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for e in errors:
        print(" -", e)
else:
    print(f"ALL {len(html_files)} PAGES AND ALL {len(projects)} PROJECTS VERIFIED WITH ZERO BROKEN ASSETS OR 404 LINKS!")
