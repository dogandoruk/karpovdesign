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
                "url": f"https://dogandoruk.github.io/karpovdesign/project-{p.get('id')}.html",
                "description": p.get("description")
            }
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Aleksandre Karpov Design LLC Architectural Portfolio",
        "description": "Selected architectural commissions, computational forms, and tectonic studies.",
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
               alt="Conceptual Architectural Sketch" 
               class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-500 ease-out">
          <div class="absolute inset-0 bg-black/0 group-hover:bg-black/15 transition-colors duration-300 flex items-end justify-end p-3 pointer-events-none">
            <span class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-[#1a1d20]/80 text-[#67aec0] text-[10px] font-mono uppercase tracking-[0.2em] px-2.5 py-1">Enlarge</span>
          </div>
        </div>

        <div class="w-full md:w-1/2 space-y-4 text-sm md:text-base text-[#595f65] leading-relaxed">
          <p>
            Architectural conception at Karpov Design originates with spontaneous observational drawing and spatial geometry. Hand-drawn travel studies establish fundamental relationships between topographical contours, solar orientation, and tactile materials before digital computation begins.
          </p>
          <p>
            Through rigorous iterative digital modeling and structural optimization, initial tectonic concepts translate into high-performance architectural environments. Each commission balances contextual sensitivity with bold sculptural presence.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Workflow Conceptual Sketch Lightbox Modal -->
  <div id="workflow-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/95 backdrop-blur-md hidden flex flex-col items-center justify-center p-4 md:p-8 cursor-pointer select-none" onclick="closeWorkflowLightbox()">
    <button onclick="closeWorkflowLightbox()" class="fixed top-4 left-6 z-60 text-[#67aec0] hover:text-[#de602e] text-3xl font-bold bg-transparent border-none p-2 cursor-pointer transition-colors focus:outline-none" title="Close (Esc)" aria-label="Close popup">&times;</button>
    <div class="max-w-[94vw] max-h-[88vh] flex flex-col items-center justify-center" onclick="event.stopPropagation()">
      <img src="{sketch_src}" alt="Conceptual Architectural Sketch - Full View" class="max-w-full max-h-[82vh] object-contain drop-shadow-2xl">
      <div class="mt-4 text-center">
        <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#e4f0f2]">Rome &amp; Mediterranean Travel Study &bull; Conceptual Watermark</span>
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
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-8 border-b border-[#e2e5e8]">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">Finalist Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">ArchMedium De Pijp Cultural Center Competition</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">International open architecture competition for Amsterdam's historic De Pijp quarter. Selected among top entries globally.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2016 &bull; Amsterdam, NL</span>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8 pb-8 border-b border-[#e2e5e8]">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">Honor Studio Award</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">UNCC College of Arts + Architecture Studio Excellence</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Design excellence recognition for SEED Artists Getaway high-performance passive timber sanctuary.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2018 &bull; Charlotte, USA</span>
          </div>
        </div>

        <!-- Item 3 -->
        <div class="flex flex-col md:flex-row md:items-start justify-between gap-2 md:gap-8">
          <div class="md:w-1/4">
            <span class="text-xs font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold">Institutional Pedigree</span>
          </div>
          <div class="md:w-2/4">
            <h3 class="text-base md:text-lg font-semibold text-[#1a1d20]">UNCC School of Architecture</h3>
            <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Bachelor of Arts in Architecture. Advanced digital fabrication fellow, Studio X.</p>
          </div>
          <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
            <span>2018–2021 &bull; USA</span>
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
  <section class="w-full bg-[#f8f9fa] py-16 md:py-24">
    <div class="field-content-rail">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6 py-8">
        <div>
          <h2 class="text-xl sm:text-2xl font-semibold tracking-[0.18em] uppercase text-[#1a1d20] {h2_font}">Start a Conversation</h2>
          <p class="text-xs sm:text-sm text-[#595f65] mt-1.5">Bespoke residential & cultural architectural commissions across North Carolina and internationally.</p>
        </div>
        <a href="{contact_url}" class="inline-flex items-center gap-3 px-6 py-3.5 bg-[#1a1d20] hover:bg-[#de602e] text-white text-xs font-mono uppercase tracking-[0.2em] font-medium transition-colors shrink-0 group">
          <span>Get in touch</span>
          <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
        </a>
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
        ctaBtn.href = `project-${HERO_SLIDES[idx].id}.html`;
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
          card.onclick = () => { window.location.href = `project-${p.id}.html`; };
        } else {
          card.onclick = () => openModal(p.id);
        }

        const titleMinH = IS_VARIANT ? 'min-h-[48px]' : 'min-h-[52px] md:min-h-[64px]';

        // Historical Variant Standard (commit 128202d): dedicated space beneath image, title appears on hover/touch
        card.innerHTML = `
          <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
            <img src="${p.primary_image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
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
        pageLink.href = `project-${p.id}.html`;
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
  <title>Aleksandre Karpov — About & Pedigree &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <main class="w-full bg-[#f8f9fa] py-14 md:py-20">
    <div class="field-content-rail">
      
      <div class="space-y-16 max-w-4xl">
        
        <!-- Studio Narrative -->
        <div>
          <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-[#1a1d20] mb-8 font-raleway">
            Design at the Edge of Landscape and Computation
          </h1>
          <div class="space-y-6 text-base md:text-lg text-[#595f65] leading-relaxed">
            <p>
              Aleksandre Karpov Design LLC is an architectural practice based in North Carolina, operating at the intersection of rigorous tectonic thinking, vernacular materiality, and computational form-finding.
            </p>
            <p>
              Each project is approached not as an isolated sculptural object, but as a responsive ecological and spatial field. From private mountain retreats in the Blue Ridge to urban community infrastructure, our methodology privileges environmental resilience, atmospheric lighting, and high-precision construction detailing.
            </p>
          </div>
        </div>

        <!-- Pedigree & Credentials (Completely Borderless) -->
        <div class="pt-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
            <div>
              <h3 class="text-lg font-semibold text-[#1a1d20]">UNCC School of Architecture</h3>
              <p class="text-xs text-[#595f65] mt-1 font-mono">Bachelor of Arts in Architecture (B.A. Arch)</p>
              <p class="text-xs text-[#595f65] mt-2 leading-relaxed">
                Focus on digital fabrication, computational form generation, and high-performance building skins.
              </p>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-[#1a1d20]">Karpov Design LLC</h3>
              <p class="text-xs text-[#595f65] mt-1 font-mono">North Carolina, USA</p>
              <p class="text-xs text-[#595f65] mt-2 leading-relaxed">
                Full-service architectural design consulting, digital visualization, and master planning commissions.
              </p>
            </div>
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
      
      <div class="max-w-3xl space-y-12">
        <div>
          <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-[#1a1d20] mb-6 font-raleway">
            Start a Commission
          </h1>
          <p class="text-base text-[#595f65] leading-relaxed">
            Karpov Design accepts select architectural commissions, master plans, and computational design consultations. Submit your project requirements below.
          </p>
        </div>

        <form id="contact-form" onsubmit="event.preventDefault(); alert('Inquiry recorded. The studio will respond within 24 business hours.');" class="space-y-8">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
            <div>
              <label class="block text-xs font-mono uppercase tracking-widest text-[#595f65] mb-2">Full Name *</label>
              <input type="text" required class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50">
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-widest text-[#595f65] mb-2">Email Address *</label>
              <input type="email" required class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50">
            </div>
          </div>
          <div>
            <label class="block text-xs font-mono uppercase tracking-widest text-[#595f65] mb-2">Project Typology &amp; Location</label>
            <input type="text" placeholder="e.g. Residential Retreat, Asheville NC" class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50">
          </div>
          <div>
            <label class="block text-xs font-mono uppercase tracking-widest text-[#595f65] mb-2">Project Brief / Narrative *</label>
            <textarea rows="4" required class="w-full py-2.5 bg-transparent border-b border-[#e2e5e8] text-sm text-[#1a1d20] focus:outline-none focus:border-[#de602e] transition-colors rounded-none placeholder:text-[#595f65]/50 resize-y"></textarea>
          </div>
          <div class="pt-4">
            <button type="submit" class="inline-flex items-center gap-2.5 text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#1a1d20] hover:text-[#de602e] bg-transparent border-none py-2 transition-colors group">
              <span>Submit Inquiry</span>
              <span class="group-hover:translate-x-1.5 transition-transform duration-300">&rarr;</span>
            </button>
          </div>
        </form>
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

def generate_project_page(p, prev_p, next_p):
    best_hero = get_best_hero_image(p)
    status_label = "Built Commission" if p.get('status') == 'Completion' else "Concept / Exploration"
    
    award_markup = ""
    if p.get('award') and p.get('awardText'):
        award_markup = f"""
            <div class="p-4 bg-white border-l-2 border-[#de602e] border border-[#e2e5e8]">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">Award / Selection</span>
              <p class="text-xs md:text-sm font-semibold text-[#1a1d20] mt-1">{p['awardText']}</p>
            </div>
"""

    images = p.get('images', [])
    images_json = json.dumps(images).replace('</script>', '<\\/script>')
    gallery_html = ""
    for idx, img_path in enumerate(images):
        gallery_html += f"""
            <div onclick="openLightbox({idx})" class="group cursor-pointer bg-transparent flex flex-col justify-start overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden bg-[#1a1d20]">
                <img src="{img_path}" alt="{p['title']} — Plate {idx+1}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/15 transition-colors duration-300 flex items-end justify-end p-4">
                  <span class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-[#1a1d20]/85 text-white text-[10px] font-mono uppercase tracking-[0.2em] px-3 py-1.5">Enlarge</span>
                </div>
              </div>
            </div>
"""

    template = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
__SHARED_HEAD__
  <title>{p['title']} — Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

__HEADER__

  <!-- Breadcrumb Navigation -->
  <div class="w-full bg-[#f8f9fa] py-4">
    <nav aria-label="Breadcrumb" class="field-content-rail text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65] flex items-center justify-between overflow-x-auto no-scrollbar whitespace-nowrap">
      <div class="flex items-center">
        <a href="index.html" class="hover:text-[#1a1d20] transition-colors shrink-0">Home</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <a href="index.html#works" class="hover:text-[#1a1d20] transition-colors shrink-0">Works</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <span class="text-[#1a1d20] font-semibold truncate">{p['title']}</span>
      </div>
    </nav>
  </div>

  <main>
    <!-- Dedicated Hero Banner: Secondary Metadata (Date, Location) OMITTED per User Rule -->
    <section id="project-hero-banner" class="relative w-full h-[52svh] sm:h-[60vh] md:h-[75vh] bg-[#1a1d20] overflow-hidden flex items-end">
      <img src="{best_hero}" alt="{p['title']}" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-black/20"></div>

      <!-- Hero Title Only (Secondary metadata omitted) -->
      <div class="relative z-10 field-content-rail pb-8 md:pb-12">
        <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-white drop-shadow-md font-raleway">{p['title']}</h1>
      </div>
    </section>

    <!-- Main Content: Field Architecture Asymmetric Rail -->
    <section class="w-full bg-[#f8f9fa] py-12 md:py-16">
      <div class="field-content-rail space-y-12">
        
        <!-- Narrative & Brief -->
        <div class="space-y-6 max-w-4xl">
          <div class="pb-2">
            <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block mb-3">Project Brief &amp; Spatial Strategy</span>
            <p class="text-sm sm:text-base md:text-lg text-[#1a1d20] leading-relaxed">
              {p['description']}
            </p>
          </div>

          {award_markup}

          <!-- Specifications Table -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-[#e2e5e8]">
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0]">Typology</span>
              <span class="text-sm font-semibold text-[#2b4951] block mt-1">{p['typology']}</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0]">Status</span>
              <span class="text-sm font-semibold text-[#2b4951] block mt-1">{status_label}</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0]">Location</span>
              <span class="text-sm font-semibold text-[#2b4951] block mt-1">{p['location']}</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0]">Year</span>
              <span class="text-sm font-semibold text-[#2b4951] block mt-1">{p['year']}</span>
            </div>
          </div>
        </div>

        <!-- Large Images Gallery: Consistent 20% Reduced Vertical Row Gap (gap-y-6 md:gap-y-7 gap-x-6 md:gap-x-8) -->
        <div>
          <h2 class="text-lg md:text-xl font-semibold tracking-[0.25em] uppercase text-[#38606a] mb-6 md:mb-8 font-raleway">Visual Documentation &amp; Plates</h2>
          <div id="project-gallery" class="grid grid-cols-1 md:grid-cols-2 gap-x-6 md:gap-x-8 gap-y-6 md:gap-y-7">
            {gallery_html}
          </div>
        </div>

        <!-- Prev / Next Navigation -->
        <div class="pt-8 md:pt-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs font-mono uppercase tracking-widest border-t border-[#e2e5e8]">
          <a href="project-{prev_p['id']}.html" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center gap-2">
            &larr; Prev: {prev_p['title']}
          </a>
          <a href="project-{next_p['id']}.html" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center sm:justify-end gap-2 sm:text-right">
            Next: {next_p['title']} &rarr;
          </a>
        </div>

      </div>
    </section>
  </main>

  <!-- Image Lightbox Modal -->
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/95 backdrop-blur-md hidden flex flex-col items-center justify-between p-4 md:p-6 cursor-pointer select-none" onclick="handleLightboxClick(event)">
    <button onclick="closeLightbox()" class="fixed top-4 left-6 z-60 text-[#67aec0] hover:text-[#de602e] text-3xl font-bold bg-transparent border-none p-2 cursor-pointer transition-colors focus:outline-none" title="Close (Esc)" aria-label="Close popup">&times;</button>
    
    <div class="w-full flex items-center justify-end text-white/80 pt-2 pointer-events-none px-6">
      <span id="lightbox-counter" class="text-xs font-mono uppercase tracking-widest bg-[#2b4951]/80 px-3 py-1.5 text-[#e4f0f2]">Plate 1 of {len(images)}</span>
    </div>

    <div class="relative w-full flex-1 flex items-center justify-center my-2 select-none">
      <button onclick="navigateLightbox(-1); event.stopPropagation();" class="absolute left-1 md:left-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none" title="Previous">&larr;</button>
      <img id="lightbox-img" src="" alt="Enlarged Project Plate" class="max-w-[94vw] max-h-[82vh] object-contain drop-shadow-2xl transition-all duration-300">
      <button onclick="navigateLightbox(1); event.stopPropagation();" class="absolute right-1 md:right-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none" title="Next">&rarr;</button>
    </div>

    <div class="w-full text-center pb-2 text-white/70 text-xs font-mono pointer-events-none">
      <span id="lightbox-caption">{p['title']}</span>
    </div>
  </div>

__FOOTER__

  <script>
    const GALLERY_IMAGES = {images_json};
    let currentLightboxIdx = 0;

    function openLightbox(idx) {{
      currentLightboxIdx = idx;
      updateLightbox();
      document.getElementById('image-lightbox').classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      const lb = document.getElementById('image-lightbox');
      if (lb) lb.classList.add('hidden');
      document.body.style.overflow = '';
    }}

    function navigateLightbox(dir) {{
      if (GALLERY_IMAGES.length === 0) return;
      currentLightboxIdx = (currentLightboxIdx + dir + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightbox();
    }}

    function updateLightbox() {{
      if (GALLERY_IMAGES.length === 0) return;
      const img = document.getElementById('lightbox-img');
      const counter = document.getElementById('lightbox-counter');
      if (img) img.src = GALLERY_IMAGES[currentLightboxIdx];
      if (counter) counter.textContent = `Plate ${{currentLightboxIdx + 1}} of ${{GALLERY_IMAGES.length}}`;
    }}

    function handleLightboxClick(e) {{
      if (e.target.id === 'image-lightbox' || e.target.closest('.relative')) {{
        closeLightbox();
      }}
    }}

    window.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeLightbox();
      if (!document.getElementById('image-lightbox').classList.contains('hidden')) {{
        if (e.key === 'ArrowLeft') navigateLightbox(-1);
        if (e.key === 'ArrowRight') navigateLightbox(1);
      }}
    }});
  </script>
</body>
</html>
"""
    template = template.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS.replace('{JSON_LD_SCHEMA_TAG}', JSON_LD_SCHEMA_TAG))
    template = template.replace('__HEADER__', generate_header(active_nav="works", borderless=True, font_mode="raleway"))
    template = template.replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway"))
    return template

def generate_field_summer_island_page(base_path="../../"):
    summer_island = next((p for p in projects_data if p['id'] == 'summer-island'), None)
    if not summer_island:
        return ""
    
    images = summer_island.get('images', [])
    full_images = [f"{base_path}{img}" for img in images]
    images_json = json.dumps(full_images).replace('</script>', '<\\/script>')

    hero_img = full_images[0] if full_images else ""
    split_1 = full_images[1] if len(full_images) > 1 else hero_img
    split_2 = full_images[2] if len(full_images) > 2 else hero_img
    horiz_1 = full_images[3] if len(full_images) > 3 else hero_img
    horiz_2 = full_images[4] if len(full_images) > 4 else hero_img
    horiz_3 = full_images[5] if len(full_images) > 5 else hero_img
    horiz_4 = full_images[6] if len(full_images) > 6 else hero_img
    pair_1  = full_images[7] if len(full_images) > 7 else hero_img
    pair_2  = full_images[8] if len(full_images) > 8 else hero_img
    master_plate = full_images[9] if len(full_images) > 9 else hero_img

    header_html = generate_header(active_nav="works", borderless=True, font_mode="raleway", base_path=base_path)
    footer_html = generate_footer(borderless=True, bg="#f8f9fa", font_mode="raleway", base_path=base_path)

    standard_url = f"{base_path}project-summer-island.html"
    home_url = f"{base_path}index.html"
    works_url = f"{base_path}index.html#works"
    prev_url = f"{base_path}project-hand-study.html"
    next_url = f"{base_path}project-tent-hill.html"

    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/svg+xml" href="{base_path}assets/official/logo_charcoal.svg">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    if (!window.tailwind) {{
      document.write('<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"><\\/script>');
    }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
  {JSON_LD_SCHEMA_TAG}
  <title>Summer Island Coastal Resort &amp; Villas — Field Architecture Rendition &bull; Karpov Design LLC</title>
  <style>
    .font-raleway {{
      font-family: 'Raleway', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }}
    :root {{
      --field-left-offset: 25vw;
      --field-right-gutter: clamp(32px, 5vw, 64px);
    }}
    @media (max-width: 1023px) {{
      :root {{
        --field-left-offset: clamp(20px, 5vw, 40px);
        --field-right-gutter: clamp(20px, 5vw, 40px);
      }}
    }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #f8f9fa;
      color: #1a1d20;
      overflow-x: hidden;
    }}
    .field-header-container {{
      padding-left: var(--field-left-offset);
      padding-right: var(--field-right-gutter);
      width: 100%;
    }}
    .field-content-rail {{
      padding-left: var(--field-left-offset);
      padding-right: var(--field-right-gutter);
      width: 100%;
    }}
    #header-logo-img {{
      height: 72px;
      width: auto;
      display: block;
    }}
    @media (min-width: 768px) {{
      #header-logo-img {{
        height: 84px;
      }}
    }}
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
    @media (min-width: 1024px) {{
      .field-horizontal-pin {{
        position: sticky;
        top: 0;
        height: 100vh;
        width: 100%;
        overflow: hidden;
      }}
    }}
  </style>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  {header_html}

  <!-- Breadcrumb Navigation with Rendition Switcher -->
  <div class="w-full bg-[#f8f9fa] py-4 border-b border-[#e2e5e8]/60">
    <nav aria-label="Breadcrumb" class="field-content-rail text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65] flex items-center justify-between overflow-x-auto no-scrollbar whitespace-nowrap">
      <div class="flex items-center">
        <a href="{home_url}" class="hover:text-[#1a1d20] transition-colors shrink-0">Home</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <a href="{works_url}" class="hover:text-[#1a1d20] transition-colors shrink-0">Works</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <span class="text-[#1a1d20] font-semibold truncate font-raleway tracking-wider">Summer Island</span>
      </div>
      <div class="ml-auto flex items-center gap-2 pl-4 shrink-0 text-[11px] font-mono">
        <span class="text-[#767676] uppercase tracking-wider hidden sm:inline">Layout:</span>
        <a href="{standard_url}" class="px-2 py-0.5 text-[#595f65] hover:text-[#1a1d20] transition-colors">Standard</a>
        <span class="px-2 py-0.5 text-[#de602e] font-semibold border-b border-[#de602e]">Field Architecture</span>
      </div>
    </nav>
  </div>

  <main>
    <!-- ACT 1: Monumental Full-Bleed Hero Plate -->
    <section class="relative w-full h-[75vh] md:h-[90vh] bg-[#1a1d20] overflow-hidden flex items-end">
      <img src="{hero_img}" alt="Summer Island Coastal Resort" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-black/10"></div>
      <div class="relative z-10 field-content-rail pb-10 md:pb-16 text-white">
        <span class="text-xs font-mono uppercase tracking-[0.3em] text-[#67aec0] block mb-2">01 / Master Territory</span>
        <h1 class="text-3xl sm:text-4xl md:text-6xl font-semibold tracking-tight text-white font-raleway leading-none">
          Summer Island Coastal Resort
        </h1>
      </div>
    </section>

    <!-- ACT 2: Sticky Split Narrative -->
    <section class="w-full bg-[#f8f9fa] py-16 md:py-24">
      <div class="field-content-rail flex flex-col lg:flex-row items-start gap-12 lg:gap-16">
        <div class="w-full lg:w-5/12 lg:sticky lg:top-28 space-y-6">
          <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block">02 / Narrative &bull; Spatial Logic</span>
          <h2 class="text-2xl sm:text-3xl font-semibold tracking-tight text-[#1a1d20] font-raleway">
            A Resilient Tectonic Reef Along the Aegean Shore
          </h2>
          <p class="text-sm sm:text-base text-[#595f65] leading-relaxed">
            {summer_island.get('description', '')}
          </p>
          <div class="pt-6 border-t border-[#e2e5e8] space-y-3 font-mono text-xs text-[#595f65]">
            <div class="flex justify-between py-1 border-b border-[#e2e5e8]/50">
              <span class="text-[#67aec0] uppercase tracking-wider">Typology</span>
              <span class="text-[#1a1d20] font-semibold">{summer_island.get('typology', '')}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-[#e2e5e8]/50">
              <span class="text-[#67aec0] uppercase tracking-wider">Location</span>
              <span class="text-[#1a1d20] font-semibold">{summer_island.get('location', '')}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-[#e2e5e8]/50">
              <span class="text-[#67aec0] uppercase tracking-wider">Year</span>
              <span class="text-[#1a1d20] font-semibold">{summer_island.get('year', '')}</span>
            </div>
          </div>
        </div>

        <div class="w-full lg:w-7/12 space-y-10">
          <div onclick="openLightbox(1)" class="group cursor-pointer bg-white border border-[#e2e5e8] overflow-hidden">
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="{split_1}" alt="Summer Island Plate 2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white border-t border-[#e2e5e8]/60 flex items-center justify-between text-xs font-mono text-[#595f65]">
              <span class="uppercase tracking-wider">Plate 02 &bull; Exterior Villa Envelope</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
            </div>
          </div>
          <div onclick="openLightbox(2)" class="group cursor-pointer bg-white border border-[#e2e5e8] overflow-hidden">
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="{split_2}" alt="Summer Island Plate 3" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white border-t border-[#e2e5e8]/60 flex items-center justify-between text-xs font-mono text-[#595f65]">
              <span class="uppercase tracking-wider">Plate 03 &bull; Shaded Aegean Courtyard</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ACT 3: Horizontal Scroll Filmstrip (250vh Pin) -->
    <section id="field-horizontal-section" class="relative w-full h-[180vh] lg:h-[260vh] bg-[#1a1d20] text-white">
      <div class="field-horizontal-pin flex flex-col justify-between py-8 md:py-12">
        <div class="field-content-rail flex items-center justify-between z-10 shrink-0">
          <div class="flex items-center gap-4">
            <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0]">03 / Tectonic Sequence</span>
            <span class="text-[#595f65] hidden sm:inline">&bull;</span>
            <span class="text-xs font-mono text-white/70 hidden sm:inline">Scroll to Scrub Photographic Plates</span>
          </div>
          <div class="flex items-center gap-3 font-mono text-xs">
            <span id="horizontal-counter" class="text-[#67aec0]">01 / 04</span>
            <div class="w-20 sm:w-28 h-0.5 bg-white/20 overflow-hidden">
              <div id="horizontal-progress" class="h-full bg-[#de602e] transition-all duration-100" style="width: 25%;"></div>
            </div>
          </div>
        </div>

        <div class="w-full overflow-hidden flex-1 flex items-center my-4">
          <div id="horizontal-track" class="flex gap-6 md:gap-10 pl-[var(--field-left-offset)] pr-[var(--field-right-gutter)] transition-transform duration-75 ease-out select-none">
            <div onclick="openLightbox(3)" class="w-[78vw] sm:w-[62vw] lg:w-[48vw] shrink-0 group cursor-pointer bg-black/40 border border-white/10 overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden">
                <img src="{horiz_1}" alt="Plate 04" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              </div>
              <div class="p-4 flex items-center justify-between text-xs font-mono text-white/70">
                <span>04 &bull; Arrival Pavilion</span>
                <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
              </div>
            </div>
            <div onclick="openLightbox(4)" class="w-[78vw] sm:w-[62vw] lg:w-[48vw] shrink-0 group cursor-pointer bg-black/40 border border-white/10 overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden">
                <img src="{horiz_2}" alt="Plate 05" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              </div>
              <div class="p-4 flex items-center justify-between text-xs font-mono text-white/70">
                <span>05 &bull; Infinity Horizon Basin</span>
                <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
              </div>
            </div>
            <div onclick="openLightbox(5)" class="w-[78vw] sm:w-[62vw] lg:w-[48vw] shrink-0 group cursor-pointer bg-black/40 border border-white/10 overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden">
                <img src="{horiz_3}" alt="Plate 06" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              </div>
              <div class="p-4 flex items-center justify-between text-xs font-mono text-white/70">
                <span>06 &bull; Coastal Villa Terraces</span>
                <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
              </div>
            </div>
            <div onclick="openLightbox(6)" class="w-[78vw] sm:w-[62vw] lg:w-[48vw] shrink-0 group cursor-pointer bg-black/40 border border-white/10 overflow-hidden">
              <div class="relative w-full aspect-[16/10] overflow-hidden">
                <img src="{horiz_4}" alt="Plate 07" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              </div>
              <div class="p-4 flex items-center justify-between text-xs font-mono text-white/70">
                <span>07 &bull; Shaded Promenade Corridor</span>
                <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
              </div>
            </div>
          </div>
        </div>

        <div class="field-content-rail z-10 text-xs font-mono text-white/50 shrink-0">
          <span>Field Architecture Sequence &bull; Karpov Design LLC</span>
        </div>
      </div>
    </section>

    <!-- ACT 4: Comparative Pair Plates -->
    <section class="w-full bg-[#f8f9fa] py-16 md:py-24">
      <div class="field-content-rail space-y-10">
        <div>
          <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block mb-2">04 / Material Dialogue</span>
          <h2 class="text-2xl sm:text-3xl font-semibold tracking-tight text-[#1a1d20] font-raleway">
            Sunken Courtyards &amp; Shaded Colonnades
          </h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-6 md:gap-x-8 gap-y-6 md:gap-y-7">
          <div onclick="openLightbox(7)" class="group cursor-pointer bg-white border border-[#e2e5e8] overflow-hidden">
            <div class="relative w-full aspect-[16/10] overflow-hidden bg-[#1a1d20]">
              <img src="{pair_1}" alt="Summer Island Plate 8" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white border-t border-[#e2e5e8]/60 flex items-center justify-between text-xs font-mono text-[#595f65]">
              <span>Plate 08 &bull; Perimeter Screen Detail</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
            </div>
          </div>
          <div onclick="openLightbox(8)" class="group cursor-pointer bg-white border border-[#e2e5e8] overflow-hidden">
            <div class="relative w-full aspect-[16/10] overflow-hidden bg-[#1a1d20]">
              <img src="{pair_2}" alt="Summer Island Plate 9" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white border-t border-[#e2e5e8]/60 flex items-center justify-between text-xs font-mono text-[#595f65]">
              <span>Plate 09 &bull; Timber Sunshade Pergola</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Enlarge &rarr;</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ACT 5: Full-Width Master Plate -->
    <section class="relative w-full aspect-[16/9] md:aspect-[21/9] bg-[#1a1d20] overflow-hidden">
      <img src="{master_plate}" alt="Summer Island Master Elevation" class="w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-transparent flex items-end">
        <div class="field-content-rail pb-8 md:pb-12 text-white flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4">
          <div>
            <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] block mb-1">05 / Masterplate</span>
            <h3 class="text-xl sm:text-2xl md:text-3xl font-semibold font-raleway">Complete Coastal Master Plan</h3>
          </div>
          <button onclick="openLightbox(9)" class="px-5 py-2.5 bg-white/20 hover:bg-[#de602e] backdrop-blur-sm text-white text-xs font-mono uppercase tracking-widest transition-colors">
            View Full-Res Master &rarr;
          </button>
        </div>
      </div>
    </section>

    <!-- Project Navigation Bar -->
    <div class="w-full bg-[#f8f9fa] py-8 border-t border-[#e2e5e8]">
      <div class="field-content-rail flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs font-mono uppercase tracking-widest">
        <a href="{prev_url}" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center gap-2">
          &larr; Prev Project: Hand Study
        </a>
        <a href="{next_url}" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center sm:justify-end gap-2 sm:text-right">
          Next Project: Tent Hill &rarr;
        </a>
      </div>
    </div>
  </main>

  <!-- Full-Size Image Lightbox Modal with top-left X close button -->
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/90 backdrop-blur-md hidden flex items-center justify-center p-4 sm:p-6 md:p-10 cursor-pointer" onclick="handleLightboxClick(event)">
    <div class="relative max-w-6xl max-h-[92vh] flex flex-col items-center justify-center cursor-default" onclick="event.stopPropagation()">
      <button onclick="closeLightbox()" class="absolute top-3 left-3 z-30 text-[#67aec0] hover:text-[#de602e] text-2xl md:text-3xl font-bold bg-[#1a1d20]/80 hover:bg-[#1a1d20] w-10 h-10 flex items-center justify-center transition-colors focus:outline-none cursor-pointer" title="Close (Esc)" aria-label="Close popup">✕</button>
      <button onclick="navigateLightbox(-1)" class="absolute left-3 top-1/2 -translate-y-1/2 z-20 text-white/80 hover:text-white text-3xl md:text-4xl p-3 bg-black/40 hover:bg-black/70 transition-colors focus:outline-none" aria-label="Previous image">&lsaquo;</button>
      <button onclick="navigateLightbox(1)" class="absolute right-3 top-1/2 -translate-y-1/2 z-20 text-white/80 hover:text-white text-3xl md:text-4xl p-3 bg-black/40 hover:bg-black/70 transition-colors focus:outline-none" aria-label="Next image">&rsaquo;</button>
      <img id="lightbox-img" src="" alt="Project View" class="max-w-[94vw] max-h-[82vh] object-contain drop-shadow-2xl">
      <div id="lightbox-counter" class="mt-3 text-xs font-mono text-white/70 uppercase tracking-widest">Plate 1 of 10</div>
    </div>
  </div>

  <script>
    const GALLERY_IMAGES = {images_json};
    let currentLightboxIndex = 0;

    function openLightbox(idx) {{
      currentLightboxIndex = idx;
      updateLightboxContent();
      const lb = document.getElementById('image-lightbox');
      if (lb) {{
        lb.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
      }}
    }}

    function closeLightbox() {{
      const lb = document.getElementById('image-lightbox');
      if (lb && !lb.classList.contains('hidden')) {{
        lb.classList.add('hidden');
        document.body.style.overflow = '';
      }}
    }}

    function navigateLightbox(dir) {{
      currentLightboxIndex = (currentLightboxIndex + dir + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightboxContent();
    }}

    function updateLightboxContent() {{
      const img = document.getElementById('lightbox-img');
      const counter = document.getElementById('lightbox-counter');
      if (img && GALLERY_IMAGES[currentLightboxIndex]) {{
        img.src = GALLERY_IMAGES[currentLightboxIndex];
        img.alt = "Summer Island — Plate " + (currentLightboxIndex + 1);
      }}
      if (counter) {{
        counter.textContent = `Plate ${{currentLightboxIndex + 1}} of ${{GALLERY_IMAGES.length}}`;
      }}
    }}

    function handleLightboxClick(e) {{
      if (e.target.closest('#lightbox-img') || e.target.closest('button')) return;
      closeLightbox();
    }}

    window.addEventListener('keydown', (e) => {{
      const lb = document.getElementById('image-lightbox');
      if (lb && !lb.classList.contains('hidden')) {{
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowLeft') navigateLightbox(-1);
        if (e.key === 'ArrowRight') navigateLightbox(1);
      }}
    }});

    // Scroll-Linked Horizontal Scrubbing for Desktop (Field Architecture SKHorizontalScroll)
    function onFieldScroll() {{
      const section = document.getElementById('field-horizontal-section');
      const track = document.getElementById('horizontal-track');
      const bar = document.getElementById('horizontal-progress');
      const counter = document.getElementById('horizontal-counter');
      if (!section || !track) return;
      if (window.innerWidth < 1024) {{
        track.style.transform = '';
        return;
      }}
      const rect = section.getBoundingClientRect();
      const totalScroll = section.offsetHeight - window.innerHeight;
      if (totalScroll <= 0) return;
      
      let progress = -rect.top / totalScroll;
      progress = Math.max(0, Math.min(1, progress));
      
      const maxTranslate = track.scrollWidth - window.innerWidth + 96;
      track.style.transform = `translate3d(-${{progress * maxTranslate}}px, 0, 0)`;
      if (bar) bar.style.width = `${{progress * 100}}%`;
      
      const plateIdx = Math.min(4, Math.floor(progress * 4) + 1);
      if (counter) counter.textContent = `0${{plateIdx}} / 04`;
    }}

    window.addEventListener('scroll', onFieldScroll, {{ passive: true }});
    window.addEventListener('resize', onFieldScroll, {{ passive: true }});
    onFieldScroll();
  </script>

  {footer_html}

</body>
</html>
"""

def main():
    print("Building Version 1 (index.html): Centered Hero Logo, Custom Dropdowns, Option 2 Logo (2px boundary clearance)...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="default"))
    print("Saved index.html")

    print("Building Version 2 (variant.html): Left-Aligned Hero Logo, Native Dropdowns, Option 2 Logo...")
    with open('variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="variant"))
    print("Saved variant.html")

    print("Building Version 3 (variant2.html): Field Architecture Variant 2...")
    with open('variant2.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="variant2"))
    print("Saved variant2.html")

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

    print("Building 21 individual project pages...")
    for idx, p in enumerate(projects_data):
        prev_p = projects_data[(idx - 1 + len(projects_data)) % len(projects_data)]
        next_p = projects_data[(idx + 1) % len(projects_data)]
        fname = f"project-{p['id']}.html"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(generate_project_page(p, prev_p, next_p))
    print(f"Saved {len(projects_data)} individual project pages!")

    print("Building Field Architecture Summer Island Variant at project-summer-island/variant/index.html...")
    os.makedirs('project-summer-island/variant', exist_ok=True)
    with open('project-summer-island/variant/index.html', 'w', encoding='utf-8') as f:
        f.write(generate_field_summer_island_page())
    with open('project-summer-island-variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_field_summer_island_page(base_path=""))
    print("Saved project-summer-island/variant/index.html and project-summer-island-variant.html!")

    print("Site compilation finished successfully.")

if __name__ == '__main__':
    main()
