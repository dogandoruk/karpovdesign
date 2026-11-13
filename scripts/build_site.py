# Master site build script for Karpov Design LLC
# Incorporating Field Architecture Model (25% left negative space, 70% content rail, clamp(32px, 5vw, 64px) right edge)
# Global dropdown filters, 20% reduced card gap, contrast-favoring cover images, Hero Variants A & B
# Locked Option 2 Logo Height (84px desktop / 72px mobile) with 2px vertical margin from header boundaries, 1.5s Hero logo fade timing, curated alternating hero slideshow sequence

import os
import json
import re
from PIL import Image

def load_projects():
    with open('assets/official/projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

projects_data = load_projects()
projects_json_str = json.dumps(projects_data).replace('</script>', '<\\/script>')

def get_best_hero_image(p):
    best = p.get('primary_image')
    max_px = 0
    for img in p.get('images', []):
        if os.path.exists(img):
            try:
                with Image.open(img) as im:
                    px = im.width * im.height
                    if px > max_px:
                        max_px = px
                        best = img
            except Exception:
                pass
    return best

for p in projects_data:
    p['best_hero_image'] = get_best_hero_image(p)

CROP_CLASS_MAP = {
    'cover-center': 'object-cover object-center',
    'cover-top': 'object-cover object-top',
    'cover-bottom': 'object-cover object-bottom',
    'contain': 'object-contain object-center',
}

def crop_mode_to_class(mode):
    return CROP_CLASS_MAP.get(mode, 'object-cover object-center')

def get_project_image_roles(p):
    images = p.get('images') or []
    primary = p.get('primary_image') or (images[0] if images else '')
    existing = p.get('image_roles') if isinstance(p.get('image_roles'), dict) else {}

    def pick_fallback(idx):
        if not images:
            return primary
        return images[idx % len(images)]

    if p.get('id') == 'summer-island':
        defaults = {
            'card_thumb': primary,
            'hero_image': pick_fallback(0),
            'sketch_image': pick_fallback(10),
            'landscape_1': pick_fallback(7),
            'pair_1a': pick_fallback(6),
            'pair_1b': pick_fallback(8),
            'landscape_2': pick_fallback(4),
            'pair_2a': pick_fallback(11),
            'pair_2b': pick_fallback(5),
            'banner_image': pick_fallback(9),
        }
    else:
        ordered = []
        if primary:
            ordered.append(primary)
        for img in images:
            if img not in ordered:
                ordered.append(img)
        if not ordered:
            ordered = ['']
        def pick_seq(idx):
            return ordered[idx % len(ordered)]
        defaults = {
            'card_thumb': primary or pick_seq(0),
            'hero_image': primary or pick_seq(0),
            'sketch_image': pick_seq(1),
            'landscape_1': pick_seq(2),
            'pair_1a': pick_seq(3),
            'pair_1b': pick_seq(4),
            'landscape_2': pick_seq(5),
            'pair_2a': pick_seq(6),
            'pair_2b': pick_seq(7),
            'banner_image': pick_seq(8),
        }

    roles = {}
    for key, fallback_val in defaults.items():
        val = existing.get(key)
        if val and (val in images or os.path.exists(val)):
            roles[key] = val
        else:
            roles[key] = fallback_val
    return roles

def get_project_image_crops(p):
    existing = p.get('image_crops') if isinstance(p.get('image_crops'), dict) else {}
    defaults = {
        'card_thumb': 'cover-center',
        'hero_image': 'cover-center',
        'sketch_image': 'contain',
        'landscape_1': 'cover-center',
        'pair_1a': 'cover-center',
        'pair_1b': 'cover-center',
        'landscape_2': 'contain',
        'pair_2a': 'cover-center',
        'pair_2b': 'cover-center',
        'banner_image': 'cover-center',
    }
    crops = {}
    for key, fallback_val in defaults.items():
        val = existing.get(key)
        crops[key] = val if val in CROP_CLASS_MAP else fallback_val
    return crops

roles_updated = False
for p in projects_data:
    computed_roles = get_project_image_roles(p)
    computed_crops = get_project_image_crops(p)
    if p.get('image_roles') != computed_roles or p.get('image_crops') != computed_crops:
        p['image_roles'] = computed_roles
        p['image_crops'] = computed_crops
        p['primary_image'] = computed_roles.get('card_thumb') or p.get('primary_image')
        roles_updated = True

if roles_updated:
    projects_to_save = []
    for p in projects_data:
        copy_p = {k: v for k, v in p.items() if k != 'best_hero_image'}
        projects_to_save.append(copy_p)
    with open('assets/official/projects.json', 'w', encoding='utf-8') as f:
        json.dump(projects_to_save, f, indent=2, ensure_ascii=False)

projects_json_str = json.dumps(projects_data).replace('</script>', '<\\/script>')

# Curated Alternating Hero Slideshow Sequence (Dark & Moody Rhythm based on luminosity)
# Alternating deep darks (lum 24-80) with architectural midtones (lum 99-127)
CURATED_PROJECT_ORDER = [
    "beer-code",          # Lum 24.7 (Deep dark interior brewery)
    "multi-city",         # Lum 99.8 (Industrial architectural midtone)
    "tent-hill",          # Lum 26.8 (Dark dramatic night silhouette)
    "seed-retreat",       # Lum 113.8 (Blue Ridge dusk retreat)
    "travel-sketches",    # Lum 32.7 (Rich Mediterranean watercolor study)
    "summer-island",      # Lum 127.3 (Aegean coastal twilight resort)
    "hand-study",         # Lum 35.2 (Graphite tectonic study)
    "life-bridge",        # Lum 105.4 (Sivas river twilight civic bridge)
    "chrono-orb",         # Lum 79.5 (Moody kinetic spherical pavilion)
    "izka-tower",         # Lum 134.9 (Izmir glass headquarters dusk)
    "eternity-ring",      # Lum 96.5 (Sculptural circular installation)
    "growing-cell",       # Lum 111.0 (Parametric cellular pavilion)
    "valley-of-life",     # Lum 135.4 (Beylikdüzü urban ecological corridor)
    "pijp-park",          # Lum 121.8 (Amsterdam cultural community center)
    "outside-in",         # Lum 118.3 (Residential courtyard residence)
    "flowing-garden",     # Lum 116.8 (Terraced residential landscape)
    "natures-gateway",    # Lum 119.9 (Parametric wooden gateway)
    "community-plaza",    # Lum 121.3 (Caferağa public civic square)
    "flex-tower",         # Lum 146.2 (Adaptive commercial highrise)
    "modular-house",      # Lum 150.7 (Prefabricated timber module)
    "folding-edge"        # Lum 152.4 (Geometric sky pavilion)
]

projects_map = {p['id']: p for p in projects_data}
HERO_SLIDES = []
for p_id in CURATED_PROJECT_ORDER:
    if p_id in projects_map:
        p = projects_map[p_id]
        HERO_SLIDES.append({
            "id": p["id"],
            "title": p["title"],
            "image": p.get("primary_image")
        })
for p in projects_data:
    if p['id'] not in CURATED_PROJECT_ORDER:
        HERO_SLIDES.append({
            "id": p["id"],
            "title": p["title"],
            "image": p.get("primary_image")
        })

hero_slides_json_str = json.dumps(HERO_SLIDES).replace('</script>', '<\\/script>')

def generate_json_ld_schema():
    items = []
    for idx, p in enumerate(projects_data):
        items.append({
            "@type": "ListItem",
            "position": idx + 1,
            "item": {
                "@type": "VisualArtwork",
                "name": p.get("title"),
                "image": f"https://dogandoruk.github.io/karpovdesign/{p.get('primary_image')}",
                "creator": {
                    "@type": "Person",
                    "name": "Aleksandre Karpov"
                },
                "artform": p.get("typology"),
                "dateCreated": str(p.get("year")),
                "contentLocation": p.get("location"),
                "url": f"https://dogandoruk.github.io/karpovdesign/projects/{p.get('id')}/",
                "description": p.get("description")
            }
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Aleksandre Karpov Design LLC Portfolio",
        "description": "Selected residential design projects, computational models, and spatial studies by Karpov Design LLC.",
        "itemListElement": items
    }
    return json.dumps(schema, indent=2)

JSON_LD_SCHEMA_TAG = f'<script type="application/ld+json">\n{generate_json_ld_schema()}\n</script>'


SHARED_HEAD_TAGS = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/svg+xml" href="assets/official/logo_charcoal.svg">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    if (!window.tailwind) {
      document.write('<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"><\\/script>');
    }
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
  {JSON_LD_SCHEMA_TAG}
  <style>
    .font-raleway {
      font-family: 'Raleway', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    :root {
      --bg-main: #f8f9fa;
      --bg-surface: #ffffff;
      --text-main: #1a1d20;
      --text-muted: #595f65;
      --border-line: #e2e5e8;
      
      /* Eyeblue palette */
      --eyeblue-deep: #2b4951;
      --eyeblue-mid: #38606a;
      --eyeblue-soft: #67aec0;
      --eyeblue-pale: #e4f0f2;

      /* Hairberry orange palette */
      --hairberry-rich: #ad4b24;
      --hairberry-vibrant: #de602e;
      --hairberry-bright: #f36a34;
      --hairberry-peach: #f19f55;

      /* Field Architecture Spacing Model:
         Desktop: 25% Left Negative Offset, 70% Asymmetric Content Rail, Right edge clamped between 32px and 64px
         Tablet/Mobile (< 1024px): 5% - 90% - 5% (min 20px padding)
      */
      --field-left-offset: 25vw;
      --field-right-gutter: clamp(32px, 5vw, 64px);
    }
    @media (max-width: 1023px) {
      :root {
        --field-left-offset: clamp(20px, 5vw, 40px);
        --field-right-gutter: clamp(20px, 5vw, 40px);
      }
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      overflow-x: hidden;
    }

    /* Asymmetric Field Layout Containers */
    .field-header-container {
      padding-left: var(--field-left-offset);
      padding-right: var(--field-right-gutter);
      width: 100%;
    }
    .field-content-rail {
      padding-left: var(--field-left-offset);
      padding-right: var(--field-right-gutter);
      width: 100%;
    }

    /* Ambient Ken-Burns Animation for Hero Slides */
    @keyframes kenBurnsSubtle {
      0% {
        transform: scale(1.0) translate(0, 0);
      }
      50% {
        transform: scale(1.05) translate(-1%, -0.5%);
      }
      100% {
        transform: scale(1.0) translate(0, 0);
      }
    }
    .ambient-motion {
      animation: kenBurnsSubtle 16s ease-in-out infinite alternate;
      will-change: transform;
    }
    .paused-motion {
      animation-play-state: paused !important;
    }

    /* Custom Sleek Dropdown Styling (Default Page) */
    .custom-dropdown-container {
      position: relative;
    }
    .custom-dropdown-btn {
      display: inline-flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      padding: 0.5rem 0.85rem;
      background: #ffffff;
      border: 1px solid #e2e5e8;
      font-family: monospace;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: #1a1d20;
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .custom-dropdown-btn:hover {
      border-color: #38606a;
    }
    .custom-dropdown-btn.active-filter {
      border-color: #de602e;
      color: #de602e;
      font-weight: 600;
    }
    .custom-dropdown-menu {
      position: absolute;
      top: calc(100% + 4px);
      left: 0;
      min-width: 100%;
      background: #ffffff;
      border: 1px solid #e2e5e8;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
      z-index: 40;
      display: none;
      flex-direction: column;
      padding: 0.25rem 0;
    }
    .custom-dropdown-menu.open {
      display: flex;
    }
    .custom-dropdown-item {
      padding: 0.5rem 0.85rem;
      font-family: monospace;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: #595f65;
      text-align: left;
      transition: all 0.15s ease;
      cursor: pointer;
      white-space: nowrap;
    }
    .custom-dropdown-item:hover {
      background: #f8f9fa;
      color: #1a1d20;
    }
    .custom-dropdown-item.selected {
      color: #de602e;
      font-weight: 600;
      background: #fff5f2;
    }

    /* Native Dropdown Styling (Variant Page) */
    .native-architectural-select {
      appearance: none;
      -webkit-appearance: none;
      -moz-appearance: none;
      background-color: #ffffff;
      border: 1px solid #e2e5e8;
      padding: 0.5rem 2rem 0.5rem 0.85rem;
      font-family: monospace;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      color: #1a1d20;
      cursor: pointer;
      outline: none;
      transition: all 0.2s ease;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%23595f65'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 0.65rem center;
      background-size: 0.85rem;
    }
    .native-architectural-select:hover {
      border-color: #38606a;
    }
    .native-architectural-select:focus {
      border-color: #de602e;
    }
    .native-architectural-select.active-filter {
      border-color: #de602e;
      color: #de602e;
      font-weight: 600;
    }

    /* Header Logo Height & Tight 2px Margin to Borders */
    #header-logo-img {
      height: 72px;
      width: auto;
      display: block;
    }
    @media (min-width: 768px) {
      #header-logo-img {
        height: 84px;
      }
    }

    
    @media (hover: none), (max-width: 1023px) {
      .touch-variant-title {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
    }

    ::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
"""

def generate_header(active_nav="works", borderless=True, is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    works_url = f"{base_path}index.html#works"
    about_url = f"{base_path}about.html"
    contact_url = f"{base_path}contact.html"
    home_url = f"{base_path}index.html"
    logo_src = f"{base_path}assets/official/logo_charcoal.svg"
    
    brand_font = "font-raleway" if font_mode == "raleway" else ""
    works_cls = f"text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5 {brand_font}" if active_nav == "works" else f"text-[#595f65] hover:text-[#1a1d20] transition-colors {brand_font}"
    about_cls = f"text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5 {brand_font}" if active_nav == "about" else f"text-[#595f65] hover:text-[#1a1d20] transition-colors {brand_font}"
    contact_cls = f"text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5 {brand_font}" if active_nav == "contact" else f"text-[#595f65] hover:text-[#1a1d20] transition-colors {brand_font}"

    border_cls = "" if borderless else "border-b border-[#e2e5e8]"

    return f"""
  <!-- Top Navigation: Header Height Tailored to Logo Option 2 (84px desktop / 72px mobile) with 2px Vertical Clearance -->
  <header id="main-site-header" class="w-full bg-[#f8f9fa]/95 backdrop-blur-md {border_cls} z-50 sticky top-0 transition-all border-b border-[#e2e5e8]/60">
    <div class="field-header-container flex items-center justify-between py-[2px]">
      
      <!-- Top Left: Logo Monogram (84px/72px, 2px away from borders) + Stacked Typography Flush to Baseline -->
      <a href="{home_url}" class="flex items-center gap-3.5 md:gap-4 group">
        <img id="header-logo-img" src="{logo_src}" alt="KAD Monogram" class="w-auto object-contain">
        <div id="header-logo-text" class="flex flex-col text-[12px] md:text-[13px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20] {brand_font}">
          <span>ALEKSANDRE</span>
          <span>KARPOV</span>
          <span id="header-logo-sub" class="text-[9.5px] md:text-[10px] tracking-[0.22em] text-[#595f65] font-normal">DESIGN LLC</span>
        </div>
      </a>

      <!-- Right Area: Navigation Links -->
      <nav class="hidden md:flex items-center gap-8 text-xs tracking-[0.2em] uppercase {brand_font}">
        <a href="{works_url}" class="{works_cls}">Works</a>
        <a href="{about_url}" class="{about_cls}">About</a>
        <a href="{contact_url}" class="{contact_cls}">Contact</a>
      </nav>

      <!-- Mobile Navigation Trigger (< 768px) -->
      <button id="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Menu" aria-expanded="false" class="md:hidden inline-flex items-center gap-2 px-2 py-2 text-xs font-mono uppercase tracking-[0.22em] text-[#1a1d20] focus:outline-none">
        <span id="mobile-menu-label" class="font-semibold">Menu</span>
        <div class="w-5 h-3.5 flex flex-col justify-between items-end">
          <span id="burger-line-1" class="w-5 h-[1.5px] bg-[#1a1d20] transition-all duration-300 origin-right"></span>
          <span id="burger-line-2" class="w-3.5 h-[1.5px] bg-[#1a1d20] transition-all duration-300"></span>
          <span id="burger-line-3" class="w-5 h-[1.5px] bg-[#1a1d20] transition-all duration-300 origin-right"></span>
        </div>
      </button>

    </div>

    <!-- Mobile Full-Bleed Navigation Sheet (< 768px) -->
    <div id="mobile-nav-menu" class="hidden md:hidden w-full bg-[#f8f9fa] border-b border-[#e2e5e8] px-6 py-8 transition-all">
      <nav class="flex flex-col gap-6 text-sm font-mono uppercase tracking-[0.22em]">
        <a href="{works_url}" onclick="closeMobileMenu()" class="{works_cls} pb-2 border-b border-[#e2e5e8]">01 / Works</a>
        <a href="{about_url}" onclick="closeMobileMenu()" class="{about_cls} pb-2 border-b border-[#e2e5e8]">02 / About</a>
        <a href="{contact_url}" onclick="closeMobileMenu()" class="{contact_cls} pb-2 border-b border-[#e2e5e8]">03 / Contact</a>
      </nav>
      <div class="mt-8 pt-6 border-t border-[#e2e5e8] flex flex-col gap-2 text-[11px] font-mono text-[#595f65]">
        <span>Aleksandre Karpov Design LLC</span>
        <span>Asheville &bull; Charlotte &bull; International</span>
      </div>
    </div>
  </header>
"""

def generate_footer(borderless=True, bg="#f8f9fa", is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    border_cls = "" if borderless else "border-t border-[#e2e5e8]"
    brand_font = "font-raleway" if font_mode == "raleway" else ""
    works_url = f"{base_path}index.html#works"
    about_url = f"{base_path}about.html"
    contact_url = f"{base_path}contact.html"
    academy_url = f"{base_path}academy.html"
    logo_src = f"{base_path}assets/official/logo_charcoal.svg"

    return f"""
  <!-- Footer: Field Architecture Layout Alignment -->
  <footer class="w-full bg-[{bg}] {border_cls} py-12 md:py-16">
    <div class="field-content-rail flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
      
      <!-- Studio Monogram & Identity -->
      <div class="flex items-center gap-3">
        <img src="{logo_src}" alt="KAD Monogram" class="h-8 w-auto opacity-90">
        <div class="flex flex-col text-[10px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20] {brand_font}">
          <span>ALEKSANDRE KARPOV DESIGN</span>
          <span class="text-[9px] tracking-[0.2em] text-[#595f65] font-normal">&copy; 2026 &bull; All Rights Reserved</span>
        </div>
      </div>

      <!-- Footer Quick Navigation -->
      <nav class="flex flex-wrap items-center gap-6 md:gap-8 text-xs font-mono uppercase tracking-widest text-[#595f65]">
        <a href="{works_url}" class="hover:text-[#de602e] transition-colors">Works</a>
        <a href="{about_url}" class="hover:text-[#de602e] transition-colors">About</a>
        <a href="{contact_url}" class="hover:text-[#de602e] transition-colors">Contact</a>
        <a href="{academy_url}" class="hover:text-[#de602e] transition-colors text-[#38606a]">Academy</a>
      </nav>

      <!-- Back to top trigger -->
      <button onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})" class="text-xs font-mono uppercase tracking-widest text-[#595f65] hover:text-[#1a1d20] transition-colors">
        Back to Top &uarr;
      </button>

    </div>
  </footer>
"""

def generate_workflow_section(is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    sketch_src = f"{base_path}assets/official/projects/travel-sketches/ak_4.jpg"

    return f"""
  <!-- Workflow Section -->
  <section class="w-full bg-[#f8f9fa] pt-12 md:pt-16 pb-14 md:pb-20">
    <div class="field-content-rail">
      <!-- Section Header -->
      <div class="mb-6 md:mb-8">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Workflow</h2>
      </div>

      <!-- 50/50 Side-by-Side: Conceptual Sketch & Narrative Paragraphs -->
      <div class="flex flex-col md:flex-row items-center gap-8 lg:gap-12">
        <div onclick="openWorkflowLightbox()" class="group cursor-pointer w-full md:w-1/2 aspect-[4/3] bg-transparent overflow-hidden shrink-0 relative" title="Click to view full size">
          <img src="{sketch_src}" 
               alt="Conceptual Spatial Sketch" 
               class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-500 ease-out">
          <div class="absolute inset-0 bg-black/0 group-hover:bg-black/15 transition-colors duration-300 flex items-end justify-end p-3 pointer-events-none">
            <span class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-[#1a1d20]/80 text-[#67aec0] text-[10px] font-mono uppercase tracking-[0.2em] px-2.5 py-1">Enlarge</span>
          </div>
        </div>

        <div class="w-full md:w-1/2 space-y-4 text-sm md:text-base text-[#595f65] leading-relaxed">
          <p>
            Design begins with spontaneous observational drawing and spatial geometry. Hand-drawn field studies establish essential relationships with natural light, topography, and material presence before computational modeling and technical documentation begin.
          </p>
          <p>
            The act of design is a process deeply rooted in physical reality, yet has no absolute future as our surroundings continuously change. Through rigorous digital coordination, tactile concepts translate into enduring built form.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Workflow Conceptual Sketch Lightbox Modal -->
  <div id="workflow-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/95 backdrop-blur-md hidden flex flex-col items-center justify-center p-4 md:p-8 cursor-pointer select-none" onclick="closeWorkflowLightbox()">
    <button onclick="closeWorkflowLightbox()" class="fixed top-4 left-6 z-60 text-[#67aec0] hover:text-[#de602e] text-3xl font-bold bg-transparent border-none p-2 cursor-pointer transition-colors focus:outline-none" title="Close (Esc)" aria-label="Close popup">&times;</button>
    <div class="max-w-[94vw] max-h-[88vh] flex flex-col items-center justify-center" onclick="event.stopPropagation()">
      <img src="{sketch_src}" alt="Conceptual Spatial Sketch - Full View" class="max-w-full max-h-[82vh] object-contain drop-shadow-2xl">
      <div class="mt-4 text-center">
        <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#e4f0f2]">Observational Field Studies &bull; Hand Drawing &amp; Spatial Geometry</span>
      </div>
    </div>
  </div>
"""

def generate_accolades_section(is_variant=False, layout_mode="default", font_mode="raleway"):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    return f"""
  <!-- Accolades Section -->
  <section class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      <div class="mb-6 md:mb-8">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Competitions & Accolades</h2>
      </div>
      <div class="space-y-8">
        <!-- Item 1 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-6">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">1st Place &bull; Jury Special Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">İZKA Headquarters Competition &bull; Turgut Cansever National Architecture Award</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">1st Prize winning 10,000 m² headquarters for the İzmir Development Agency with Aboutblank.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2014–2016 &bull; İzmir, TR</span>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-6">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">1st Place Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">Multi City Depot Adaptive Reuse Master Plan</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">1st Prize winning 51,000 m² industrial regeneration competition victory with Aboutblank.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2015 &bull; Eskişehir, TR</span>
          </div>
        </div>

        <!-- Item 3 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-6">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">2nd Place Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">Caferağa Community Center National Competition</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">2nd Prize winning 14,000 m² cultural center, theater, and elevated community garden in Kadıköy with Aboutblank.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2016 &bull; Istanbul, TR</span>
          </div>
        </div>

        <!-- Item 4 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-6">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">3rd Place Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">Sivas Unity Bridge &amp; Cultural Crossing</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">3rd Prize winning 150 m span bridge across the Kızılırmak River integrating vehicular, pedestrian, and wetland park paths.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2016 &bull; Sivas, TR</span>
          </div>
        </div>

        <!-- Item 5 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-6">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">Honorable Mention</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">Beylikdüzü Valley of Life Park Master Plan</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">1,750,000 m² central valley park and river corridor infrastructure with Aboutblank &amp; BOOM Landscape.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2015 &bull; Istanbul, TR</span>
          </div>
        </div>

        <!-- Item 6 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">Academic Honors</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">UNCC Boardman Scholarship &amp; Scholastic Silver Key</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Academic merit recognition at the University of North Carolina at Charlotte (UNCC) and Myers Park HS.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2007–2008 &bull; Charlotte, USA</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

def generate_landing_contact_section(is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    contact_url = f"{base_path}contact.html"
    
    return f"""
  <!-- Get in Touch CTA Section -->
  <section class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      <div class="flex flex-col items-start gap-5 py-6">
        <div class="max-w-2xl">
          <h2 class="text-xl sm:text-2xl font-semibold tracking-[0.18em] uppercase text-[#1a1d20] {h2_font}">Start a Conversation</h2>
          <p class="text-xs sm:text-sm text-[#595f65] mt-2 leading-relaxed">Residential design and consulting practice based in Charlotte, North Carolina.</p>
        </div>
        <div class="pt-1">
          <a href="{contact_url}" class="inline-flex items-center gap-2 text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#1a1d20] hover:text-[#de602e] transition-colors group">
            <span>Get in touch</span>
            <span class="group-hover:translate-x-1.5 transition-transform duration-300">&rarr;</span>
          </a>
        </div>
      </div>
    </div>
  </section>
"""

def generate_interactive_modal():
    return """
  <!-- Project Deep Dive Inspection Modal (Borderless Mobile Bottom Sheet / Tablet Modal) -->
  <div id="project-modal" class="fixed inset-0 z-50 bg-[#1a1d20]/80 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-0 sm:p-4 md:p-8">
    <div class="bg-[#f8f9fa] w-full max-w-6xl max-h-[92svh] flex flex-col overflow-hidden shadow-2xl relative">
      
      <!-- Modal Top Bar -->
      <div class="flex items-center justify-between px-5 md:px-6 py-4 bg-[#f8f9fa] shrink-0">
        <div class="flex items-center gap-3">
          <span id="modal-typology" class="text-[10px] font-mono uppercase tracking-widest px-2 py-0.5 bg-[#1a1d20] text-white">Typology</span>
          <span id="modal-status" class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">Status</span>
        </div>
        <button onclick="closeModal()" class="text-[#67aec0] hover:text-[#de602e] transition-colors p-1 text-2xl leading-none" title="Close (Esc)">
          &times;
        </button>
      </div>

      <!-- Modal Body -->
      <div class="flex-1 overflow-y-auto p-5 md:p-8 flex flex-col lg:flex-row gap-6 md:gap-8">
        
        <!-- Left: Image Viewer -->
        <div class="w-full lg:w-3/5 flex flex-col gap-3">
          <div class="w-full aspect-[16/10] bg-[#1a1d20] overflow-hidden">
            <img id="modal-main-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Project Image" class="w-full h-full object-cover">
          </div>
          <!-- Thumbnails Strip -->
          <div id="modal-thumbs" class="flex gap-2 overflow-x-auto pb-2 no-scrollbar"></div>
        </div>

        <!-- Right: Architectural Specification -->
        <div class="w-full lg:w-2/5 flex flex-col justify-between">
          <div>
            <span id="modal-location-year" class="text-xs font-mono text-[#67aec0] tracking-wider uppercase block mb-1">Location &bull; Year</span>
            <h2 id="modal-title" class="text-xl sm:text-2xl md:text-3xl font-semibold tracking-tight text-[#1a1d20] mb-3">Project Title</h2>
            <div id="modal-award-box" class="p-3 bg-[#f8f9fa] border-l-2 border-[#de602e] mb-4 hidden">
              <p id="modal-award-text" class="text-xs font-semibold text-[#1a1d20]"></p>
            </div>
            <p id="modal-description" class="text-xs md:text-sm text-[#595f65] leading-relaxed mb-4"></p>
            <a id="modal-project-link" href="#" class="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-[#de602e] hover:text-[#1a1d20] font-semibold transition-colors mb-6">
              <span>View Full Project Page</span>
              <span>&rarr;</span>
            </a>
          </div>

          <div class="pt-4 mt-auto">
            <div class="flex justify-between items-center">
              <button onclick="navigateModal(-1)" class="py-2 text-xs font-mono tracking-wider uppercase text-[#595f65] hover:text-[#1a1d20] transition-colors flex items-center gap-1">
                &larr; Prev Project
              </button>
              <button onclick="navigateModal(1)" class="py-2 text-xs font-mono tracking-wider uppercase text-[#595f65] hover:text-[#1a1d20] transition-colors flex items-center gap-1">
                Next Project &rarr;
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
"""

JS_TEMPLATE = """
  <script>
    const PROJECTS = __PROJECTS_JSON__;
    const HERO_SLIDES = __HERO_SLIDES_JSON__;
    const IS_VARIANT = __IS_VARIANT__;

    // --- Hero Slideshow Logic ---
    let currentSlide = 0;
    let slideTimer = null;
    let isPaused = false;
    let mobileFiltersOpen = false;

    function toggleMobileFilters() {
      mobileFiltersOpen = !mobileFiltersOpen;
      const filtersContainer = document.getElementById('filters-wrapper');
      const chev = document.getElementById('filter-chevron');
      if (chev) chev.style.transform = mobileFiltersOpen ? 'rotate(180deg)' : '';
      if (filtersContainer) {
        if (mobileFiltersOpen) {
          filtersContainer.classList.remove('hidden');
          filtersContainer.classList.add('flex');
        } else {
          filtersContainer.classList.add('hidden');
          filtersContainer.classList.remove('flex');
        }
      }
    }

    function initHeroSlideshow() {
      const container = document.getElementById('hero-slideshow-container');
      if (!container) return;

      container.innerHTML = '';
      HERO_SLIDES.forEach((s, idx) => {
        const slideDiv = document.createElement('div');
        slideDiv.id = `hero-slide-${idx}`;
        slideDiv.className = `absolute inset-0 transition-opacity duration-1000 ease-in-out ${idx === 0 ? 'opacity-100 z-1' : 'opacity-0 z-0'}`;
        slideDiv.innerHTML = `<img src="${s.image}" alt="${s.title}" class="w-full h-full object-cover ambient-motion">`;
        container.appendChild(slideDiv);
      });

      // Update CTA Link for Initial Slide
      updateCtaLink(0);

      // Click anywhere on hero banner to toggle pause / resume
      const heroBanner = document.getElementById('hero-banner-section');
      if (heroBanner) {
        heroBanner.addEventListener('click', (e) => {
          // Do not toggle pause if clicking the CTA button directly
          if (e.target.closest('#hero-cta-btn')) return;
          toggleHeroPause();
        });
      }

      startSlideTimer();
    }

    function toggleHeroPause() {
      isPaused = !isPaused;
      const statusPill = document.getElementById('hero-pause-indicator');
      const slides = document.querySelectorAll('#hero-slideshow-container img');
      slides.forEach(img => {
        if (isPaused) {
          img.classList.add('paused-motion');
        } else {
          img.classList.remove('paused-motion');
        }
      });
      if (statusPill) {
        statusPill.textContent = isPaused ? 'PAUSED' : '';
        statusPill.style.display = isPaused ? 'block' : 'none';
      }
    }

    function startSlideTimer() {
      if (slideTimer) clearInterval(slideTimer);
      slideTimer = setInterval(() => {
        if (!isPaused) {
          goToSlide((currentSlide + 1) % HERO_SLIDES.length);
        }
      }, 5500);
    }

    function goToSlide(targetIdx) {
      const prevDiv = document.getElementById(`hero-slide-${currentSlide}`);
      const nextDiv = document.getElementById(`hero-slide-${targetIdx}`);
      if (prevDiv) {
        prevDiv.classList.remove('opacity-100', 'z-1');
        prevDiv.classList.add('opacity-0', 'z-0');
      }
      if (nextDiv) {
        nextDiv.classList.remove('opacity-0', 'z-0');
        nextDiv.classList.add('opacity-100', 'z-1');
      }
      currentSlide = targetIdx;
      updateCtaLink(targetIdx);
    }

    function updateCtaLink(idx) {
      const ctaBtn = document.getElementById('hero-cta-btn');
      if (ctaBtn && HERO_SLIDES[idx]) {
        ctaBtn.href = `projects/${HERO_SLIDES[idx].id}/`;
      }
    }

    // --- Works Grid Logic ---
    PROJECTS.forEach((p, idx) => { p._origIndex = idx; });
    
    // Core Decisions: Default filters on load are "Oldest" and "Concept"
    let currentTypology = 'all';
    let currentCompletion = 'concept';
    let currentRecency = 'oldest';
    let currentModalIndex = 0;
    let activeOrderedList = [...PROJECTS];

    function isMatch(p) {
      const matchType = (currentTypology === 'all') || (p.typology.toLowerCase() === currentTypology.toLowerCase());
      const matchCompletion = (currentCompletion === 'all') ||
        (currentCompletion === 'built' && p.status === 'Completion') ||
        (currentCompletion === 'concept' && p.status !== 'Completion');
      return matchType && matchCompletion;
    }

    function renderCards() {
      const container = document.getElementById('works-grid');
      if (!container) return;
      container.innerHTML = '';

      const hasActiveFilter = (currentTypology !== 'all') || (currentCompletion !== 'all');
      const badge = document.getElementById('active-filter-badge');
      if (badge) {
        if ((currentCompletion !== 'all') || (currentTypology !== 'all') || (currentRecency !== 'newest')) {
          badge.classList.remove('hidden');
        } else {
          badge.classList.add('hidden');
        }
      }

      const sortComparator = (a, b) => {
        const yearA = parseInt(a.year, 10) || 0;
        const yearB = parseInt(b.year, 10) || 0;
        if (yearA !== yearB) {
          return currentRecency === 'newest' ? (yearB - yearA) : (yearA - yearB);
        }
        return (a._origIndex || 0) - (b._origIndex || 0);
      };

      let ordered;
      if (!hasActiveFilter) {
        ordered = [...PROJECTS].sort(sortComparator);
      } else {
        const matching = PROJECTS.filter(p => isMatch(p)).sort(sortComparator);
        const nonMatching = PROJECTS.filter(p => !isMatch(p)).sort(sortComparator);
        ordered = [...matching, ...nonMatching];
      }

      activeOrderedList = ordered;

      activeOrderedList.forEach((p, index) => {
        const card = document.createElement('div');
        const isMatched = isMatch(p);
        card.className = `group cursor-pointer bg-transparent flex flex-col justify-start overflow-hidden transition-opacity duration-300 ${isMatched ? 'opacity-100' : 'opacity-40 hover:opacity-80'}`;
        card.dataset.projectId = p.id;
        card.dataset.typology = p.typology;
        card.dataset.status = p.status;
        card.dataset.year = p.year;
        card.dataset.location = p.location;
        card.dataset.isMatch = isMatched ? 'true' : 'false';

        if (!IS_VARIANT) {
          card.onclick = () => { window.location.href = `projects/${p.id}/`; };
        } else {
          card.onclick = () => openModal(p.id);
        }

        const titleMinH = IS_VARIANT ? 'min-h-[48px]' : 'min-h-[52px] md:min-h-[64px]';

        const cardThumb = (p.image_roles && p.image_roles.card_thumb) || p.primary_image;
        const cardCropMap = {
          'cover-center': 'object-cover object-center',
          'cover-top': 'object-cover object-top',
          'cover-bottom': 'object-cover object-bottom',
          'contain': 'object-contain object-center bg-[#1a1d20]'
        };
        const cardCropCls = cardCropMap[(p.image_crops && p.image_crops.card_thumb) || 'cover-center'] || 'object-cover object-center';

        // Historical Variant Standard (commit 128202d): dedicated space beneath image, title appears on hover/touch
        card.innerHTML = `
          <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
            <img src="${cardThumb}" alt="${p.title}" class="w-full h-full ${cardCropCls} group-hover:scale-105 transition-transform duration-700 ease-out">
          </div>
          <!-- Dedicated space UNDERNEATH image: empty by default on desktop mouse, title appears on hover / touch -->
          <div class="variant-title-space pt-4 pb-5 px-1 ${titleMinH} bg-transparent flex items-start">
            <h3 class="touch-variant-title text-sm md:text-base font-semibold text-[#1a1d20] leading-snug opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0 transition-all duration-300 ease-out __TITLE_FONT_CLS__">
              ${p.title}
            </h3>
          </div>
        `;

        container.appendChild(card);
      });
    }

    // --- Filter Handlers ---
    function setTypology(value, label) {
      currentTypology = value;
      // Update custom dropdown if present
      const labelEl = document.getElementById('typology-dropdown-label');
      if (labelEl) labelEl.textContent = label || value.toUpperCase();
      const btn = document.getElementById('typology-dropdown-btn');
      if (btn) {
        if (value !== 'all') btn.classList.add('active-filter');
        else btn.classList.remove('active-filter');
      }
      document.querySelectorAll('#typology-dropdown-menu .custom-dropdown-item').forEach(item => {
        if (item.dataset.value === value) item.classList.add('selected');
        else item.classList.remove('selected');
      });
      // Update native select if present
      const natSel = document.getElementById('native-typology-select');
      if (natSel) {
        natSel.value = value;
        if (value !== 'all') natSel.classList.add('active-filter');
        else natSel.classList.remove('active-filter');
      }
      closeAllDropdowns();
      renderCards();
    }

    function setCompletion(value, label) {
      currentCompletion = value;
      // Update custom dropdown
      const labelEl = document.getElementById('completion-dropdown-label');
      if (labelEl) labelEl.textContent = label || value.toUpperCase();
      const btn = document.getElementById('completion-dropdown-btn');
      if (btn) {
        if (value !== 'all') btn.classList.add('active-filter');
        else btn.classList.remove('active-filter');
      }
      document.querySelectorAll('#completion-dropdown-menu .custom-dropdown-item').forEach(item => {
        if (item.dataset.value === value) item.classList.add('selected');
        else item.classList.remove('selected');
      });
      // Update native select
      const natSel = document.getElementById('native-completion-select');
      if (natSel) {
        natSel.value = value;
        if (value !== 'all') natSel.classList.add('active-filter');
        else natSel.classList.remove('active-filter');
      }
      closeAllDropdowns();
      renderCards();
    }

    function setRecency(value, label) {
      currentRecency = value;
      // Update custom dropdown
      const labelEl = document.getElementById('recency-dropdown-label');
      if (labelEl) labelEl.textContent = label || value.toUpperCase();
      const btn = document.getElementById('recency-dropdown-btn');
      if (btn) {
        if (value !== 'newest') btn.classList.add('active-filter');
        else btn.classList.remove('active-filter');
      }
      document.querySelectorAll('#recency-dropdown-menu .custom-dropdown-item').forEach(item => {
        if (item.dataset.value === value) item.classList.add('selected');
        else item.classList.remove('selected');
      });
      // Update native select
      const natSel = document.getElementById('native-recency-select');
      if (natSel) {
        natSel.value = value;
        if (value !== 'newest') natSel.classList.add('active-filter');
        else natSel.classList.remove('active-filter');
      }
      closeAllDropdowns();
      renderCards();
    }

    function toggleCustomDropdown(id) {
      const menu = document.getElementById(id);
      if (!menu) return;
      const isOpen = menu.classList.contains('open');
      closeAllDropdowns();
      if (!isOpen) {
        menu.classList.add('open');
      }
    }

    function closeAllDropdowns() {
      document.querySelectorAll('.custom-dropdown-menu').forEach(menu => {
        menu.classList.remove('open');
      });
    }

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.custom-dropdown-container')) {
        closeAllDropdowns();
      }
    });

    // --- Modal Logic (For Variant) ---
    function openModal(projectId) {
      const idx = activeOrderedList.findIndex(p => p.id === projectId);
      if (idx === -1) return;
      currentModalIndex = idx;
      populateModal(activeOrderedList[currentModalIndex]);
      document.getElementById('project-modal').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
      window.location.hash = `project-${projectId}`;
    }

    function closeModal() {
      const modal = document.getElementById('project-modal');
      if (!modal) return;
      modal.classList.add('hidden');
      document.body.style.overflow = '';
      if (window.location.hash.startsWith('#project-')) {
        history.replaceState(null, null, ' ');
      }
    }

    function navigateModal(direction) {
      currentModalIndex = (currentModalIndex + direction + activeOrderedList.length) % activeOrderedList.length;
      populateModal(activeOrderedList[currentModalIndex]);
      window.location.hash = `project-${activeOrderedList[currentModalIndex].id}`;
    }

    function populateModal(p) {
      document.getElementById('modal-title').textContent = p.title;
      document.getElementById('modal-typology').textContent = p.typology;
      document.getElementById('modal-status').textContent = p.status === 'Completion' ? 'Built Commission' : 'Design Exploration';
      document.getElementById('modal-location-year').textContent = `${p.location} • ${p.year}`;
      document.getElementById('modal-description').textContent = p.description;

      const awardBox = document.getElementById('modal-award-box');
      const awardText = document.getElementById('modal-award-text');
      if (p.award && p.awardText) {
        awardBox.classList.remove('hidden');
        awardText.textContent = p.awardText;
      } else {
        awardBox.classList.add('hidden');
      }

      const pageLink = document.getElementById('modal-project-link');
      if (pageLink) {
        pageLink.href = `projects/${p.id}/`;
      }

      const mainImg = document.getElementById('modal-main-img');
      mainImg.src = p.primary_image;

      const thumbs = document.getElementById('modal-thumbs');
      thumbs.innerHTML = '';
      if (p.images && p.images.length > 0) {
        p.images.forEach(imgUrl => {
          const t = document.createElement('img');
          t.src = imgUrl;
          t.className = 'w-16 h-12 object-cover cursor-pointer opacity-80 hover:opacity-100 transition-opacity shrink-0';
          t.onclick = () => { mainImg.src = imgUrl; };
          thumbs.appendChild(t);
        });
      }
    }

    window.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        closeModal();
        if (typeof closeWorkflowLightbox === 'function') closeWorkflowLightbox();
      }
      const pm = document.getElementById('project-modal');
      if (pm && !pm.classList.contains('hidden')) {
        if (e.key === 'ArrowLeft') navigateModal(-1);
        if (e.key === 'ArrowRight') navigateModal(1);
      }
    });

    function toggleMobileMenu() {
      const menu = document.getElementById('mobile-nav-menu');
      if (menu) menu.classList.toggle('hidden');
    }
    function closeMobileMenu() {
      const menu = document.getElementById('mobile-nav-menu');
      if (menu) menu.classList.add('hidden');
    }

    function openWorkflowLightbox() {
      const lb = document.getElementById('workflow-lightbox');
      if (lb) lb.classList.remove('hidden');
    }
    function closeWorkflowLightbox() {
      const lb = document.getElementById('workflow-lightbox');
      if (lb) lb.classList.add('hidden');
    }

    window.addEventListener('DOMContentLoaded', () => {
      initHeroSlideshow();
      renderCards();
      const pm = document.getElementById('project-modal');
      if (pm) {
        let touchStartX = 0;
        pm.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, { passive: true });
        pm.addEventListener('touchend', e => {
          const diff = e.changedTouches[0].screenX - touchStartX;
          if (Math.abs(diff) > 48) navigateModal(diff < 0 ? 1 : -1);
        }, { passive: true });
      }
      if (window.location.hash.startsWith('#project-')) {
        const slug = window.location.hash.replace('#project-', '');
        openModal(slug);
      }
      initLogoAnimation();
    });

    // High-Fidelity Canvas Spritesheet Player
    function initLogoAnimation() {
      const canvas = document.getElementById('hero-logo-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const sheet = new Image();
      sheet.src = 'assets/official/kad_logo_spritesheet.png';

      const totalFrames = 60;
      const cols = 8;
      const fw = 400, fh = 520;
      const duration = __ANIM_DURATION__;

      sheet.onload = () => {
        let startTime = null;
        function step(now) {
          if (!startTime) startTime = now;
          const elapsed = now - startTime;
          const progress = Math.min(1, elapsed / duration);
          const frameIdx = Math.min(totalFrames - 1, Math.floor(progress * totalFrames));

          const col = frameIdx % cols;
          const row = Math.floor(frameIdx / cols);

          ctx.clearRect(0, 0, fw, fh);
          ctx.drawImage(sheet, col * fw, row * fh, fw, fh, 0, 0, fw, fh);

          if (progress < 1) {
            requestAnimationFrame(step);
          } else {
            // Once animation completes, fade out hero logo after 1.5 seconds per user specification
            const logoWrapper = document.getElementById('hero-logo-wrapper');
            if (logoWrapper) {
              setTimeout(() => {
                logoWrapper.style.transition = 'opacity 1s ease-out';
                logoWrapper.style.opacity = '0';
              }, 1500);
            }
          }
        }
        requestAnimationFrame(step);
      };
    }
  </script>
"""

def generate_landing_page(variant_mode="default"):
    # variant_mode: "default" | "variant" | "variant2"
    is_variant = (variant_mode == "variant")
    is_variant2 = (variant_mode == "variant2")

    if variant_mode == "default":
        title_suffix = "Works Archive (Default — Centered Hero Logo)"
        font_mode = "raleway"
        anim_duration = "3000"
    elif variant_mode == "variant":
        title_suffix = "Works Archive (Variant — Left-Aligned Hero Logo)"
        font_mode = "inter"
        anim_duration = "3000"
    elif variant_mode == "variant2":
        title_suffix = "Works Archive (Variant 2 — Field Architecture)"
        font_mode = "raleway"
        anim_duration = "3000"
    else:
        title_suffix = "Works Archive"
        font_mode = "raleway"
        anim_duration = "3000"

    h1_font = "font-raleway" if font_mode == "raleway" else ""
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    title_font_cls = "font-raleway" if font_mode == "raleway" else ""

    # Hero Logo Placement:
    # Variant A (Default): Centered logo fading out after 1.5s
    # Variant B (Variant): Left-aligned logo matching Content Left Inset Boundary
    if not is_variant:
        # Default: Centerpiece - Centered Dead-Center Across Entire Viewport (50vw & 50vh)
        hero_logo_markup = f"""
    <!-- Centerpiece: White Line-Art Logo Animation (Fades out after 1.5s, centered across entire viewport) -->
    <div id="hero-logo-wrapper" class="relative z-10 flex items-center justify-center pointer-events-none transition-opacity duration-1000">
      <canvas id="hero-logo-canvas" width="400" height="520" class="w-52 sm:w-64 md:w-80 lg:w-[420px] h-auto drop-shadow-2xl"></canvas>
    </div>
"""
    else:
        # Variant: Left-aligned matching Content Left Inset Boundary
        hero_logo_markup = f"""
    <!-- Left-Aligned: White Line-Art Logo Matching Content Left Inset Boundary -->
    <div class="relative z-10 w-full field-content-rail flex flex-col items-start justify-center pointer-events-none">
      <div id="hero-logo-wrapper" class="flex flex-col items-start text-left transition-opacity duration-1000">
        <canvas id="hero-logo-canvas" width="400" height="520" class="w-48 sm:w-56 md:w-72 lg:w-[380px] h-auto drop-shadow-2xl"></canvas>
      </div>
    </div>
"""

    hero_markup = f"""
  <!-- Hero Banner: Interactive Slideshow + Subtle Ambient Motion + Click to Pause + Bottom-Right Borderless CTA -->
  <section id="hero-banner-section" class="relative w-full h-[74svh] sm:h-[80svh] md:h-[90dvh] bg-[#1a1d20] overflow-hidden flex items-center justify-center select-none cursor-pointer">
    
    <!-- Slideshow Background Container with Subtle Ken-Burns Pan/Tilt -->
    <div id="hero-slideshow-container" class="absolute inset-0 w-full h-full">
      <!-- Injected via JS -->
    </div>
    
    <!-- Dark Scrim Veil -->
    <div class="absolute inset-0 bg-black/45 z-5 pointer-events-none"></div>

    {hero_logo_markup}

    <!-- Bottom Pause Status Pill -->
    <div id="hero-pause-indicator" class="hidden absolute top-6 right-6 z-20 text-[10px] font-mono uppercase tracking-[0.2em] bg-black/60 text-[#67aec0] px-3 py-1 pointer-events-none">
      PAUSED
    </div>

    <!-- Plain, Borderless Text CTA Button at Bottom-Right linking to Active Slide's Project Page -->
    <div class="absolute bottom-6 md:bottom-8 right-[var(--field-right-gutter)] z-20">
      <a id="hero-cta-btn" href="#" class="inline-flex items-center gap-2 text-white/90 hover:text-[#de602e] text-xs md:text-sm font-mono uppercase tracking-[0.2em] bg-transparent border-none py-1.5 transition-colors group">
        <span>Details</span>
        <span class="group-hover:translate-x-1.5 transition-transform duration-300">&rarr;</span>
      </a>
    </div>

  </section>
"""

    # Filter Bar Generation:
    # Default: Custom sleek dropdown menus with subtle borders & typography
    # Variant: Native architectural <select> dropdowns
    if not is_variant:
        filter_bar_markup = """
  <!-- Custom Sleek Architectural Dropdown Filters (No Award Filter, Default: Oldest & Concept) -->
  <div class="w-full bg-[#f8f9fa] pt-6 pb-4">
    <div id="filters-wrapper" class="hidden md:flex flex-wrap items-center gap-4 text-xs font-mono uppercase tracking-[0.15em]">
      
      <!-- Filter 1: Typology / Category Dropdown -->
      <div class="custom-dropdown-container">
        <button id="typology-dropdown-btn" onclick="toggleCustomDropdown('typology-dropdown-menu')" class="custom-dropdown-btn">
          <span class="text-[#767676] mr-1">Type:</span>
          <span id="typology-dropdown-label">ALL</span>
          <svg class="w-3 h-3 ml-2 text-[#767676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
        <div id="typology-dropdown-menu" class="custom-dropdown-menu">
          <div onclick="setTypology('all', 'ALL')" data-value="all" class="custom-dropdown-item selected">All Typologies</div>
          <div onclick="setTypology('Residential', 'RESIDENTIAL')" data-value="Residential" class="custom-dropdown-item">Residential</div>
          <div onclick="setTypology('Commercial', 'COMMERCIAL')" data-value="Commercial" class="custom-dropdown-item">Commercial</div>
          <div onclick="setTypology('Cultural', 'CULTURAL')" data-value="Cultural" class="custom-dropdown-item">Cultural</div>
          <div onclick="setTypology('Conceptual', 'CONCEPTUAL')" data-value="Conceptual" class="custom-dropdown-item">Conceptual</div>
          <div onclick="setTypology('Art', 'ART')" data-value="Art" class="custom-dropdown-item">Art</div>
        </div>
      </div>

      <!-- Filter 2: Completion / Status Dropdown (Default Active: CONCEPT) -->
      <div class="custom-dropdown-container">
        <button id="completion-dropdown-btn" onclick="toggleCustomDropdown('completion-dropdown-menu')" class="custom-dropdown-btn active-filter">
          <span class="text-[#767676] mr-1">Status:</span>
          <span id="completion-dropdown-label">CONCEPT</span>
          <svg class="w-3 h-3 ml-2 text-[#767676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
        <div id="completion-dropdown-menu" class="custom-dropdown-menu">
          <div onclick="setCompletion('all', 'ALL STATUS')" data-value="all" class="custom-dropdown-item">All Status</div>
          <div onclick="setCompletion('built', 'BUILT')" data-value="built" class="custom-dropdown-item">Built Commissions</div>
          <div onclick="setCompletion('concept', 'CONCEPT')" data-value="concept" class="custom-dropdown-item selected">Concept / Explorations</div>
        </div>
      </div>

      <!-- Filter 3: Chronological Sort Dropdown (Default Active: OLDEST) -->
      <div class="custom-dropdown-container">
        <button id="recency-dropdown-btn" onclick="toggleCustomDropdown('recency-dropdown-menu')" class="custom-dropdown-btn active-filter">
          <span class="text-[#767676] mr-1">Sort:</span>
          <span id="recency-dropdown-label">OLDEST</span>
          <svg class="w-3 h-3 ml-2 text-[#767676]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
        <div id="recency-dropdown-menu" class="custom-dropdown-menu">
          <div onclick="setRecency('oldest', 'OLDEST')" data-value="oldest" class="custom-dropdown-item selected">Oldest First (Ascending)</div>
          <div onclick="setRecency('newest', 'NEWEST')" data-value="newest" class="custom-dropdown-item">Newest First (Descending)</div>
        </div>
      </div>

    </div>
  </div>
"""
    else:
        filter_bar_markup = """
  <!-- Native Architectural <select> Dropdown Filters (No Award Filter, Default: Oldest & Concept) -->
  <div class="w-full bg-[#f8f9fa] pt-6 pb-4">
    <div id="filters-wrapper" class="hidden md:flex flex-wrap items-center gap-4 text-xs font-mono uppercase tracking-[0.15em]">
      
      <!-- Native Filter 1: Typology -->
      <div class="flex items-center gap-2">
        <label for="native-typology-select" class="text-[#767676]">Type:</label>
        <select id="native-typology-select" onchange="setTypology(this.value, this.options[this.selectedIndex].text)" class="native-architectural-select">
          <option value="all" selected>All Typologies</option>
          <option value="Residential">Residential</option>
          <option value="Commercial">Commercial</option>
          <option value="Cultural">Cultural</option>
          <option value="Conceptual">Conceptual</option>
          <option value="Art">Art</option>
        </select>
      </div>

      <!-- Native Filter 2: Status (Default: Concept) -->
      <div class="flex items-center gap-2">
        <label for="native-completion-select" class="text-[#767676]">Status:</label>
        <select id="native-completion-select" onchange="setCompletion(this.value, this.options[this.selectedIndex].text)" class="native-architectural-select active-filter">
          <option value="all">All Status</option>
          <option value="built">Built</option>
          <option value="concept" selected>Concept</option>
        </select>
      </div>

      <!-- Native Filter 3: Sort (Default: Oldest) -->
      <div class="flex items-center gap-2">
        <label for="native-recency-select" class="text-[#767676]">Sort:</label>
        <select id="native-recency-select" onchange="setRecency(this.value, this.options[this.selectedIndex].text)" class="native-architectural-select active-filter">
          <option value="oldest" selected>Oldest</option>
          <option value="newest">Newest</option>
        </select>
      </div>

    </div>
  </div>
"""

    grid_section = f"""
  <!-- Works Grid Section: Field Architecture Asymmetric Rail (25% Left Offset Desktop, Right Edge Clamped 32-64px) -->
  <section id="works" class="w-full bg-[#f8f9fa] py-12 md:py-16">
    <div class="field-content-rail">
      
      <!-- Section Header + Mobile Filter Toggle -->
      <div class="flex items-center justify-between">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">PORTFOLIO</h2>
        <button id="mobile-filter-toggle" onclick="toggleMobileFilters()" class="md:hidden inline-flex items-center gap-2 py-1 text-xs font-mono uppercase tracking-[0.18em] text-[#38606a] hover:text-[#de602e] transition-colors">
          <span>Filter &amp; Sort</span>
          <span id="active-filter-badge" class="w-2 h-2 rounded-full bg-[#de602e] hidden"></span>
          <svg id="filter-chevron" class="w-3.5 h-3.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
      </div>

      {filter_bar_markup}

      <!-- Project Cards Grid: 20% Reduced Vertical Row Gap (gap-y-6 md:gap-y-7 gap-x-6 md:gap-x-8) -->
      <div id="works-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 mt-6 md:mt-8">
        <!-- Dynamically Rendered Cards with Details Visible Underneath -->
      </div>

    </div>
  </section>
"""

    modal_markup = generate_interactive_modal() if is_variant else ""

    rendered_js = JS_TEMPLATE.replace('__PROJECTS_JSON__', projects_json_str)\
                             .replace('__HERO_SLIDES_JSON__', hero_slides_json_str)\
                             .replace('__IS_VARIANT__', 'true' if is_variant else 'false')\
                             .replace('__ANIM_DURATION__', anim_duration)\
                             .replace('__TITLE_FONT_CLS__', title_font_cls)

    page = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
__SHARED_HEAD__
  <title>Aleksandre Karpov &bull; {title_suffix}</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <main>
{hero_markup}
{grid_section}
{generate_workflow_section(is_variant=is_variant, font_mode=font_mode)}
{generate_accolades_section(is_variant=is_variant, font_mode=font_mode)}
{generate_landing_contact_section(is_variant=is_variant, font_mode=font_mode)}
  </main>

{modal_markup}

__FOOTER__

{rendered_js}
</body>
</html>
"""
    page = page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG))
    page = page.replace('__HEADER__', generate_header(active_nav="works", borderless=True, is_variant=is_variant, font_mode=font_mode))
    page = page.replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", is_variant=is_variant, font_mode=font_mode))
    return page

def generate_about_page():
    page = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
__SHARED_HEAD__
  <title>Aleksandre Karpov — About &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <main class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      
      <div class="space-y-12 max-w-5xl">
        
        <!-- Header -->
        <div>
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-semibold tracking-tight text-[#1a1d20] font-raleway">
            Aleksandre Karpov
          </h1>
          <p class="text-xs font-mono uppercase tracking-wider text-[#67aec0] font-semibold mt-3">
            B.A. in Architecture &bull; UNCC &bull; Lund University (Sweden)
          </p>
        </div>

        <!-- Profile Section: Side-by-Side Portrait & Bio (Completely Borderless) -->
        <div class="flex flex-col md:flex-row items-start gap-10 lg:gap-14">
          
          <!-- Portrait sitting directly on #f8f9fa, zero borders, zero white cards -->
          <div class="w-full md:w-80 lg:w-96 shrink-0 flex flex-col">
            <div class="w-full aspect-[4/5] bg-transparent overflow-hidden">
              <img src="assets/official/alex_portrait.png" alt="Aleksandre Karpov" class="w-full h-full object-cover">
            </div>
            <div class="mt-4">
              <span class="text-sm font-semibold tracking-wider uppercase text-[#1a1d20] block font-raleway">Aleksandre Karpov</span>
              <span class="text-xs font-mono text-[#67aec0] uppercase tracking-widest block mt-1">Principal &bull; Karpov Design LLC</span>
            </div>
          </div>

          <!-- Bio Narrative (Authentic portfolio statement & CV) -->
          <div class="flex-1 space-y-6">
            <h2 class="text-xl md:text-2xl lg:text-3xl font-semibold text-[#38606a] tracking-tight leading-snug font-raleway">
              Fine Art Foundations &amp; Virtual Construction
            </h2>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              Aleksandre Karpov operates at the convergence of tactile draftsmanship and advanced digital building information modeling. Raised with a rigorous foundation in classical drawing, watercolor plein-air representation, and structural sculpture, he approaches each project with visceral sensitivity to materials, topography, and natural light.
            </p>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed italic">
              &ldquo;The act of design is a process deeply rooted in physical reality, yet has no absolute future as our surroundings continuously change. They are changed by us and they change us, becoming an integral player in the human experiment.&rdquo;
            </p>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              Prior to establishing Karpov Design LLC, Aleksandre managed design, municipal documentation, and construction administration for over 20 commercial projects at RD&amp;D in Charlotte, NC, and served as project designer and BIM manager at Aboutblank in Istanbul across international competition victories and realized commercial developments.
            </p>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              As principal of <span class="text-[#2b4951] font-semibold">Karpov Design LLC</span> in Charlotte, NC, he provides complete residential design commissions and consulting services.
            </p>
          </div>

        </div>

      </div>

    </div>
  </main>

__FOOTER__

</body>
</html>
"""
    page = page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG))
    page = page.replace('__HEADER__', generate_header(active_nav="about", borderless=True, font_mode="raleway"))
    page = page.replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway"))
    return page

def generate_contact_page():
    page = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
__SHARED_HEAD__
  <title>Contact & Inquiries — Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <main class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      
      <div class="max-w-4xl space-y-12">
        
        <!-- Heading & Direct Coordinates (Authentic from d13ccec) -->
        <div class="space-y-8">
          <div>
            <h1 class="text-3xl md:text-5xl font-semibold tracking-tight text-[#38606a] mb-4 font-raleway">Get in touch</h1>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed max-w-2xl">
              For residential design commissions, computational BIM consulting, or competition collaborations, reach out directly.
            </p>
          </div>

          <!-- Direct Coordinates Grid (Borderless, Plain Charlotte NC) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8 pt-2">
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">United States Direct</span>
              <a href="tel:+17048459596" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                +1 (704) 845-9596
              </a>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">International Line</span>
              <a href="tel:+905385907458" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                +90 (538) 590-7458
              </a>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Electronic Mail</span>
              <a href="mailto:contact@karpovdesign.com" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                contact@karpovdesign.com
              </a>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Studio Location</span>
              <span class="text-base font-semibold text-[#2b4951] mt-1.5 block">Charlotte, NC</span>
            </div>
          </div>
        </div>

        <!-- Streamlined 3-Field Mandatory Form (Underline inputs, borderless, seamless inline success) -->
        <div id="contact-form-container">
          <form id="contact-form" onsubmit="event.preventDefault(); showContactSuccess();" class="space-y-8 pt-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Name *</label>
                <input type="text" required placeholder="Your full name" class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50">
              </div>
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Email *</label>
                <input type="email" required placeholder="your.email@domain.com" class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50">
              </div>
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Project Scope &amp; Description *</label>
              <textarea id="contact-scope-textarea" rows="5" required placeholder="Describe your vision, site parameters, approximate square footage, or project timeline..." class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50 resize-y"></textarea>
            </div>
            <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pt-2">
              <span class="text-xs text-[#595f65]">Confidentiality guaranteed. Direct response within 24 business hours.</span>
              <button type="submit" class="inline-flex items-center gap-2 text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#1a1d20] hover:text-[#de602e] bg-transparent border-none py-2 transition-colors group cursor-pointer">
                <span>Submit Inquiry</span>
                <span class="group-hover:translate-x-1.5 transition-transform duration-300">&rarr;</span>
              </button>
            </div>
          </form>
          <div id="contact-success-msg" class="hidden py-10 space-y-3">
            <h3 class="text-2xl font-semibold text-[#1a1d20] font-raleway">Inquiry Received</h3>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">Thank you. Your message has been sent directly to Aleksandre Karpov. We will respond within 24 business hours.</p>
          </div>
        </div>
        <script>
          function showContactSuccess() {{
            document.getElementById('contact-form').classList.add('hidden');
            document.getElementById('contact-success-msg').classList.remove('hidden');
          }}
        </script>

      </div>

    </div>
  </main>

__FOOTER__

</body>
</html>
"""
    page = page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG))
    page = page.replace('__HEADER__', generate_header(active_nav="contact", borderless=True, font_mode="raleway"))
    page = page.replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway"))
    return page

def generate_academy_page():
    page = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
__SHARED_HEAD__
  <title>Academy & Computation — Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <main class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      
      <div class="max-w-4xl space-y-12">
        <div>
          <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-[#1a1d20] mb-6 font-raleway">
            Architectural Academy
          </h1>
          <p class="text-base text-[#595f65] leading-relaxed">
            Computational design workflows, parametric generative scripts, and tectonic form-finding masterclasses authored by Aleksandre Karpov.
          </p>
        </div>

        <div class="space-y-6">
          <div class="flex items-center justify-between pb-2">
            <h3 class="text-lg font-semibold text-[#1a1d20]">Algorithmic Massing &amp; Solar Optimization</h3>
            <span class="text-xs font-mono text-[#de602e] uppercase tracking-widest">Grasshopper &bull; Python</span>
          </div>
          <p class="text-sm text-[#595f65] leading-relaxed">
            Curriculum covering automated solar-path radiation analysis, kinetic facade kinematics, and topological optimization for complex structural shells.
          </p>
        </div>
      </div>

    </div>
  </main>

__FOOTER__

</body>
</html>
"""
    page = page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG))
    page = page.replace('__HEADER__', generate_header(active_nav="", borderless=True, font_mode="raleway"))
    page = page.replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway"))
    return page

