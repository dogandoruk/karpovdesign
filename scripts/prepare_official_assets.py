import os
import shutil
import json
import fitz
from PIL import Image

def extract_logos():
    os.makedirs('assets/official', exist_ok=True)
    ai_path = 'Official Assets/KAD web ref links/logo.ai'
    doc = fitz.open(ai_path)
    page = doc[0]
    svg_raw = page.get_svg_image()

    # Charcoal SVG
    with open('assets/official/logo_charcoal.svg', 'w', encoding='utf-8') as f:
        f.write(svg_raw)
    print("Saved assets/official/logo_charcoal.svg")

    # White SVG (substitute #231f20 fill with #ffffff)
    svg_white = svg_raw.replace('fill="#231f20"', 'fill="#ffffff"')
    with open('assets/official/logo_white.svg', 'w', encoding='utf-8') as f:
        f.write(svg_white)
    print("Saved assets/official/logo_white.svg")

    # High-DPI transparent PNGs
    mat = fitz.Matrix(4, 4)
    pix = page.get_pixmap(matrix=mat, alpha=True)
    pix.save('assets/official/logo_charcoal.png')
    print("Saved assets/official/logo_charcoal.png")

    im = Image.open('assets/official/logo_charcoal.png').convert('RGBA')
    r, g, b, a = im.split()
    white_img = Image.merge('RGBA', (Image.new('L', im.size, 255), Image.new('L', im.size, 255), Image.new('L', im.size, 255), a))
    white_img.save('assets/official/logo_white.png')
    print("Saved assets/official/logo_white.png")

def optimize_image(src_path, dest_path, max_dim=2000):
    try:
        with Image.open(src_path) as im:
            # Convert CMYK or others to RGB
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

