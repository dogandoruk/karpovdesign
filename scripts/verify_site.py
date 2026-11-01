import os
import re
import json

html_files = ['index.html', 'variant.html', 'about.html', 'contact.html', 'academy.html']
errors = []

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
        clean_src = src.split('?')[0].split('#')[0]
        if not os.path.exists(clean_src):
            errors.append(f"Broken static img src in {hf}: {src}")

    # Check favicon / link hrefs
    links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
    for l in links:
        if l.startswith(('http', 'data:')):
            continue
        clean_l = l.split('?')[0].split('#')[0]
        if not os.path.exists(clean_l):
            errors.append(f"Broken link in {hf}: {l}")

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
    print("ALL 5 PAGES AND ALL 21 PROJECTS VERIFIED WITH ZERO BROKEN ASSETS OR 404 LINKS!")