def build_project_lightbox_markup_and_script(project_title, images, base_path=""):
    full_images = [f"{base_path}{img}" for img in images]
    images_json = json.dumps(full_images).replace('</script>', '<\\/script>')
    escaped_title = project_title.replace('"', '&quot;')

    markup = f"""
  <!-- Full-Viewport Image Lightbox Modal -->
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/95 backdrop-blur-md hidden flex flex-col items-center justify-between p-4 md:p-6 cursor-pointer select-none" onclick="handleLightboxClick(event)">
    <button onclick="closeLightbox(); event.stopPropagation();" class="fixed top-4 left-6 z-60 text-[#67aec0] hover:text-[#de602e] text-3xl font-bold bg-transparent border-none p-2 cursor-pointer transition-colors focus:outline-none" title="Close (Esc)" aria-label="Close popup">&times;</button>

    <div class="w-full flex items-center justify-end text-white/80 pt-2 pointer-events-none px-6">
      <span id="lightbox-counter" class="text-xs font-mono uppercase tracking-widest bg-[#2b4951]/80 px-3 py-1.5 text-[#e4f0f2]">Plate 1 of {len(full_images)}</span>
    </div>

    <div class="relative w-full flex-1 flex items-center justify-center my-2 select-none">
      <button onclick="navigateLightbox(-1); event.stopPropagation();" class="absolute left-1 md:left-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none cursor-pointer" title="Previous" aria-label="Previous image">&larr;</button>
      <img id="lightbox-img" src="" alt="Enlarged Project Plate" class="max-w-[86vw] md:max-w-[85vw] max-h-[82vh] object-contain drop-shadow-2xl transition-all duration-300" onclick="event.stopPropagation()">
      <button onclick="navigateLightbox(1); event.stopPropagation();" class="absolute right-1 md:right-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none cursor-pointer" title="Next" aria-label="Next image">&rarr;</button>
    </div>

    <div class="w-full text-center pb-2 text-white/70 text-xs font-mono pointer-events-none">
      <span id="lightbox-caption">{project_title}</span>
    </div>
  </div>

  <script>
    const GALLERY_IMAGES = {images_json};
    let currentLightboxIdx = 0;

    function openLightbox(target) {{
      if (!GALLERY_IMAGES || GALLERY_IMAGES.length === 0) return;
      let idx = 0;
      if (typeof target === 'number') {{
        idx = target;
      }} else if (typeof target === 'string') {{
        const cleanTarget = target.replace(/^(\\.\\.\\/)+/, '');
        const found = GALLERY_IMAGES.findIndex(img => img === target || img.endsWith(cleanTarget));
        idx = found !== -1 ? found : 0;
      }}
      currentLightboxIdx = ((idx % GALLERY_IMAGES.length) + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightbox();
      const lb = document.getElementById('image-lightbox');
      if (lb) lb.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      const lb = document.getElementById('image-lightbox');
      if (lb) lb.classList.add('hidden');
      document.body.style.overflow = '';
    }}

    function navigateLightbox(dir) {{
      if (!GALLERY_IMAGES || GALLERY_IMAGES.length === 0) return;
      currentLightboxIdx = (currentLightboxIdx + dir + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightbox();
    }}

    function updateLightbox() {{
      if (!GALLERY_IMAGES || GALLERY_IMAGES.length === 0) return;
      const img = document.getElementById('lightbox-img');
      const counter = document.getElementById('lightbox-counter');
      if (img) {{
        img.src = GALLERY_IMAGES[currentLightboxIdx];
        img.alt = "{escaped_title} — Plate " + (currentLightboxIdx + 1);
      }}
      if (counter) counter.textContent = `Plate ${{currentLightboxIdx + 1}} of ${{GALLERY_IMAGES.length}}`;
    }}

    function handleLightboxClick(e) {{
      if (e.target.closest('#lightbox-img') || e.target.closest('button')) return;
      closeLightbox();
    }}

    window.addEventListener('keydown', e => {{
      const lb = document.getElementById('image-lightbox');
      if (lb && !lb.classList.contains('hidden')) {{
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') navigateLightbox(-1);
        if (e.key === 'ArrowRight') navigateLightbox(1);
      }}
    }});
  </script>
"""
    return markup