# Mapping 21 official directories to project metadata
PROJECTS_CONFIG = [
    {
        "id": "pijp-park",
        "dir": "01 PIJP PARK",
        "title": "De Pijp Community Center & Park",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "Amsterdam, Netherlands",
        "year": "2016",
        "award": True,
        "awardText": "ArchMedium International Architecture Competition Finalist",
        "description": "Urban park integration and community cultural pavilion within Amsterdam's historic De Pijp quarter, reconnecting neighborhood density with porous green civic corridors.",
        "primary_file": "pijp park 4.jpg"
    },
    {
        "id": "seed-retreat",
        "dir": "02 SEED ARTISTS GETAWAY",
        "title": "SEED Artists Getaway",
        "category": "Residential",
        "typology": "Residential",
        "status": "Concepts",
        "location": "Black Mountain, NC, USA",
        "year": "2018",
        "award": True,
        "awardText": "UNCC School of Architecture Honor Studio Selection",
        "description": "A secluded residential sanctuary and studio retreat embedded in the Blue Ridge Mountains, harmonizing local timber framing with passive thermal envelopes.",
        "primary_file": "seed 2.jpg"
    },
    {
        "id": "izka-tower",
        "dir": "03 IZKA",
        "title": "İZKA Corporate Headquarters",
        "category": "Commercial",
        "typology": "Commercial",
        "status": "Completion",
        "location": "Izmir, Turkey",
        "year": "2015",
        "award": True,
        "awardText": "Built Commercial Commission with Aboutblank Architecture",
        "description": "High-performance commercial office tower designed with Aboutblank Architecture, featuring responsive kinetic sun-shading louvers and optimized floorplates.",
        "primary_file": "izka 10.jpg"
    },
    {
        "id": "beer-code",
        "dir": "04 BEER CODE",
        "title": "Beer Code Gastropub & Brewery",
        "category": "Commercial",
        "typology": "Commercial",
        "status": "Completion",
        "location": "Eskişehir, Turkey",
        "year": "2017",
        "award": False,
        "awardText": "",
        "description": "Bespoke industrial gastropub interior featuring custom metalwork, raw structural masonry, and integrated microbrewery tasting experience.",
        "primary_file": "beer 1.jpg"
    },
    {
        "id": "travel-sketches",
        "dir": "05 TRAVEL SKETCHES",
        "title": "Rome & Mediterranean Watercolors",
        "category": "Art",
        "typology": "Art",
        "status": "Completion",
        "location": "Rome, Italy & Aegean Coast",
        "year": "2016",
        "award": True,
        "awardText": "Featured Fine Art Portfolio & Studio Selection",
        "description": "Plein-air architectural watercolors and analog field studies capturing Roman antiquity, classical light, and monumental urban spatial sequences.",
        "primary_file": "ak 1.jpg"
    },
    {
        "id": "growing-cell",
        "dir": "06 GROWING CELL",
        "title": "Growing Cell Modular Habitat",
        "category": "Conceptual",
        "typology": "Conceptual",
        "status": "Concepts",
        "location": "Theoretical Research",
        "year": "2017",
        "award": False,
        "awardText": "",
        "description": "Biological cellular aggregation model exploring adaptable, self-assembling spatial growth systems for high-density resilient future cities.",
        "primary_file": "growingcell 1.jpg"
    },
    {
        "id": "valley-of-life",
        "dir": "07 VALLEY OF LIFE",
        "title": "Beylikdüzü Valley of Life",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "Istanbul, Turkey",
        "year": "2016",
        "award": True,
        "awardText": "Beylikdüzü Valley of Life National Competition Award",
        "description": "Ecological corridor master plan converting a desiccated dry river valley into a resilient green civic park and recreational waterfront infrastructure.",
        "primary_file": "VALEY OF LIFE 1.jpg"
    },
    {
        "id": "life-bridge",
        "dir": "08 LIFE BRIDGE",
        "title": "Sivas Unity Bridge & Cultural Crossing",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "Sivas, Turkey",
        "year": "2015",
        "award": True,
        "awardText": "Sivas Kizilirmak Bridge International Competition",
        "description": "Inhabited pedestrian infrastructure spanning the Kızılırmak River, weaving public amphitheaters, cycling lanes, and open gathering plazas into a unified civic deck.",
        "primary_file": "LIFE BRIDGE 10.jpg"
    },
    {
        "id": "multi-city",
        "dir": "09 MULTI CITY",
        "title": "Eskişehir Industrial Regeneration (Multi-City)",
        "category": "Commercial",
        "typology": "Commercial",
        "status": "Concepts",
        "location": "Eskişehir, Turkey",
        "year": "2015",
        "award": True,
        "awardText": "1st Place Winner - Two-Phase Invited Competition (51,000 m²)",
        "description": "1st Prize winning adaptive reuse master plan transforming an abandoned municipal vehicle depot into a 51,000 m² thriving mixed-use tech incubator, retail promenade, and cultural center.",
        "primary_file": "MULTI CITY 10.jpg"
    },
    {
        "id": "hand-study",
        "dir": "10 HAND STUDY",
        "title": "Analog Charcoal & Structural Drafting Studies",
        "category": "Art",
        "typology": "Art",
        "status": "Completion",
        "location": "Charlotte, NC & Europe",
        "year": "2018",
        "award": False,
        "awardText": "",
        "description": "Exploratory hand drafting, charcoal volumetric studies, and anatomical tectonic investigations demonstrating pure tactile mastery of architectural proportion.",
        "primary_file": "HAND STUDY02.jpg"
    },
    {
        "id": "folding-edge",
        "dir": "11 FOLDING EDGE",
        "title": "Folding Edge Sky Garden Pavilion",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "UNCC Architectural Labs, USA",
        "year": "2019",
        "award": False,
        "awardText": "",
        "description": "Origami-inspired origami geometric envelope engineered with self-supporting folded steel plates, creating dramatic cantilevered sky observation terraces.",
        "primary_file": "FOLDING EDGE 11.jpg"
    },
    {
        "id": "community-plaza",
        "dir": "12 COMMUNITY PLAZA",
        "title": "Caferağa Community Center & Public Plaza",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "Kadıköy, Istanbul, Turkey",
        "year": "2016",
        "award": True,
        "awardText": "2nd Place Winner - National Architectural Competition",
        "description": "2nd Prize winning civic center providing tiered community halls, public library facilities, and permeable street-level urban plazas in historic Kadıköy.",
        "primary_file": "COMMUNITY PLAZA 2.jpg"
    },
    {
        "id": "summer-island",
        "dir": "13 SUMMER ISLAND",
        "title": "Summer Island Coastal Resort & Villas",
        "category": "Residential",
        "typology": "Residential",
        "status": "Concepts",
        "location": "Aegean Archipelago",
        "year": "2018",
        "award": False,
        "awardText": "",
        "description": "Low-slung subterranean coastal villas carved into limestone topography, celebrating panoramic sea vistas with minimal ecological footprint.",
        "primary_file": "SUMMER ISLAND 10.jpg"
    },
    {
        "id": "flowing-garden",
        "dir": "14 FLOWING GARDEN",
        "title": "Flowing Garden Estate & Terraces",
        "category": "Residential",
        "typology": "Residential",
        "status": "Concepts",
        "location": "North Carolina Foothills, USA",
        "year": "2019",
        "award": False,
        "awardText": "",
        "description": "Stepped residential volumes intertwined with continuous rainwater bioretention bioswales and native botanical gardens.",
        "primary_file": "FLOWING GARDEN 13.jpg"
    },
    {
        "id": "tent-hill",
        "dir": "15 TENT HILL",
        "title": "Tent Hill Tensile Pavilion",
        "category": "Conceptual",
        "typology": "Conceptual",
        "status": "Concepts",
        "location": "Appalachian Ridgeline, USA",
        "year": "2018",
        "award": False,
        "awardText": "",
        "description": "Lightweight high-tensile membrane structure responding to wind loads and solar angles, forming a luminous canopy over natural knolls.",
        "primary_file": "TENT HILL 14.jpg"
    },
    {
        "id": "chrono-orb",
        "dir": "16 CHRONO ORB",
        "title": "Chrono Orb Parametric Installation",
        "category": "Art",
        "typology": "Art",
        "status": "Completion",
        "location": "Exhibition Space, USA",
        "year": "2019",
        "award": False,
        "awardText": "",
        "description": "Kinetic light and shadow pavilion calibrated to solar ephemeris, projecting dynamic shadow geometries throughout seasonal solstices.",
        "primary_file": "CHRONO ORB 1.jpg"
    },
    {
        "id": "eternity-ring",
        "dir": "17 ETERNITY RING",
        "title": "Eternity Ring Monumental Forum",
        "category": "Art",
        "typology": "Art",
        "status": "Concepts",
        "location": "Civic Memorial Park",
        "year": "2017",
        "award": False,
        "awardText": "",
        "description": "Continuous circular weathered-steel monolith defining an acoustic sanctuary and reflective water forum for quiet commemoration.",
        "primary_file": "ETERNIGY RING 2.jpg"
    },
    {
        "id": "modular-house",
        "dir": "18 MODULAR HOUSE",
        "title": "Modular Prefab Mass-Timber Housing",
        "category": "Residential",
        "typology": "Residential",
        "status": "Concepts",
        "location": "Charlotte, NC, USA",
        "year": "2020",
        "award": False,
        "awardText": "",
        "description": "Scalable mass-timber housing system designed for rapid off-site fabrication, circular demountability, and net-zero operational energy.",
        "primary_file": "MODULAR HOUSE 11.jpg"
    },
    {
        "id": "natures-gateway",
        "dir": "19 NATURES GATEWAY",
        "title": "Nature's Gateway Forest Observatory",
        "category": "Cultural",
        "typology": "Cultural",
        "status": "Concepts",
        "location": "Great Smoky Mountains, USA",
        "year": "2018",
        "award": False,
        "awardText": "",
        "description": "Vertical timber lookout tower providing elevated canopy walkways and educational exhibits focused on regional forest preservation.",
        "primary_file": "NATURES GATEWAY 12.jpg"
    },
    {
        "id": "flex-tower",
        "dir": "20 FLEX TOWER",
        "title": "Flex Tower Sustainable Skyscraper",
        "category": "Commercial",
        "typology": "Commercial",
        "status": "Concepts",
        "location": "High-Density Metropolis",
        "year": "2019",
        "award": False,
        "awardText": "",
        "description": "Aerodynamically sculpted high-rise tower integrating sky courts, natural stack ventilation, and flexible modular floorplates for hybrid working.",
        "primary_file": "FLEX TOWER 02.jpg"
    },
    {
        "id": "outside-in",
        "dir": "21 OUTSIDE-IN",
        "title": "Outside-In Courtyard Residence",
        "category": "Residential",
        "typology": "Residential",
        "status": "Completion",
        "location": "Suburban Estate",
        "year": "2017",
        "award": True,
        "awardText": "Private Residential Commission",
        "description": "Introspective courtyard residence inverting traditional suburban typologies by wrapping living zones around a tranquil Japanese zen courtyard.",
        "primary_file": "OUTSIDE IN 10.jpg"
    }
]

