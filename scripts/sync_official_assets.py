import os
import shutil
import json
import re
from PIL import Image, ImageStat

# Disable decompression bomb warning check for high-res architectural renders
Image.MAX_IMAGE_PIXELS = None

def sanitize_filename(name):
    # keep letters, numbers, dot, dash, underscore
    clean = re.sub(r'[^a-zA-Z0-9._-]', '_', name)
    clean = re.sub(r'_+', '_', clean).lower()
    return clean

def optimize_image(src_path, dest_path, max_dim=2000):
    try:
        with Image.open(src_path) as im:
            if im.mode in ('CMYK', 'P'):
                im = im.convert('RGB')
            w, h = im.size
            if max(w, h) > max_dim:
                scale = max_dim / float(max(w, h))
                new_w = int(w * scale)
                new_h = int(h * scale)
                im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            if dest_path.lower().endswith(('.jpg', '.jpeg')):
                if im.mode == 'RGBA':
                    im = im.convert('RGB')
                im.save(dest_path, 'JPEG', quality=88, optimize=True, progressive=True)
            else:
                im.save(dest_path, optimize=True)
            return True
    except Exception as e:
        print(f"Error optimizing {src_path}: {e}")
        return False

def calculate_luminosity(path):
    try:
        with Image.open(path) as im:
            stat = ImageStat.Stat(im.convert('L'))
            return stat.mean[0]
    except Exception:
        return 999.0

def process_all_projects():
    with open('assets/official/projects.json', 'r', encoding='utf-8') as f:
        projects = json.load(f)

    for p in projects:
        proj_dir_name = p['dir']
        p_id = p['id']
        src_dir = os.path.join('Official Assets', proj_dir_name)
        dest_dir = os.path.join('assets/official/projects', p_id)
        os.makedirs(dest_dir, exist_ok=True)

        if not os.path.exists(src_dir):
            print(f"Directory not found: {src_dir}")
            continue

        raw_files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]
        
        processed_images = []
        file_lum_map = []

        for f in raw_files:
            src_file = os.path.join(src_dir, f)
            dest_filename = sanitize_filename(f)
            dest_file = os.path.join(dest_dir, dest_filename)

            # Optimize and copy to assets/official/projects/<p_id>/
            if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
                optimize_image(src_file, dest_file)
            
            web_path = f"assets/official/projects/{p_id}/{dest_filename}".replace('\\', '/')
            processed_images.append(web_path)

            lum = calculate_luminosity(src_file)
            file_lum_map.append((lum, web_path, f))

        # Sort by luminosity ascending (lowest = darkest, best contrast against #f8f9fa)
        file_lum_map.sort(key=lambda x: x[0])

        if file_lum_map:
            darkest_lum, darkest_web_path, darkest_raw_name = file_lum_map[0]
            p['primary_image'] = darkest_web_path
            p['primary_file'] = darkest_raw_name
            p['primary_luminosity'] = round(darkest_lum, 2)
            print(f"[{p_id}] Selected cover: {darkest_web_path} (Luminosity: {darkest_lum:.1f})")

        p['images'] = sorted(list(set(processed_images)))

    with open('assets/official/projects.json', 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=2, ensure_ascii=False)
    print("Updated assets/official/projects.json successfully!")

if __name__ == '__main__':
    process_all_projects()