def generate_dawnridge_project_page(p, prev_p, next_p, base_path="../../"):
    roles = get_project_image_roles(p)
    crops = get_project_image_crops(p)
    images = p.get('images', [])

    def src_of(slot):
        rel = roles.get(slot, '')
        return f"{base_path}{rel}" if rel else ''

    def crop_cls(slot):
        return crop_mode_to_class(crops.get(slot, 'cover-center'))

    award_markup = ""
    if p.get('award') and p.get('awardText'):
        award_markup = f"""
            <div class="pt-1">
              <span class="text-xs font-mono uppercase tracking-widest text-[#de602e] font-semibold">{p['awardText']}</span>
            </div>"""

    home_url = f"{base_path}index.html"
    works_url = f"{base_path}index.html#works"
    prev_url = f"{base_path}projects/{prev_p['id']}/"
    next_url = f"{base_path}projects/{next_p['id']}/"

    head_html = SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG)
    if base_path:
        head_html = head_html.replace('href="assets/official/', f'href="{base_path}assets/official/')

    header_html = generate_header(active_nav="works", borderless=True, font_mode="raleway", base_path=base_path)
    footer_html = generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway", base_path=base_path)
    lightbox_html = build_project_lightbox_markup_and_script(p['title'], images, base_path=base_path)

    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
{head_html}
  <title>{p['title']} — Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