def process_all_projects():
    base_src = 'Official Assets/KAD web ref links'
    base_dest = 'assets/official/projects'
    os.makedirs(base_dest, exist_ok=True)
    
    output_projects = []
    
    for p in PROJECTS_CONFIG:
        dir_name = p['dir']
        slug = p['id']
        src_dir = os.path.join(base_src, dir_name)
        dest_dir = os.path.join(base_dest, slug)
        os.makedirs(dest_dir, exist_ok=True)
        
        if not os.path.exists(src_dir):
            print(f"Warning: directory not found: {src_dir}")
            continue
            
        all_files = os.listdir(src_dir)
        img_files = [f for f in all_files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        processed_images = []
        for img in img_files:
            src_file = os.path.join(src_dir, img)
            # Clean dest filename
            clean_name = img.lower().replace(' ', '_')
            dest_file = os.path.join(dest_dir, clean_name)
            rel_url = f"assets/official/projects/{slug}/{clean_name}"
            
            if optimize_image(src_file, dest_file, max_dim=2000):
                processed_images.append({
                    "original": img,
                    "filename": clean_name,
                    "url": rel_url
                })
        
        # Determine primary image URL
        primary_clean = p['primary_file'].lower().replace(' ', '_')
        primary_url = f"assets/official/projects/{slug}/{primary_clean}"
        if not os.path.exists(os.path.join(dest_dir, primary_clean)) and processed_images:
            primary_url = processed_images[0]['url']
            
        proj_data = dict(p)
        proj_data['primary_image'] = primary_url
        proj_data['images'] = [pi['url'] for pi in processed_images]
        output_projects.append(proj_data)
        print(f"Processed {slug}: {len(processed_images)} images. Primary: {primary_url}")
        
    # Write JSON database
    with open('assets/official/projects.json', 'w', encoding='utf-8') as f:
        json.dump(output_projects, f, indent=2)
    print(f"Saved database of {len(output_projects)} projects to assets/official/projects.json")

def copy_alex_portrait():
    # Canonical photo from brain
    brain_portrait = "C:/Users/doruk/.gemini/antigravity/brain/39f46965-f880-4dd3-820e-4b5b8413e9eb/.user_uploaded/media_1793505232220_74d68b0f.png"
    if os.path.exists(brain_portrait):
        optimize_image(brain_portrait, "assets/official/alex_portrait.png", max_dim=1600)
        print("Copied and optimized Alex's portrait to assets/official/alex_portrait.png")

if __name__ == '__main__':
    extract_logos()
    copy_alex_portrait()
    process_all_projects()
    print("ALL OFFICIAL ASSETS PREPARED SUCCESSFULLY!")