{header_html}

  <main class="w-full bg-[#f8f9fa]">
    <!-- Slot 1: Top Full-Bleed Hero (Zero Text Overlay) -->
    <section id="project-hero-banner" data-project-id="{p['id']}" data-slot-key="hero_image" data-slot-label="Top Full-Bleed Hero" onclick="openLightbox('{roles.get('hero_image', '')}')" class="relative w-full h-[75vh] md:h-[88vh] bg-[#1a1d20] overflow-hidden cursor-pointer group">
      <img src="{src_of('hero_image')}" alt="{p['title']} — Hero View" data-slot-key="hero_image" class="w-full h-full {crop_cls('hero_image')} group-hover:scale-[1.01] transition-transform duration-700 ease-out">
    </section>

    <!-- Centered 720px Dawnridge Editorial Rail -->
    <div class="max-w-[720px] mx-auto px-5 sm:px-6 py-14 md:py-20 space-y-12 md:space-y-16">
      <!-- Section 1: 2-Column Title, Narrative & Concept Sketch Pair -->
      <section class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-10 items-center">
        <div class="space-y-4">
          <h1 class="text-2xl sm:text-3xl font-semibold tracking-[0.14em] uppercase text-[#1a1d20] font-raleway">
            {p['title']}
          </h1>
          <p class="text-sm sm:text-[15px] text-[#595f65] leading-relaxed">
            {p['description']}
          </p>
          {award_markup}
        </div>
        <div data-project-id="{p['id']}" data-slot-key="sketch_image" data-slot-label="Concept Sketch / Diagram" onclick="openLightbox('{roles.get('sketch_image', '')}')" class="cursor-pointer group overflow-hidden bg-transparent">
          <img src="{src_of('sketch_image')}" alt="{p['title']} — Concept Sketch" data-slot-key="sketch_image" class="w-full h-auto {crop_cls('sketch_image')} group-hover:scale-[1.02] transition-transform duration-500 ease-out">
        </div>
      </section>

      <!-- Slot 3: Centered Single Landscape Plate -->
      <section data-project-id="{p['id']}" data-slot-key="landscape_1" data-slot-label="Primary Landscape Plate" onclick="openLightbox('{roles.get('landscape_1', '')}')" class="cursor-pointer group overflow-hidden bg-[#1a1d20]">
        <img src="{src_of('landscape_1')}" alt="{p['title']} — Landscape Plate" data-slot-key="landscape_1" class="w-full h-auto {crop_cls('landscape_1')} group-hover:scale-[1.02] transition-transform duration-700 ease-out">
      </section>

      <!-- Slots 4 & 5: Centered 2-Column Vertical Pair (4:5, 12px gutter) -->
      <section class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div data-project-id="{p['id']}" data-slot-key="pair_1a" data-slot-label="Vertical Pair Left (4:5)" onclick="openLightbox('{roles.get('pair_1a', '')}')" class="cursor-pointer group overflow-hidden bg-[#1a1d20] aspect-[4/5]">
          <img src="{src_of('pair_1a')}" alt="{p['title']} — Vertical Study 1" data-slot-key="pair_1a" class="w-full h-full {crop_cls('pair_1a')} group-hover:scale-[1.03] transition-transform duration-700 ease-out">
        </div>
        <div data-project-id="{p['id']}" data-slot-key="pair_1b" data-slot-label="Vertical Pair Right (4:5)" onclick="openLightbox('{roles.get('pair_1b', '')}')" class="cursor-pointer group overflow-hidden bg-[#1a1d20] aspect-[4/5]">
          <img src="{src_of('pair_1b')}" alt="{p['title']} — Vertical Study 2" data-slot-key="pair_1b" class="w-full h-full {crop_cls('pair_1b')} group-hover:scale-[1.03] transition-transform duration-700 ease-out">
        </div>
      </section>

      <!-- Slot 6: Centered Secondary Landscape / Cutaway Plate -->
      <section data-project-id="{p['id']}" data-slot-key="landscape_2" data-slot-label="Secondary Landscape / Cutaway" onclick="openLightbox('{roles.get('landscape_2', '')}')" class="cursor-pointer group overflow-hidden bg-transparent">
        <img src="{src_of('landscape_2')}" alt="{p['title']} — Spatial Cutaway" data-slot-key="landscape_2" class="w-full h-auto {crop_cls('landscape_2')} group-hover:scale-[1.02] transition-transform duration-700 ease-out">
      </section>

      <!-- Slots 7 & 8: Centered 2-Column Study Pair (4:3, 12px gutter) -->
      <section class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div data-project-id="{p['id']}" data-slot-key="pair_2a" data-slot-label="Study Pair Left (4:3)" onclick="openLightbox('{roles.get('pair_2a', '')}')" class="cursor-pointer group overflow-hidden bg-white aspect-[4/3]">
          <img src="{src_of('pair_2a')}" alt="{p['title']} — Detail Study 1" data-slot-key="pair_2a" class="w-full h-full {crop_cls('pair_2a')} group-hover:scale-[1.03] transition-transform duration-700 ease-out">
        </div>
        <div data-project-id="{p['id']}" data-slot-key="pair_2b" data-slot-label="Study Pair Right (4:3)" onclick="openLightbox('{roles.get('pair_2b', '')}')" class="cursor-pointer group overflow-hidden bg-white aspect-[4/3]">
          <img src="{src_of('pair_2b')}" alt="{p['title']} — Detail Study 2" data-slot-key="pair_2b" class="w-full h-full {crop_cls('pair_2b')} group-hover:scale-[1.03] transition-transform duration-700 ease-out">
        </div>
      </section>
    </div>

    <!-- Slot 9: Bottom Full-Bleed Bookend Banner (100vw) -->
    <section data-project-id="{p['id']}" data-slot-key="banner_image" data-slot-label="Bottom Full-Bleed Banner" onclick="openLightbox('{roles.get('banner_image', '')}')" class="relative w-full h-[65vh] md:h-[82vh] bg-[#1a1d20] overflow-hidden cursor-pointer group">
      <img src="{src_of('banner_image')}" alt="{p['title']} — Panoramic Banner" data-slot-key="banner_image" class="w-full h-full {crop_cls('banner_image')} group-hover:scale-[1.01] transition-transform duration-700 ease-out">
    </section>

    <!-- Borderless Linear Project Pagination Bar (Zero Clutter) -->
    <div class="w-full bg-[#f8f9fa] py-12 md:py-16">
      <div class="max-w-[720px] mx-auto px-5 sm:px-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-sm sm:text-base font-medium text-[#1a1d20] font-raleway">
        <a href="{prev_url}" class="py-1 hover:text-[#de602e] transition-colors flex items-center gap-2">
          <span>&lsaquo;</span>
          <span>{prev_p['title']}</span>
        </a>
        <a href="{next_url}" class="py-1 hover:text-[#de602e] transition-colors flex items-center sm:justify-end gap-2 sm:text-right">
          <span>{next_p['title']}</span>
          <span>&rsaquo;</span>
        </a>
      </div>
    </div>
  </main>

{lightbox_html}

{footer_html}

</body>
</html>
"""


def generate_grid_variant_project_page(p, prev_p, next_p, base_path="../../../"):
    roles = get_project_image_roles(p)
    crops = get_project_image_crops(p)
    hero_rel = roles.get('hero_image') or get_best_hero_image(p)
    hero_src = f"{base_path}{hero_rel}"
    hero_crop_cls = crop_mode_to_class(crops.get('hero_image', 'cover-center'))

    award_markup = ""
    if p.get('award') and p.get('awardText'):
        award_markup = f"""
            <div class="py-2">
              <span class="text-xs font-mono uppercase tracking-widest text-[#de602e] font-semibold">{p['awardText']}</span>
            </div>
"""

    images = p.get('images', [])
    gallery_html = ""
    for idx, img_path in enumerate(images):
        gallery_html += f"""
            <div onclick="openLightbox({idx})" class="group cursor-pointer bg-transparent flex flex-col justify-start overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden bg-[#1a1d20]">
                <img src="{base_path}{img_path}" alt="{p['title']} — Plate {idx+1}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/15 transition-colors duration-300 flex items-end justify-end p-4">
                  <span class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-[#1a1d20]/85 text-white text-[10px] font-mono uppercase tracking-[0.2em] px-3 py-1.5">Enlarge</span>
                </div>
              </div>
            </div>
"""

    home_url = f"{base_path}index.html"
    works_url = f"{base_path}index.html#works"
    prev_url = f"{base_path}projects/{prev_p['id']}/variant/"
    next_url = f"{base_path}projects/{next_p['id']}/variant/"

    head_html = SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG)
    if base_path:
        head_html = head_html.replace('href="assets/official/', f'href="{base_path}assets/official/')

    header_html = generate_header(active_nav="works", borderless=True, font_mode="raleway", base_path=base_path)
    footer_html = generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway", base_path=base_path)
    lightbox_html = build_project_lightbox_markup_and_script(p['title'], images, base_path=base_path)

    template = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
{head_html}
  <title>{p['title']} (Grid Variant) — Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

{header_html}

  <main>
    <!-- Dedicated Hero Banner: Secondary Metadata (Date, Location) OMITTED per User Rule -->
    <section id="project-hero-banner" data-project-id="{p['id']}" data-slot-key="hero_image" data-slot-label="Top Hero Banner" class="relative w-full h-[52svh] sm:h-[60vh] md:h-[75vh] bg-[#1a1d20] overflow-hidden flex items-end">
      <img src="{hero_src}" alt="{p['title']}" data-slot-key="hero_image" class="absolute inset-0 w-full h-full {hero_crop_cls}">
      <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-black/20"></div>

      <!-- Hero Title Only (Secondary metadata omitted) -->
      <div class="relative z-10 field-content-rail pb-8 md:pb-12">
        <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-white drop-shadow-md font-raleway">{p['title']}</h1>
      </div>
    </section>

    <!-- Main Content: Field Architecture Asymmetric Rail -->
    <section class="w-full bg-[#f8f9fa] py-12 md:py-16">
      <div class="field-content-rail space-y-12">
        
        <!-- Narrative & Description (Zero Visible Clutter, Metadata preserved in head JSON-LD) -->
        <div class="space-y-4 max-w-4xl">
          <p class="text-sm sm:text-base md:text-lg text-[#595f65] leading-relaxed">
            {p['description']}
          </p>
          {award_markup}
        </div>

        <!-- Large Images Gallery -->
        <div class="pt-2">
          <div id="project-gallery" class="grid grid-cols-1 md:grid-cols-2 gap-x-6 md:gap-x-8 gap-y-6 md:gap-y-7">
            {gallery_html}
          </div>
        </div>

        <!-- Prev / Next Navigation (Borderless) -->
        <div class="pt-8 md:pt-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs font-mono uppercase tracking-widest">
          <a href="{prev_url}" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center gap-2">
            &larr; Prev: {prev_p['title']}
          </a>
          <a href="{next_url}" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center sm:justify-end gap-2 sm:text-right">
            Next: {next_p['title']} &rarr;
          </a>
        </div>

      </div>
    </section>
  </main>

{lightbox_html}

{footer_html}

</body>
</html>
"""
    return template

def main():
    print("Building Version 1 (index.html): Centered Hero Logo, Custom Dropdowns, Option 2 Logo (2px boundary clearance)...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="default"))
    print("Saved index.html")

    print("Building Version 2 (variant.html): Left-Aligned Hero Logo, Native Dropdowns, Option 2 Logo...")
    with open('variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="variant"))
    print("Saved variant.html")

    print("Building about.html...")
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(generate_about_page())
    print("Saved about.html")

    print("Building contact.html...")
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(generate_contact_page())
    print("Saved contact.html")

    print("Building academy.html...")
    with open('academy.html', 'w', encoding='utf-8') as f:
        f.write(generate_academy_page())
    print("Saved academy.html")

    print("Building 21 individual project pages (Dawnridge Editorial as Default + Grid Variant) under projects/<id>/...")
    for idx, p in enumerate(projects_data):
        prev_p = projects_data[(idx - 1 + len(projects_data)) % len(projects_data)]
        next_p = projects_data[(idx + 1) % len(projects_data)]

        proj_dir = os.path.join("projects", p['id'])
        os.makedirs(proj_dir, exist_ok=True)
        with open(os.path.join(proj_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(generate_dawnridge_project_page(p, prev_p, next_p, base_path="../../"))

        variant_dir = os.path.join(proj_dir, "variant")
        os.makedirs(variant_dir, exist_ok=True)
        with open(os.path.join(variant_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(generate_grid_variant_project_page(p, prev_p, next_p, base_path="../../../"))

    print(f"Saved {len(projects_data)} Dawnridge editorial project pages and {len(projects_data)} Grid Variant pages!")
    print("Site compilation finished successfully.")

if __name__ == '__main__':
    main()
