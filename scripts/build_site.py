import os
import json
from PIL import Image

def load_projects():
    with open('assets/official/projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

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

projects_data = load_projects()
for p in projects_data:
    p['best_hero_image'] = get_best_hero_image(p)
projects_json_str = json.dumps(projects_data).replace('</script>', '<\\/script>')

# Curate distinct high-resolution hero slides (1 per project)
HERO_SLIDES = [
    {
        "id": "seed-retreat",
        "title": "SEED Artists Getaway",
        "image": "assets/official/projects/seed-retreat/seed_2.jpg"
    },
    {
        "id": "izka-tower",
        "title": "İZKA Corporate Headquarters",
        "image": "assets/official/projects/izka-tower/izka_10.jpg"
    },
    {
        "id": "multi-city",
        "title": "Eskişehir Industrial Regeneration",
        "image": "assets/official/projects/multi-city/multi_city_10.jpg"
    },
    {
        "id": "summer-island",
        "title": "Summer Island Coastal Resort",
        "image": "assets/official/projects/summer-island/summer_island_10.jpg"
    },
    {
        "id": "pijp-park",
        "title": "De Pijp Community Center & Park",
        "image": "assets/official/projects/pijp-park/pijp_park_4.jpg"
    },
    {
        "id": "valley-of-life",
        "title": "Beylikdüzü Valley of Life",
        "image": "assets/official/projects/valley-of-life/valey_of_life_1.jpg"
    },
    {
        "id": "life-bridge",
        "title": "Sivas Unity Bridge",
        "image": "assets/official/projects/life-bridge/life_bridge_10.jpg"
    },
    {
        "id": "outside-in",
        "title": "Outside-In Residence",
        "image": "assets/official/projects/outside-in/outside_in_10.jpg"
    },
    {
        "id": "folding-edge",
        "title": "Folding Edge Sky Pavilion",
        "image": "assets/official/projects/folding-edge/folding_edge_11.jpg"
    },
    {
        "id": "community-plaza",
        "title": "Caferağa Community Center",
        "image": "assets/official/projects/community-plaza/community_plaza_2.jpg"
    }
]
hero_slides_json_str = json.dumps(HERO_SLIDES).replace('</script>', '<\\/script>')

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
  <style>
    .font-raleway {
      font-family: 'Raleway', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
  <style>
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
    }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      overflow-x: hidden;
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
    @media (hover: none), (max-width: 1023px) {
      .touch-default-veil {
        background: linear-gradient(to top, rgba(26, 29, 32, 0.72) 0%, rgba(26, 29, 32, 0.22) 45%, rgba(0, 0, 0, 0) 100%) !important;
      }
      .touch-default-overlay {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
      .touch-default-title {
        opacity: 1 !important;
      }
      .touch-variant-title {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
      .variant-title-space {
        min-height: 52px !important;
        padding-top: 10px !important;
        padding-bottom: 12px !important;
      }
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
    if layout_mode == "centered":
        container_cls = "max-w-7xl mx-auto"
    elif is_variant:
        container_cls = "w-full"
    else:
        container_cls = "max-w-[1920px] mx-auto"

    template = f"""
  <!-- Top Navigation: Logo + Stacked Text on Top Left, Inline Links on Tablet/Desktop, Field Architecture Light Sheet Toggle on Mobile -->
  <header class="w-full bg-[#f8f9fa]/95 backdrop-blur-md {border_cls} z-50 sticky top-0 transition-all">
    <div class="{container_cls} px-5 md:px-12 lg:px-16 flex items-center justify-between min-h-[72px] md:min-h-[84px]">
      
      <!-- Top Left Corner: Logo Monogram + Stacked Typography -->
      <a href="{home_url}" class="flex items-center gap-3 md:gap-3.5 group">
        <img src="{logo_src}" alt="KAD Monogram" class="h-9 md:h-11 w-auto">
        <div class="flex flex-col text-[11px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20] {brand_font}">
          <span>ALEKSANDRE</span>
          <span>KARPOV</span>
          <span class="text-[9px] tracking-[0.22em] text-[#595f65] font-normal">DESIGN LLC</span>
        </div>
      </a>

      <!-- Tablet & Desktop Navigation Links (>= 768px) -->
      <nav class="hidden md:flex items-center gap-8 text-xs tracking-[0.2em] uppercase {brand_font}">
        <a href="{works_url}" class="{works_cls}">Works</a>
        <a href="{about_url}" class="{about_cls}">About</a>
        <a href="{contact_url}" class="{contact_cls}">Contact</a>
      </nav>

      <!-- Mobile Navigation Trigger (< 768px) — Field Architecture Style Borderless 'MENU / CLOSE' -->
      <button id="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Menu" aria-expanded="false" class="md:hidden inline-flex items-center gap-2.5 px-2 py-2 -mr-2 text-xs font-mono uppercase tracking-[0.22em] text-[#1a1d20] focus:outline-none">
        <span id="mobile-menu-label" class="font-semibold">Menu</span>
        <div class="w-5 h-3.5 flex flex-col justify-between items-end">
          <span id="burger-line-1" class="w-5 h-[1.5px] bg-[#1a1d20] transition-all duration-300 origin-center"></span>
          <span id="burger-line-2" class="w-3.5 h-[1.5px] bg-[#de602e] transition-all duration-300"></span>
          <span id="burger-line-3" class="w-5 h-[1.5px] bg-[#1a1d20] transition-all duration-300 origin-center"></span>
        </div>
      </button>

    </div>
  </header>

  <!-- Light Borderless Fullscreen Mobile Navigation Sheet (< 768px) -->
  <div id="mobile-drawer" class="fixed inset-0 top-[72px] z-40 bg-[#f8f9fa]/98 backdrop-blur-md text-[#1a1d20] hidden flex-col justify-between p-6 overflow-y-auto md:hidden transition-opacity duration-300">
    <div class="space-y-6 pt-4">
      <div class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold pb-1">
        Navigation
      </div>
      <nav class="flex flex-col space-y-6">
        <a href="{works_url}" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors {brand_font}">Works</span>
          <span class="text-xs font-mono text-[#38606a] uppercase tracking-widest">21 Projects &rarr;</span>
        </a>
        <a href="{about_url}" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors {brand_font}">About</span>
          <span class="text-xs font-mono text-[#38606a] uppercase tracking-widest">Pedigree &amp; BIM &rarr;</span>
        </a>
        <a href="{contact_url}" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors {brand_font}">Contact</span>
          <span class="text-xs font-mono text-[#38606a] uppercase tracking-widest">Inquiries &rarr;</span>
        </a>
      </nav>
    </div>

    <div class="pt-6 mt-8 space-y-2.5 text-xs font-mono">
      <div class="flex items-center justify-between">
        <span class="text-[#67aec0] font-semibold">CHARLOTTE, NC</span>
        <a href="tel:+17048459596" class="text-[#2b4951] hover:text-[#de602e] font-semibold">+1 (704) 845-9596</a>
      </div>
      <div class="flex items-center justify-between">
        <span class="text-[#67aec0] font-semibold">INTERNATIONAL</span>
        <a href="tel:+905385907458" class="text-[#2b4951] hover:text-[#de602e] font-semibold">+90 (538) 590-7458</a>
      </div>
      <div class="text-[#595f65] pt-1">
        contact@karpovdesign.com &bull; Karpov Design LLC
      </div>
    </div>
  </div>
  <script>
    function toggleMobileMenu() {{
      const drawer = document.getElementById('mobile-drawer');
      const label = document.getElementById('mobile-menu-label');
      const l1 = document.getElementById('burger-line-1');
      const l2 = document.getElementById('burger-line-2');
      const l3 = document.getElementById('burger-line-3');
      const btn = document.getElementById('mobile-menu-btn');
      if (!drawer) return;
      const isOpen = !drawer.classList.contains('hidden');
      if (!isOpen) {{
        drawer.classList.remove('hidden');
        drawer.classList.add('flex');
        if (label) label.textContent = 'Close';
        if (btn) btn.setAttribute('aria-expanded', 'true');
        if (l1) l1.style.transform = 'translateY(6px) rotate(45deg)';
        if (l2) l2.style.opacity = '0';
        if (l3) l3.style.transform = 'translateY(-6px) rotate(-45deg)';
        document.body.style.overflow = 'hidden';
      }} else {{
        closeMobileMenu();
      }}
    }}
    function closeMobileMenu() {{
      const drawer = document.getElementById('mobile-drawer');
      const label = document.getElementById('mobile-menu-label');
      const l1 = document.getElementById('burger-line-1');
      const l2 = document.getElementById('burger-line-2');
      const l3 = document.getElementById('burger-line-3');
      const btn = document.getElementById('mobile-menu-btn');
      if (!drawer) return;
      drawer.classList.add('hidden');
      drawer.classList.remove('flex');
      if (label) label.textContent = 'Menu';
      if (btn) btn.setAttribute('aria-expanded', 'false');
      if (l1) l1.style.transform = '';
      if (l2) l2.style.opacity = '1';
      if (l3) l3.style.transform = '';
      document.body.style.overflow = '';
    }}
  </script>
"""
    return template

def generate_footer(borderless=True, bg="#f8f9fa", is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    border_cls = "" if borderless else "border-t border-[#e2e5e8]"
    if layout_mode == "centered":
        container_cls = "max-w-7xl mx-auto"
    elif is_variant:
        container_cls = "w-full"
    else:
        container_cls = "max-w-[1920px] mx-auto"
    brand_font = "font-raleway" if font_mode == "raleway" else ""
    logo_src = f"{base_path}assets/official/logo_charcoal.svg"
    works_url = f"{base_path}index.html#works"
    about_url = f"{base_path}about.html"
    contact_url = f"{base_path}contact.html"

    return f"""
  <!-- Centered Architectural Footer: Borderless on #f8f9fa -->
  <footer class="w-full bg-[{bg}] {border_cls} py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-center justify-between gap-6 md:gap-8">
      
      <!-- Left: Logo & Studio Identity -->
      <div class="flex items-center gap-4">
        <img src="{logo_src}" alt="KAD Logo" class="h-9 md:h-10 w-auto">
        <div>
          <span class="text-sm font-semibold tracking-[0.2em] uppercase text-[#1a1d20] block {brand_font}">Karpov Design LLC</span>
          <span class="text-xs text-[#595f65] block">Aleksandre Karpov &bull; Charlotte, NC</span>
        </div>
      </div>

      <!-- Right: Links & Copyright -->
      <div class="flex flex-col items-center lg:items-end gap-3 text-xs text-[#595f65]">
        <div class="flex gap-8 tracking-[0.2em] uppercase font-medium {brand_font}">
          <a href="{works_url}" class="hover:text-[#de602e] transition-colors">Works</a>
          <a href="{about_url}" class="hover:text-[#de602e] transition-colors">About</a>
          <a href="{contact_url}" class="hover:text-[#de602e] transition-colors">Contact</a>
        </div>
        <span class="font-mono text-[11px] text-[#767676]">&copy; 2026 Karpov Design LLC. All rights reserved.</span>
      </div>

    </div>
  </footer>
"""

def generate_workflow_section(is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    sketch_src = f"{base_path}assets/official/projects/travel-sketches/ak_4.jpg"
    
    if layout_mode == "centered":
        content_markup = f"""
    <div class="max-w-7xl mx-auto">
      <!-- H2 Header above section -->
      <div class="mb-6 md:mb-8">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Workflow</h2>
      </div>

      <!-- 50/50 Side-by-Side: Conceptual Sketch & 2 Lorem Ipsum Paragraphs -->
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
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
          </p>
          <p>
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
          </p>
        </div>
      </div>
    </div>"""
    else:
        container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
        content_markup = f"""
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space with 15% Right Margin (Active width: 60% of page) -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%]">
          <!-- H2 Header above section -->
          <div class="mb-6 md:mb-8">
            <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Workflow</h2>
          </div>

          <!-- 50/50 Side-by-Side: Conceptual Sketch & 2 Lorem Ipsum Paragraphs -->
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
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              </p>
              <p>
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>"""

    return f"""
  <!-- Workflow Section: Conceptual Sketch Image + 2 Lorem Ipsum Paragraphs -->
  <section id="workflow" class="w-full bg-[#f8f9fa] pt-12 md:pt-20 pb-10 md:pb-14 px-5 md:px-12 lg:px-16">
{content_markup}
  </section>

  <!-- Full-Size Image Lightbox Modal for Workflow Sketch -->
  <div id="workflow-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/85 backdrop-blur-md hidden flex items-center justify-center p-4 sm:p-6 md:p-10 cursor-pointer" onclick="closeWorkflowLightbox()">
    <div class="relative max-w-5xl max-h-[90vh] flex items-center justify-center cursor-default" onclick="event.stopPropagation()">
      <button onclick="closeWorkflowLightbox()" class="absolute top-3 left-3 z-30 text-[#67aec0] hover:text-[#de602e] text-2xl md:text-3xl font-bold bg-[#1a1d20]/80 hover:bg-[#1a1d20] w-10 h-10 flex items-center justify-center transition-colors focus:outline-none cursor-pointer" title="Close (Esc)" aria-label="Close popup">✕</button>
      <img src="{sketch_src}" alt="Conceptual Architectural Sketch — Full View" class="max-w-[94vw] max-h-[85vh] object-contain drop-shadow-2xl">
    </div>
  </div>

  <script>
    function openWorkflowLightbox() {{
      const lb = document.getElementById('workflow-lightbox');
      if (lb) {{
        lb.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
      }}
    }}
    function closeWorkflowLightbox() {{
      const lb = document.getElementById('workflow-lightbox');
      if (lb && !lb.classList.contains('hidden')) {{
        lb.classList.add('hidden');
        document.body.style.overflow = '';
      }}
    }}
  </script>
"""

def generate_accolades_section(is_variant=False, layout_mode="default", font_mode="raleway"):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    h3_font = "font-raleway" if font_mode == "raleway" else ""
    
    items_markup = f"""
            <!-- Item 1 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">1st Place Winner &bull; Invited Competition</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1 {h3_font}">Eskişehir Industrial Regeneration (Multi-City)</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">51,000 m² municipal depot adaptive reuse into cultural and tech center.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2015 &bull; Eskişehir, TR</span>
              </div>
            </div>

            <!-- Item 2 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">2nd Place Award &bull; National Competition</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1 {h3_font}">Caferağa Community Center & Plaza</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Civic cultural gathering venue, public library, and tiered urban courtyards.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2016 &bull; Istanbul, TR</span>
              </div>
            </div>

            <!-- Item 3 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">Competition Selection & Finalist</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1 {h3_font}">Sivas Unity Bridge & Cultural Crossing</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Inhabited civic bridge weaving public amphitheatres and active promenade.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2015 &bull; Sivas, TR</span>
              </div>
            </div>

            <!-- Item 4 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">Academic Pedigree & Honors</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1 {h3_font}">UNC Charlotte School of Architecture</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Bachelor of Arts in Architecture. Advanced digital lab fellow, Studio X.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2018–2021 &bull; USA / SE</span>
              </div>
            </div>"""

    if layout_mode == "centered":
        content_markup = f"""
    <div class="max-w-7xl mx-auto">
      <div class="mb-6 md:mb-8">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Competitions & Accolades</h2>
      </div>
      <div class="space-y-8">
{items_markup}
      </div>
    </div>"""
    else:
        container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
        content_markup = f"""
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space with 15% Right Margin Buffer -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%]">
          <!-- Heading -->
          <div class="mb-6 md:mb-8">
            <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">Competitions & Accolades</h2>
          </div>
          <div class="space-y-8">
{items_markup}
          </div>
        </div>
      </div>
    </div>"""

    return f"""
  <!-- Accolades Section -->
  <section class="w-full bg-[#f8f9fa] py-14 md:py-20 px-5 md:px-12 lg:px-16">
{content_markup}
  </section>
"""

def generate_landing_contact_section(is_variant=False, layout_mode="default", font_mode="raleway", base_path=""):
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    contact_url = f"{base_path}contact.html"
    
    if layout_mode == "centered":
        content_markup = f"""
    <div class="max-w-7xl mx-auto">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6 py-10 px-6 sm:px-10 bg-white/70 backdrop-blur-sm border border-[#e2e5e8]">
        <div>
          <span class="text-[10px] font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block mb-1">Direct Commission &bull; Inquiries</span>
          <h2 class="text-xl sm:text-2xl font-semibold tracking-[0.18em] uppercase text-[#1a1d20] {h2_font}">Start a Conversation</h2>
          <p class="text-xs sm:text-sm text-[#595f65] mt-1.5">Bespoke residential & cultural architectural commissions across North Carolina and internationally.</p>
        </div>
        <a href="{contact_url}" class="inline-flex items-center gap-3 px-6 py-3.5 bg-[#1a1d20] hover:bg-[#de602e] text-white text-xs font-mono uppercase tracking-[0.2em] font-medium transition-colors shrink-0 group">
          <span>Get in touch</span>
          <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
        </a>
      </div>
    </div>"""
    else:
        container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
        content_markup = f"""
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      <!-- 25% Left Column: Pure Empty Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Area with 15% Right Buffer (Aligns directly with works grid) -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%]">
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6 py-10 px-6 sm:px-10 bg-white/70 backdrop-blur-sm border border-[#e2e5e8]">
            <div>
              <span class="text-[10px] font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block mb-1">Direct Commission &bull; Inquiries</span>
              <h2 class="text-xl sm:text-2xl font-semibold tracking-[0.18em] uppercase text-[#1a1d20] {h2_font}">Start a Conversation</h2>
              <p class="text-xs sm:text-sm text-[#595f65] mt-1.5">Bespoke residential & cultural architectural commissions across North Carolina and internationally.</p>
            </div>
            <a href="{contact_url}" class="inline-flex items-center gap-3 px-6 py-3.5 bg-[#1a1d20] hover:bg-[#de602e] text-white text-xs font-mono uppercase tracking-[0.2em] font-medium transition-colors shrink-0 group">
              <span>Get in touch</span>
              <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
            </a>
          </div>
        </div>
      </div>
    </div>"""

    return f"""
  <!-- Get in Touch CTA Section at Bottom of Landing Page (Seamless #f8f9fa, Borderless) -->
  <section class="w-full bg-[#f8f9fa] py-16 md:py-24 px-5 md:px-12 lg:px-16">
{content_markup}
  </section>
"""

def generate_interactive_modal():
    return """
  <!-- Project Deep Dive Inspection Modal (Borderless Mobile Bottom Sheet / Tablet Modal) -->
  <div id="project-modal" class="fixed inset-0 z-50 bg-[#1a1d20]/80 backdrop-blur-md hidden flex items-end sm:items-center justify-center p-0 sm:p-4 md:p-8">
    <div class="bg-[#f8f9fa] w-full max-w-6xl max-h-[92svh] flex flex-col overflow-hidden shadow-2xl relative">
      
      <!-- Modal Top Bar (Borderless) -->
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
      const secRow = document.getElementById('secondary-filters-row');
      const chev = document.getElementById('filter-chevron');
      if (chev) chev.style.transform = mobileFiltersOpen ? 'rotate(180deg)' : '';
      if (secRow) {
        if (mobileFiltersOpen) {
          secRow.classList.remove('hidden');
          secRow.classList.add('flex');
        } else {
          secRow.classList.add('hidden');
          secRow.classList.remove('flex');
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
        slideDiv.innerHTML = `<img src="${s.image}" alt="${s.title}" class="w-full h-full object-cover">`;
        container.appendChild(slideDiv);
      });

      // Click anywhere on hero to toggle pause / resume
      container.addEventListener('click', () => {
        isPaused = !isPaused;
      });

      if (IS_VARIANT) {
        initPaginationDots();
      }

      startSlideTimer();
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
      if (IS_VARIANT) {
        updatePaginationDots();
      }
    }

    function initPaginationDots() {
      const dotsContainer = document.getElementById('hero-dots-container');
      if (!dotsContainer) return;
      dotsContainer.innerHTML = '';
      HERO_SLIDES.forEach((s, idx) => {
        const dot = document.createElement('button');
        dot.id = `hero-dot-${idx}`;
        dot.className = `w-2.5 h-2.5 md:w-3 md:h-3 rounded-full border border-white transition-all duration-300 ${idx === 0 ? 'bg-[#de602e] border-[#de602e]' : 'bg-transparent'}`;
        dot.title = s.title;
        dot.onclick = (e) => {
          e.stopPropagation();
          goToSlide(idx);
        };
        dotsContainer.appendChild(dot);
      });
    }

    function updatePaginationDots() {
      HERO_SLIDES.forEach((s, idx) => {
        const dot = document.getElementById(`hero-dot-${idx}`);
        if (dot) {
          dot.className = `w-2.5 h-2.5 md:w-3 md:h-3 rounded-full border border-white transition-all duration-300 ${idx === currentSlide ? 'bg-[#de602e] border-[#de602e]' : 'bg-transparent'}`;
        }
      });
    }

    // --- Works Grid Logic ---
    PROJECTS.forEach((p, idx) => { p._origIndex = idx; });
    let currentTypology = 'all';
    let currentCompletion = 'all';
    let currentRecency = 'newest';
    let currentAward = 'all';
    let currentModalIndex = 0;
    let activeOrderedList = [...PROJECTS];

    function isMatch(p) {
      const matchType = (currentTypology === 'all') || (p.typology.toLowerCase() === currentTypology.toLowerCase());
      const matchCompletion = (currentCompletion === 'all') ||
        (currentCompletion === 'built' && p.status === 'Completion') ||
        (currentCompletion === 'concept' && p.status !== 'Completion');
      const matchAward = (currentAward === 'all') || (p.award === true);
      return matchType && matchCompletion && matchAward;
    }

    function renderCards() {
      const container = document.getElementById('works-grid');
      container.innerHTML = '';

      const hasActiveFilter = (currentTypology !== 'all') || (currentCompletion !== 'all') || (currentAward !== 'all');
      const badge = document.getElementById('active-filter-badge');
      if (badge) {
        if ((currentCompletion !== 'all') || (currentAward !== 'all') || (currentRecency !== 'newest')) {
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
        card.className = 'group cursor-pointer bg-transparent flex flex-col justify-start overflow-hidden';
        card.dataset.projectId = p.id;
        card.dataset.typology = p.typology;
        card.dataset.status = p.status;
        card.dataset.year = p.year;
        card.dataset.award = p.award ? 'true' : 'false';
        card.dataset.isMatch = isMatch(p) ? 'true' : 'false';
        if (!IS_VARIANT) {
          card.onclick = () => { window.location.href = `project-${p.id}.html`; };
        } else {
          card.onclick = () => openModal(p.id);
        }

        if (!IS_VARIANT) {
          // DEFAULT VERSION (index.html): TITLE ON IMAGE ON HOVER (10% DARKENING VEIL) + TOUCH VISIBLE ON MOBILE/TABLET
          card.innerHTML = `
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="${p.primary_image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              
              <!-- Strictly 10% dark veil on hover per user directive; touch gradient on mobile/tablet -->
              <div class="touch-default-veil absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors duration-500 ease-out"></div>
              
              <!-- Title appears ON THE IMAGE when hovered (and always on touch screens) -->
              <div class="touch-default-overlay variant-hover-overlay absolute inset-0 p-5 md:p-6 flex flex-col justify-end opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-500 ease-out">
                <h3 class="touch-default-title text-base md:text-lg font-semibold text-white leading-tight drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)] opacity-0 group-hover:opacity-100 transition-opacity duration-500 __TITLE_FONT_CLS__">${p.title}</h3>
              </div>
            </div>
          `;
        } else {
          // VARIANT VERSION (variant.html): DEDICATED SPACE BELOW IMAGE
          card.innerHTML = `
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="${p.primary_image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <!-- Dedicated space UNDERNEATH image: empty by default on desktop mouse, title appears on hover / touch -->
            <div class="variant-title-space pt-5 pb-6 px-1 min-h-[84px] bg-transparent flex items-start">
              <h3 class="touch-variant-title text-sm md:text-base font-semibold text-[#1a1d20] leading-snug opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-300 ease-out">
                ${p.title}
              </h3>
            </div>
          `;
        }

        container.appendChild(card);
      });
    }

    function setTypology(value) {
      currentTypology = value;
      document.querySelectorAll('.filter-typ-btn').forEach(btn => {
        btn.className = 'filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0';
      });
      const activeBtn = document.getElementById(`btn-typ-${value.toLowerCase()}`);
      if (activeBtn) {
        activeBtn.className = 'filter-typ-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1.5 shrink-0';
      }
      renderCards();
    }
    const setFilter = setTypology;

    function setCompletion(value) {
      currentCompletion = value;
      if (!IS_VARIANT) {
        document.querySelectorAll('.filter-comp-btn').forEach(btn => {
          btn.className = 'filter-comp-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors';
        });
        const activeBtn = document.getElementById(`btn-comp-${value.toLowerCase()}`);
        if (activeBtn) {
          activeBtn.className = 'filter-comp-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1';
        }
      } else {
        const sel = document.getElementById('select-completion');
        if (sel) {
          sel.className = (value !== 'all')
            ? 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold border-b-2 border-[#de602e] focus:outline-none cursor-pointer py-1 transition-colors'
            : 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors';
        }
      }
      renderCards();
    }

    function setRecency(value) {
      currentRecency = value;
      if (!IS_VARIANT) {
        document.querySelectorAll('.filter-rec-btn').forEach(btn => {
          btn.className = 'filter-rec-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors';
        });
        const activeBtn = document.getElementById(`btn-rec-${value.toLowerCase()}`);
        if (activeBtn) {
          activeBtn.className = 'filter-rec-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1';
        }
      } else {
        const sel = document.getElementById('select-recency');
        if (sel) {
          sel.className = (value !== 'newest')
            ? 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold border-b-2 border-[#de602e] focus:outline-none cursor-pointer py-1 transition-colors'
            : 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors';
        }
      }
      renderCards();
    }

    function setAward(value) {
      currentAward = value;
      if (!IS_VARIANT) {
        document.querySelectorAll('.filter-award-btn').forEach(btn => {
          btn.className = 'filter-award-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors';
        });
        const activeBtn = document.getElementById(`btn-award-${value.toLowerCase()}`);
        if (activeBtn) {
          activeBtn.className = 'filter-award-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1';
        }
      } else {
        const sel = document.getElementById('select-award');
        if (sel) {
          sel.className = (value !== 'all')
            ? 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#de602e] font-semibold border-b-2 border-[#de602e] focus:outline-none cursor-pointer py-1 transition-colors'
            : 'bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors';
        }
      }
      renderCards();
    }

    // Modal Interaction
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
      document.getElementById('project-modal').classList.add('hidden');
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
      if (!document.getElementById('project-modal').classList.contains('hidden')) {
        if (e.key === 'ArrowLeft') navigateModal(-1);
        if (e.key === 'ArrowRight') navigateModal(1);
      }
    });

    // Touch-swipe support for modal
    let modalTouchStartX = 0;
    window.addEventListener('DOMContentLoaded', () => {
      initHeroSlideshow();
      renderCards();
      const pm = document.getElementById('project-modal');
      if (pm) {
        pm.addEventListener('touchstart', e => { modalTouchStartX = e.changedTouches[0].screenX; }, { passive: true });
        pm.addEventListener('touchend', e => {
          const diff = e.changedTouches[0].screenX - modalTouchStartX;
          if (Math.abs(diff) > 48) navigateModal(diff < 0 ? 1 : -1);
        }, { passive: true });
      }
      if (window.location.hash.startsWith('#project-')) {
        const slug = window.location.hash.replace('#project-', '');
        openModal(slug);
      }
      initLogoAnimation();
    });

    // High-Fidelity Canvas Spritesheet Player: Plays once from frame 0 to 59 and freezes permanently on the last frame
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
        title_suffix = "Works Archive (Default)"
        font_mode = "raleway"
        layout_mode = "default"
        anim_duration = "4000"
    elif variant_mode == "variant":
        title_suffix = "Works Archive (Variant)"
        font_mode = "inter"
        layout_mode = "variant"
        anim_duration = "2000"
    elif variant_mode == "variant2":
        title_suffix = "Works Archive (Variant 2 — Centered 3-Column)"
        font_mode = "raleway"
        layout_mode = "centered"
        anim_duration = "4000"
    else:
        title_suffix = "Works Archive"
        font_mode = "raleway"
        layout_mode = "default"
        anim_duration = "4000"

    h1_font = "font-raleway" if font_mode == "raleway" else ""
    h2_font = "font-raleway" if font_mode == "raleway" else ""
    title_font_cls = "font-raleway" if font_mode == "raleway" else ""

    # Hero: Centered circles on variant only, zero status pills
    dots_markup = """
    <!-- Circular Pagination Dots (Variant Only) -->
    <div id="hero-dots-container" class="absolute bottom-6 md:bottom-8 left-1/2 -translate-x-1/2 z-20 flex items-center gap-2.5 md:gap-3"></div>
""" if is_variant else ""

    hero_markup = f"""
  <!-- Hero Banner: Animated White Line-Art Logo (Freezes on last frame) + Multi-Project Slideshow (Click to Pause) -->
  <section class="relative w-full h-[74svh] sm:h-[80svh] md:h-[90dvh] bg-[#1a1d20] overflow-hidden flex items-center justify-center select-none cursor-pointer">
    
    <!-- Slideshow Background Container -->
    <div id="hero-slideshow-container" class="absolute inset-0 w-full h-full">
      <!-- Injected via JS -->
    </div>
    
    <!-- Dark Scrim Veil -->
    <div class="absolute inset-0 bg-black/45 z-5 pointer-events-none"></div>

    <!-- Centerpiece: White Line-Art Logo Animation (Monumental 5x Size) + Aleksandre Karpov -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center px-6 pointer-events-none">
      <canvas id="hero-logo-canvas" width="400" height="520" class="w-56 sm:w-72 md:w-96 lg:w-[480px] h-auto drop-shadow-2xl"></canvas>
      <h1 class="text-lg sm:text-xl md:text-2xl lg:text-3xl font-semibold tracking-[0.25em] uppercase text-white mt-5 md:mt-6 drop-shadow-md {h1_font}">
        Aleksandre Karpov
      </h1>
    </div>

    {dots_markup}
  </section>
"""

    if variant_mode in ["default", "variant2"]:
        filter_bar_markup = """
  <!-- Typographic Filters: BIG.dk Horizontal Touch Ribbon on Mobile + Borderless Collapsible Secondary Row (No Fade Mask) -->
  <div class="w-full bg-[#f8f9fa] pt-5 md:pt-8 pb-3 md:pb-4 space-y-3 md:space-y-4">
    <!-- Row 1: Typology Open Buttons -->
    <div class="flex items-center gap-6 md:gap-10 text-xs md:text-sm font-mono uppercase tracking-[0.2em] pb-2 overflow-x-auto no-scrollbar whitespace-nowrap">
      <button onclick="setTypology('all')" id="btn-typ-all" class="filter-typ-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1.5 shrink-0">All</button>
      <button onclick="setTypology('Residential')" id="btn-typ-residential" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Residential</button>
      <button onclick="setTypology('Commercial')" id="btn-typ-commercial" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Commercial</button>
      <button onclick="setTypology('Cultural')" id="btn-typ-cultural" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Cultural</button>
      <button onclick="setTypology('Conceptual')" id="btn-typ-conceptual" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Conceptual</button>
      <button onclick="setTypology('Art')" id="btn-typ-art" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Art</button>
    </div>

    <!-- Row 2: Secondary Filters as Open Buttons Underneath Type Filters -->
    <div id="secondary-filters-row" class="hidden md:flex flex-col sm:flex-row sm:flex-wrap items-start sm:items-center gap-4 sm:gap-10 text-xs md:text-sm font-mono uppercase tracking-[0.2em] pt-1">
      <!-- Completion Group: ALL / BUILT / CONCEPT -->
      <div class="flex items-center gap-4 sm:gap-6">
        <button onclick="setCompletion('all')" id="btn-comp-all" class="filter-comp-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1">All Status</button>
        <button onclick="setCompletion('built')" id="btn-comp-built" class="filter-comp-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Built</button>
        <button onclick="setCompletion('concept')" id="btn-comp-concept" class="filter-comp-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Concept</button>
      </div>

      <span class="text-[#cbd5e1] font-light hidden sm:inline">&bull;</span>

      <!-- Recency Group: NEWEST / OLDEST -->
      <div class="flex items-center gap-4 sm:gap-6">
        <button onclick="setRecency('newest')" id="btn-rec-newest" class="filter-rec-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1">Newest</button>
        <button onclick="setRecency('oldest')" id="btn-rec-oldest" class="filter-rec-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Oldest</button>
      </div>

      <span class="text-[#cbd5e1] font-light hidden sm:inline">&bull;</span>

      <!-- Award Group: ALL / AWARDED -->
      <div class="flex items-center gap-4 sm:gap-6">
        <button onclick="setAward('all')" id="btn-award-all" class="filter-award-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1">All Works</button>
        <button onclick="setAward('awarded')" id="btn-award-awarded" class="filter-award-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Awarded</button>
      </div>
    </div>
  </div>
"""
    else:
        filter_bar_markup = """
  <!-- Variant Version Typographic Filters: Type Row + Right-Aligned Simplistic Dropdowns -->
  <div class="w-full bg-[#f8f9fa] pt-5 md:pt-8 pb-3 md:pb-4">
    <div class="flex flex-col xl:flex-row xl:items-center justify-between gap-4 md:gap-6 pb-2">
      <!-- Left: Typology Open Buttons (No Fade Mask) -->
      <div class="flex items-center gap-6 md:gap-10 text-xs md:text-sm font-mono uppercase tracking-[0.2em] overflow-x-auto no-scrollbar whitespace-nowrap pb-1">
        <button onclick="setTypology('all')" id="btn-typ-all" class="filter-typ-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1.5 shrink-0">All</button>
        <button onclick="setTypology('Residential')" id="btn-typ-residential" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Residential</button>
        <button onclick="setTypology('Commercial')" id="btn-typ-commercial" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Commercial</button>
        <button onclick="setTypology('Cultural')" id="btn-typ-cultural" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Cultural</button>
        <button onclick="setTypology('Conceptual')" id="btn-typ-conceptual" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Conceptual</button>
        <button onclick="setTypology('Art')" id="btn-typ-art" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Art</button>
      </div>

      <!-- Right: Simplistic No-Background Dropdowns (Recency, Completion, Award) -->
      <div id="secondary-filters-row" class="hidden md:flex flex-wrap items-center gap-6 sm:gap-8 text-xs md:text-sm font-mono uppercase tracking-[0.2em]">
        <div class="relative inline-block">
          <select id="select-recency" onchange="setRecency(this.value)" class="bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors">
            <option value="newest" class="bg-white text-[#1a1d20]">Newest</option>
            <option value="oldest" class="bg-white text-[#1a1d20]">Oldest</option>
          </select>
        </div>

        <div class="relative inline-block">
          <select id="select-completion" onchange="setCompletion(this.value)" class="bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors">
            <option value="all" class="bg-white text-[#1a1d20]">All Status</option>
            <option value="built" class="bg-white text-[#1a1d20]">Built</option>
            <option value="concept" class="bg-white text-[#1a1d20]">Concept</option>
          </select>
        </div>

        <div class="relative inline-block">
          <select id="select-award" onchange="setAward(this.value)" class="bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors">
            <option value="all" class="bg-white text-[#1a1d20]">All Works</option>
            <option value="awarded" class="bg-white text-[#1a1d20]">Awarded</option>
          </select>
        </div>
      </div>
    </div>
  </div>
"""

    if layout_mode == "centered":
        grid_section = f"""
  <!-- Works Grid Section: Centered 3-Column Grid (Borderless on #f8f9fa) -->
  <section id="works" class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="max-w-7xl mx-auto">
      
      <!-- Header: PORTFOLIO in Eyeblue + Mobile Borderless Filter & Sort Trigger -->
      <div class="flex items-center justify-between">
        <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">PORTFOLIO</h2>
        <button id="mobile-filter-toggle" onclick="toggleMobileFilters()" class="md:hidden inline-flex items-center gap-2 py-1 text-xs font-mono uppercase tracking-[0.18em] text-[#38606a] hover:text-[#de602e] transition-colors">
          <span>Filter &amp; Sort</span>
          <span id="active-filter-badge" class="w-2 h-2 rounded-full bg-[#de602e] hidden"></span>
          <svg id="filter-chevron" class="w-3.5 h-3.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
        </button>
      </div>

      {filter_bar_markup}

      <!-- Generous Spacing between cards (gap-6 md:gap-8 lg:gap-10) -->
      <div id="works-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 lg:gap-10 mt-6 md:mt-10">
        <!-- Dynamically Rendered Cards -->
      </div>

    </div>
  </section>
"""
    else:
        container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
        grid_section = f"""
  <!-- Works Grid Section: 25% Pure Negative Space Desktop + 75% 3-Column Works Grid (Borderless on #f8f9fa) -->
  <section id="works" class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Column: 100% PURE EMPTY NEGATIVE SPACE -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Grid Space with 15% Right Margin Buffer (Active corridor: 60% of page) -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%]">
          
          <!-- Header: PORTFOLIO in Eyeblue + Mobile Borderless Filter & Sort Trigger -->
          <div class="flex items-center justify-between">
            <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a] {h2_font}">PORTFOLIO</h2>
            <button id="mobile-filter-toggle" onclick="toggleMobileFilters()" class="md:hidden inline-flex items-center gap-2 py-1 text-xs font-mono uppercase tracking-[0.18em] text-[#38606a] hover:text-[#de602e] transition-colors">
              <span>Filter &amp; Sort</span>
              <span id="active-filter-badge" class="w-2 h-2 rounded-full bg-[#de602e] hidden"></span>
              <svg id="filter-chevron" class="w-3.5 h-3.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </button>
          </div>

          {filter_bar_markup}

          <!-- Generous Spacing between cards (gap-6 md:gap-8 lg:gap-10) -->
          <div id="works-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 lg:gap-10 mt-6 md:mt-10">
            <!-- Dynamically Rendered Cards -->
          </div>

        </div>
      </div>

    </div>
  </section>
"""

    rendered_js = JS_TEMPLATE.replace('__PROJECTS_JSON__', projects_json_str)\
                             .replace('__HERO_SLIDES_JSON__', hero_slides_json_str)\
                             .replace('__IS_VARIANT__', 'true' if is_variant else 'false')\
                             .replace('__ANIM_DURATION__', anim_duration)\
                             .replace('__TITLE_FONT_CLS__', title_font_cls)

    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Aleksandre Karpov — __TITLE_SUFFIX__</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  __HEADER__

  <main>
    __HERO__
    __WORKFLOW__
    __GRID__
    __ACCOLADES__
    __CONTACT_FORM__
  </main>

  __FOOTER__
  __MODAL__
  __SCRIPT__

</body>
</html>
"""
    return page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
               .replace('__TITLE_SUFFIX__', title_suffix)\
               .replace('__HEADER__', generate_header("works", borderless=True, is_variant=is_variant, layout_mode=layout_mode, font_mode=font_mode))\
               .replace('__HERO__', hero_markup)\
               .replace('__GRID__', grid_section)\
               .replace('__WORKFLOW__', generate_workflow_section(is_variant=is_variant, layout_mode=layout_mode, font_mode=font_mode))\
               .replace('__ACCOLADES__', generate_accolades_section(is_variant=is_variant, layout_mode=layout_mode, font_mode=font_mode))\
               .replace('__CONTACT_FORM__', generate_landing_contact_section(is_variant=is_variant, layout_mode=layout_mode, font_mode=font_mode))\
               .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", is_variant=is_variant, layout_mode=layout_mode, font_mode=font_mode))\
               .replace('__MODAL__', generate_interactive_modal() if is_variant else '')\
               .replace('__SCRIPT__', rendered_js)
def generate_about_page():
    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Aleksandre Karpov — About & Pedigree &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  __HEADER__

  <!-- Breadcrumb Navigation (Seamless, No Borders) -->
  <div class="w-full bg-[#f8f9fa] py-4 px-5 md:px-12 lg:px-16">
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-[1920px] mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20] transition-colors">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">About</span>
    </nav>
  </div>

  <main class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Empty Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Right Column Content (Pure Typographic, No Box Outlines) with 15% Right Margin Buffer -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%] space-y-14 md:space-y-16">
        
        <!-- Header: Aleksandre Karpov + Subtitle (Degree & Universities, Eyeblue Soft accent) -->
        <div>
          <h1 class="text-3xl md:text-5xl font-semibold tracking-tight text-[#1a1d20]">Aleksandre Karpov</h1>
          <p class="text-xs font-mono uppercase tracking-wider text-[#67aec0] font-semibold mt-3">
            B.A. in Architecture &bull; Lund University (Sweden)
          </p>
        </div>

        <!-- Profile Section: Compact Mobile Portrait (w-56 sm:w-64) + Larger Tablet/Desktop Portrait (md:w-80 lg:w-96) + Biography -->
        <div class="flex flex-col md:flex-row items-start gap-8 md:gap-10 lg:gap-14">
          
          <div class="w-56 sm:w-64 md:w-80 lg:w-96 shrink-0 flex flex-col">
            <div class="w-full aspect-[4/5] bg-transparent overflow-hidden">
              <img src="assets/official/alex_portrait.png" alt="Aleksandre Karpov" class="w-full h-full object-cover">
            </div>
            <!-- Caption directly on canvas, zero border, zero white card -->
            <div class="mt-4">
              <span class="text-sm font-semibold tracking-wider uppercase text-[#1a1d20] block">Aleksandre Karpov</span>
              <span class="text-xs font-mono text-[#67aec0] uppercase tracking-widest block mt-1">Principal &bull; Karpov Design LLC</span>
            </div>
          </div>

          <!-- Bio Narrative with H2 in Eyeblue Mid (#38606a) -->
          <div class="flex-1 space-y-6">
            <h2 class="text-xl md:text-3xl font-semibold text-[#38606a] tracking-tight leading-snug">
              Dual Mastery: Analog Fine Art & Computational BIM
            </h2>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              Aleksandre Karpov operates at the convergence of tactile architectural draftsmanship and advanced digital building information modeling. Raised with a rigorous foundation in classical drawing, watercolor plein-air representation, and structural sculpture, he approaches each project with visceral sensitivity to materials, topography, and natural light.
            </p>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              Parallel to this analog mastery, Aleksandre possesses extensive experience in computational building coordination, parametric modeling, and Revit/BIM management. He has led technical documentation across international commercial towers, complex mixed-use industrial regenerations, and bespoke mountain residences.
            </p>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
              As principal of <span class="text-[#2b4951] font-semibold">Karpov Design LLC</span>, he provides complete residential design commissions and architectural consultation.
            </p>
          </div>

        </div>

        <!-- Academic & Technical Capabilities (No white boxes, No borders, Eyeblue Mid headings, Deep Eyeblue highlights) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 pt-4">
          
          <!-- Academic Foundation -->
          <div class="space-y-4">
            <h3 class="text-sm font-mono font-semibold uppercase tracking-[0.2em] text-[#38606a]">Academic Foundation</h3>
            <ul class="space-y-4 text-xs md:text-sm text-[#595f65] leading-relaxed">
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">UNC Charlotte:</strong>
                Bachelor of Arts in Architecture. Recipient of studio merit recognitions.
              </li>
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">Lund University (Sweden):</strong>
                Advanced sustainable urbanism and Nordic housing morphology.
              </li>
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">UNCC Innovative Housing Lab & Studio X:</strong>
                Research fellow prototyping mass-timber structural assemblies.
              </li>
            </ul>
          </div>

          <!-- Software & Technical Stack -->
          <div class="space-y-4">
            <h3 class="text-sm font-mono font-semibold uppercase tracking-[0.2em] text-[#38606a]">Software & Technical Stack</h3>
            <ul class="space-y-4 text-xs md:text-sm text-[#595f65] leading-relaxed">
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">Computational BIM:</strong>
                Autodesk Revit, ArchiCAD, Navisworks clash detection.
              </li>
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">Parametric & Form-Generation:</strong>
                Rhino 3D, Grasshopper, SketchUp Pro.
              </li>
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">Visualization & Media:</strong>
                Enscape, V-Ray, Lumion, Adobe Creative Cloud Suite.
              </li>
              <li>
                <strong class="text-[#2b4951] font-semibold block sm:inline">Analog Methods:</strong>
                Ink drafting, charcoal massing, watercolor rendering.
              </li>
            </ul>
          </div>

        </div>

        <!-- Competitions & Accolades (Borderless presentation on #f8f9fa) -->
        <div class="space-y-8 pt-6">
          <h2 class="text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Competitions & Accolades</h2>
          
          <div class="space-y-8">
            <!-- Item 1 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">1st Place Winner &bull; Invited Competition</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Eskişehir Industrial Regeneration (Multi-City)</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">51,000 m² municipal depot adaptive reuse into cultural and tech center.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2015 &bull; Eskişehir, TR</span>
              </div>
            </div>

            <!-- Item 2 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">2nd Place Award &bull; National Competition</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Caferağa Community Center & Plaza</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Civic cultural gathering venue, public library, and tiered urban courtyards.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2016 &bull; Istanbul, TR</span>
              </div>
            </div>

            <!-- Item 3 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">Competition Selection & Finalist</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Sivas Unity Bridge & Cultural Crossing</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Inhabited civic bridge weaving public amphitheatres and active promenade.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2015 &bull; Sivas, TR</span>
              </div>
            </div>

            <!-- Item 4 -->
            <div class="flex flex-col md:flex-row md:items-baseline justify-between gap-2 md:gap-4">
              <div class="md:w-3/4">
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] font-semibold">Academic Pedigree & Honors</span>
                <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">UNC Charlotte School of Architecture</h3>
                <p class="text-xs text-[#595f65] mt-1 leading-relaxed">Bachelor of Arts in Architecture. Advanced digital lab fellow, Studio X.</p>
              </div>
              <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#2b4951]">
                <span>2018–2021 &bull; USA / SE</span>
              </div>
            </div>

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
    return page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
               .replace('__HEADER__', generate_header("about", borderless=True))\
               .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa"))

def generate_contact_page():
    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Contact & Inquiries &bull; Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  __HEADER__

  <!-- Breadcrumb Navigation (Seamless #f8f9fa, Borderless) -->
  <div class="w-full bg-[#f8f9fa] py-4 px-5 md:px-12 lg:px-16">
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-[1920px] mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20] transition-colors">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">Contact</span>
    </nav>
  </div>

  <main class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Empty Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Right Active Column with 15% Right Margin Buffer -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%] space-y-14 md:space-y-16">
        
        <!-- Contact Header & Direct Coordinates (Eyeblue Mid H1, Eyeblue Soft Labels, Eyeblue Deep Values) -->
        <div class="space-y-8 md:space-y-10">
          <div>
            <h1 class="text-3xl md:text-5xl font-semibold tracking-tight text-[#38606a] mb-4">Get in touch</h1>
            <p class="text-sm md:text-base text-[#595f65] leading-relaxed max-w-2xl">
              For residential design commissions, computational BIM consulting, or competition collaborations, reach out directly.
            </p>
          </div>

          <!-- Direct Coordinates Grid (Borderless, Seamless #f8f9fa) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8 pt-4">
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">United States Direct</span>
              <a href="tel:+17048459596" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                +1 (704) 845-9596
              </a>
              <span class="text-xs text-[#767676] block mt-1">Charlotte, NC</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">International Line</span>
              <a href="tel:+905385907458" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                +90 (538) 590-7458
              </a>
              <span class="text-xs text-[#767676] block mt-1">European Projects</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Electronic Mail</span>
              <a href="mailto:contact@karpovdesign.com" class="text-base font-semibold text-[#2b4951] hover:text-[#de602e] transition-colors mt-1.5 block">
                contact@karpovdesign.com
              </a>
              <span class="text-xs text-[#767676] block mt-1">Direct Studio Inbox</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Studio Location</span>
              <span class="text-base font-semibold text-[#2b4951] mt-1.5 block">Charlotte, NC 28223</span>
              <span class="text-xs text-[#767676] block mt-1">By Appointment Only</span>
            </div>
          </div>
        </div>

        <!-- Form: Borderless wrapper on #f8f9fa, crisp white inputs (Option A), Eyeblue labels, Orange CTA -->
        <form onsubmit="handleInquirySubmit(event)" class="space-y-8 pt-4 max-w-4xl">
          <div>
            <h3 class="text-sm font-mono uppercase tracking-[0.2em] font-semibold text-[#38606a]">Project Inquiries</h3>
          </div>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 md:gap-8">
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Name *</label>
              <input type="text" required placeholder="Your full name" class="w-full bg-white border border-[#e2e5e8] p-3.5 text-xs text-[#1a1d20] focus:outline-none focus:border-[#38606a] transition-colors">
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Email *</label>
              <input type="email" required placeholder="your.email@domain.com" class="w-full bg-white border border-[#e2e5e8] p-3.5 text-xs text-[#1a1d20] focus:outline-none focus:border-[#38606a] transition-colors">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 md:gap-8">
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Site Location</label>
              <input type="text" placeholder="e.g. Asheville, NC / Blue Ridge Mountains" class="w-full bg-white border border-[#e2e5e8] p-3.5 text-xs text-[#1a1d20] focus:outline-none focus:border-[#38606a] transition-colors">
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Telephone</label>
              <input type="tel" placeholder="e.g. +1 (704) 000-0000" class="w-full bg-white border border-[#e2e5e8] p-3.5 text-xs text-[#1a1d20] focus:outline-none focus:border-[#38606a] transition-colors">
            </div>
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-[#2b4951] font-semibold mb-2">Project Scope & Program Requirements *</label>
            <textarea id="contact-scope-textarea" rows="5" required placeholder="Describe your vision, site parameters, approximate square footage, or architectural timeline..." oninput="autoExpandTextarea(this)" class="w-full bg-white border border-[#e2e5e8] p-4 text-xs text-[#1a1d20] focus:outline-none focus:border-[#38606a] resize-none leading-relaxed transition-colors"></textarea>
          </div>

          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-2">
            <span class="text-xs text-[#595f65]">Confidentiality guaranteed. Direct architect response within 24 hours.</span>
            <!-- Orange Submit Button -->
            <button type="submit" class="w-full sm:w-auto px-10 py-4 bg-[#de602e] hover:bg-[#ad4b24] text-white text-xs font-mono uppercase tracking-widest font-semibold transition-colors shadow-sm text-center">
              Submit &rarr;
            </button>
          </div>
          
          <div id="form-success" class="hidden p-4 bg-[#e4f0f2] text-xs text-[#2b4951]">
            Thank you. Your message has been sent directly to Aleksandre Karpov.
          </div>
        </form>

        </div>
      </div>

    </div>
  </main>

  __FOOTER__

  <script>
    function autoExpandTextarea(el) {
      el.style.height = 'auto';
      el.style.height = (el.scrollHeight + 4) + 'px';
    }

    function handleInquirySubmit(e) {
      e.preventDefault();
      document.getElementById('form-success').classList.remove('hidden');
      e.target.reset();
      const ta = document.getElementById('contact-scope-textarea');
      if (ta) ta.style.height = 'auto';
    }
  </script>

</body>
</html>
"""
    return page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
               .replace('__HEADER__', generate_header("contact", borderless=True))\
               .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa"))

def generate_academy_page():
    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Academy & Masterclasses &bull; Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  <!-- Dedicated Header for Academy (Unlinked from Main Nav, Borderless) -->
  <header class="w-full bg-[#f8f9fa]/95 backdrop-blur-md z-50 sticky top-0 transition-all">
    <div class="max-w-[1920px] mx-auto px-5 md:px-12 lg:px-16 flex items-center justify-between min-h-[72px] md:min-h-[84px]">
      <a href="index.html" class="flex items-center gap-3.5">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Logo" class="h-9 md:h-10 w-auto">
        <div class="flex flex-col text-[11px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20]">
          <span>ALEKSANDRE</span>
          <span>KARPOV</span>
          <span class="text-[9px] tracking-[0.22em] text-[#595f65] font-normal">ACADEMY</span>
        </div>
      </a>
      <a href="index.html" class="text-xs font-mono uppercase tracking-widest text-[#595f65] hover:text-[#de602e] transition-colors">
        &larr; Return to Practice
      </a>
    </div>
  </header>

  <!-- Breadcrumb Navigation (Seamless #f8f9fa, Borderless) -->
  <div class="w-full bg-[#f8f9fa] py-4 px-5 md:px-12 lg:px-16">
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-[1920px] mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20] transition-colors">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">Academy (Private Syllabus)</span>
    </nav>
  </div>

  <main class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Empty Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Right Active Column with 15% Right Margin Buffer -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="w-full lg:max-w-[82%] space-y-16">
      
      <!-- Centerpiece Masterclass Player -->
      <div class="bg-transparent">
        <div class="flex flex-col lg:flex-row gap-8 items-start">
          <div class="w-full lg:w-2/3 aspect-video bg-[#1a1d20] relative overflow-hidden">
            <img src="assets/official/projects/izka-tower/izka_10.jpg" alt="Masterclass Video" class="w-full h-full object-cover opacity-70">
            <div class="absolute inset-0 flex items-center justify-center">
              <button onclick="playAcademyDemo()" class="w-16 h-16 bg-white/90 hover:bg-[#de602e] text-[#1a1d20] hover:text-white flex items-center justify-center transition-colors shadow-lg">
                <svg class="w-6 h-6 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </button>
            </div>
          </div>

          <div class="w-full lg:w-1/3 flex flex-col justify-between">
            <div>
              <h2 class="text-xl md:text-2xl font-semibold text-[#38606a] mb-3">Tectonic Synthesis: From Watercolor Intuition to BIM Execution</h2>
              <p class="text-xs md:text-sm text-[#595f65] leading-relaxed mb-4">
                Aleksandre Karpov breaks down the complete workflow of bridging analog artistic gesture with rigorous Revit parametric families, daylight simulation, and constructible documentation.
              </p>
            </div>
            <div class="pt-4">
              <span class="text-xs font-mono text-[#67aec0] block mb-2">Lecturer: Aleksandre Karpov &bull; UNCC Studio Fellow</span>
              <button class="w-full py-3 bg-[#1a1d20] hover:bg-[#de602e] text-white text-xs font-mono uppercase tracking-widest transition-colors font-semibold">
                Access Full Studio Lecture &rarr;
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Video Tutorial Modules -->
      <div>
        <h3 class="text-lg font-semibold uppercase tracking-wider text-[#38606a] mb-6">Technical Video Modules</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-transparent overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden mb-3">
              <img src="assets/official/projects/seed-retreat/seed_8.jpg" alt="Tutorial 1" class="w-full h-full object-cover">
            </div>
            <div>
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-1.5">Mass-Timber Envelope Systems</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Passive ventilation, cross-laminated timber thermal mass, and envelope integration.</p>
            </div>
          </div>

          <div class="bg-transparent overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden mb-3">
              <img src="assets/official/projects/multi-city/multi_city_15.jpg" alt="Tutorial 2" class="w-full h-full object-cover">
            </div>
            <div>
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-1.5">Adaptive Reuse & Structural BIM</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Laser scanning registration, point-cloud integration, and historic masonry rehabilitation.</p>
            </div>
          </div>

          <div class="bg-transparent overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden mb-3">
              <img src="assets/official/projects/travel-sketches/ak_10.jpg" alt="Tutorial 3" class="w-full h-full object-cover">
            </div>
            <div>
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-1.5">Plein-Air Spatial Perception</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Translating atmospheric perspective and wash depth into physical spatial sequences.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Downloadable BIM Resources -->
      <div class="pt-6">
        <h3 class="text-lg font-semibold uppercase tracking-wider text-[#38606a] mb-6">Computational Resources & Templates</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h4 class="text-sm font-semibold text-[#2b4951] mt-0.5">Parametric Louver & Shading Family Pack</h4>
              <span class="text-xs text-[#595f65]">Dynamo + Revit Adaptive Components (.rfa)</span>
            </div>
            <a href="#" class="px-4 py-2.5 bg-[#1a1d20] text-white hover:bg-[#de602e] text-xs font-mono uppercase tracking-wider transition-colors text-center shrink-0">
              Download .ZIP
            </a>
          </div>

          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h4 class="text-sm font-semibold text-[#2b4951] mt-0.5">Architectural Line-Weight & Graphic Standard</h4>
              <span class="text-xs text-[#595f65]">UNCC / Karpov Design Pen Weights & Layouts (.ctb / .pdf)</span>
            </div>
            <a href="#" class="px-4 py-2.5 bg-[#1a1d20] text-white hover:bg-[#de602e] text-xs font-mono uppercase tracking-wider transition-colors text-center shrink-0">
              Download .PDF
            </a>
          </div>
        </div>
      </div>

      </div>
      </div>
    </div>
  </main>

  __FOOTER__

  <script>
    function playAcademyDemo() {
      alert('Masterclass streaming session loaded.');
    }
  </script>

</body>
</html>
"""
    return page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
               .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa"))

def generate_project_page(p, prev_p, next_p):
    best_hero = get_best_hero_image(p)
    status_label = "Built Commission" if p.get('status') == 'Completion' else "Concept / Exploration"
    
    award_markup = ""
    if p.get('award') and p.get('awardText'):
        award_markup = f"""
            <div class="p-4 bg-[#f8f9fa] border-l-2 border-[#de602e]">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">Award / Selection</span>
              <p class="text-xs md:text-sm font-semibold text-[#1a1d20] mt-1">{p['awardText']}</p>
            </div>
"""

    switcher_markup = ""
    if p.get('id') == 'summer-island':
        switcher_markup = """
      <div class="ml-auto flex items-center gap-2 pl-4 shrink-0 text-[11px] font-mono">
        <span class="text-[#767676] uppercase tracking-wider hidden sm:inline">Layout:</span>
        <span class="px-2 py-0.5 text-[#de602e] font-semibold border-b border-[#de602e]">Standard</span>
        <a href="project-summer-island/variant/" class="px-2 py-0.5 text-[#595f65] hover:text-[#1a1d20] transition-colors">Field Architecture &rarr;</a>
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

  <!-- Breadcrumb Navigation (Seamless #f8f9fa, Borderless) -->
  <div class="w-full bg-[#f8f9fa] py-4 px-5 md:px-12 lg:px-16">
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-[1920px] mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65] flex items-center justify-between overflow-x-auto no-scrollbar whitespace-nowrap">
      <div class="flex items-center">
        <a href="index.html" class="hover:text-[#1a1d20] transition-colors shrink-0">Home</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <a href="index.html#works" class="hover:text-[#1a1d20] transition-colors shrink-0">Works</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <span class="text-[#1a1d20] font-semibold truncate">{p['title']}</span>
      </div>
      {switcher_markup}
    </nav>
  </div>

  <main>
    <!-- Dedicated Hero Banner: Highest Resolution Render -->
    <section id="project-hero-banner" class="relative w-full h-[52svh] sm:h-[60vh] md:h-[75vh] bg-[#1a1d20] overflow-hidden flex items-end">
      <img src="{best_hero}" alt="{p['title']}" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-black/20"></div>

      <!-- Hero Title & Key Meta -->
      <div class="relative z-10 max-w-[1920px] mx-auto w-full px-5 md:px-12 lg:px-16 pb-8 md:pb-12 flex flex-col md:flex-row md:items-end justify-between gap-4 md:gap-6">
        <div>
          <h1 class="text-2xl sm:text-3xl md:text-5xl font-semibold tracking-tight text-white drop-shadow-md">{p['title']}</h1>
        </div>
        <div class="text-xs md:text-sm font-mono text-white/90 uppercase tracking-widest">
          <span>{p['location']} &bull; {p['year']}</span>
        </div>
      </div>
    </section>

    <!-- Main Content: Strict 25% Left Pure Negative Space (Borderless on #f8f9fa) -->
    <section class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
      <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
        
        <!-- 25% Left Pure Empty Negative Space -->
        <div class="hidden lg:block lg:w-1/4"></div>

        <!-- 75% Right Active Column with 15% Right Margin Buffer -->
        <div class="w-full lg:w-3/4 lg:pl-12">
          <div class="w-full lg:max-w-[82%] space-y-12">
          
          <!-- Narrative & Brief -->
          <div class="space-y-6 max-w-4xl">
            <div class="pb-2">
              <span class="text-xs font-mono uppercase tracking-[0.25em] text-[#67aec0] font-semibold block mb-3">Project Brief & Spatial Strategy</span>
              <p class="text-sm sm:text-base md:text-lg text-[#1a1d20] leading-relaxed">
                {p['description']}
              </p>
            </div>

            {award_markup}

            <!-- Specifications Table (Eyeblue Soft Labels, Eyeblue Deep Values, Borderless) -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 py-4 text-xs font-mono">
              <div>
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Typology</span>
                <span class="text-sm font-semibold text-[#2b4951] block mt-1 uppercase">{p['typology']}</span>
              </div>
              <div>
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Status</span>
                <span class="text-sm font-semibold text-[#2b4951] block mt-1 uppercase">{status_label}</span>
              </div>
              <div>
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Location</span>
                <span class="text-sm font-semibold text-[#2b4951] block mt-1">{p['location']}</span>
              </div>
              <div>
                <span class="text-[10px] font-mono uppercase tracking-widest text-[#67aec0] font-semibold block">Year</span>
                <span class="text-sm font-semibold text-[#2b4951] block mt-1">{p['year']}</span>
              </div>
            </div>
          </div>

          <!-- Large Images Gallery: Borderless Plates -->
          <div>
            <h2 class="text-lg md:text-xl font-semibold tracking-[0.25em] uppercase text-[#38606a] mb-6 md:mb-8">Visual Documentation & Plates</h2>
            <div id="project-gallery" class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10">
              {gallery_html}
            </div>
          </div>

          <!-- Previous / Next Commission Navigation (Borderless, Stacked on Mobile) -->
          <div class="pt-8 md:pt-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs font-mono uppercase tracking-widest">
            <a href="project-{prev_p['id']}.html" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center gap-2">
              &larr; Prev: {prev_p['title']}
            </a>
            <a href="project-{next_p['id']}.html" class="py-1 text-[#595f65] hover:text-[#de602e] transition-colors flex items-center sm:justify-end gap-2 sm:text-right">
              Next: {next_p['title']} &rarr;
            </a>
          </div>

        </div>
        </div>

      </div>
    </section>
  </main>

  <!-- Near-Fullscreen Image Lightbox Modal (Borderless Controls + Touch Swipe) -->
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/95 backdrop-blur-md hidden flex flex-col items-center justify-between p-4 md:p-6 cursor-pointer select-none" onclick="handleLightboxClick(event)">
    
    <!-- Top Left: Authentic Eyeblue (#67aec0) "X" Button Without Any Borders per user directive -->
    <button onclick="closeLightbox()" class="fixed top-4 left-6 z-60 text-[#67aec0] hover:text-[#de602e] text-3xl font-bold bg-transparent border-none p-2 cursor-pointer transition-colors focus:outline-none" title="Close (Esc)" aria-label="Close popup">✕</button>

    <!-- Top Bar: Counter -->
    <div class="w-full max-w-[1920px] flex items-center justify-end text-white/80 pt-2 pointer-events-none">
      <span id="lightbox-counter" class="text-xs font-mono uppercase tracking-widest bg-[#2b4951]/80 px-3 py-1.5 text-[#e4f0f2]">Plate 1 of {len(images)}</span>
    </div>

    <!-- Center Image Container & Borderless Flank Arrows -->
    <div class="relative w-full flex-1 flex items-center justify-center my-2 select-none">
      <button onclick="navigateLightbox(-1); event.stopPropagation();" class="absolute left-1 md:left-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none" title="Previous (Left Arrow)">&#8592;</button>
      <img id="lightbox-img" src="" alt="Enlarged Project Plate" class="max-w-[94vw] max-h-[82vh] object-contain drop-shadow-2xl transition-all duration-300 cursor-default" onclick="event.stopPropagation()">
      <button onclick="navigateLightbox(1); event.stopPropagation();" class="absolute right-1 md:right-6 z-10 w-10 h-10 md:w-12 md:h-12 text-white bg-[#1a1d20]/70 hover:bg-[#de602e] flex items-center justify-center transition-colors text-lg font-mono focus:outline-none" title="Next (Right Arrow)">&#8594;</button>
    </div>

    <!-- Bottom Caption -->
    <div class="w-full max-w-[1920px] text-center text-xs font-mono uppercase tracking-widest text-white/75 pb-2 pointer-events-none">
      <span>{p['title']} &bull; Visual Documentation</span>
    </div>
  </div>

  <script>
    const GALLERY_IMAGES = {images_json};
    let currentLightboxIndex = 0;

    function openLightbox(idx) {{
      if (!GALLERY_IMAGES || GALLERY_IMAGES.length === 0) return;
      currentLightboxIndex = (idx + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightbox();
      const lb = document.getElementById('image-lightbox');
      lb.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      const lb = document.getElementById('image-lightbox');
      lb.classList.add('hidden');
      document.body.style.overflow = '';
    }}

    function navigateLightbox(direction) {{
      if (!GALLERY_IMAGES || GALLERY_IMAGES.length === 0) return;
      currentLightboxIndex = (currentLightboxIndex + direction + GALLERY_IMAGES.length) % GALLERY_IMAGES.length;
      updateLightbox();
    }}

    function updateLightbox() {{
      const img = document.getElementById('lightbox-img');
      const counter = document.getElementById('lightbox-counter');
      if (img && GALLERY_IMAGES[currentLightboxIndex]) {{
        img.src = GALLERY_IMAGES[currentLightboxIndex];
        img.alt = "{p['title']} — Plate " + (currentLightboxIndex + 1);
      }}
      if (counter) {{
        counter.textContent = `Plate ${{currentLightboxIndex + 1}} of ${{GALLERY_IMAGES.length}}`;
      }}
    }}

    function handleLightboxClick(e) {{
      if (e.target.closest('#lightbox-img') || e.target.closest('button')) {{
        return;
      }}
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

    // Touch-swipe support for lightbox on mobile & tablet
    let lbTouchStartX = 0;
    window.addEventListener('DOMContentLoaded', () => {{
      const lb = document.getElementById('image-lightbox');
      if (lb) {{
        lb.addEventListener('touchstart', (e) => {{
          lbTouchStartX = e.changedTouches[0].screenX;
        }}, {{ passive: true }});
        lb.addEventListener('touchend', (e) => {{
          const diff = e.changedTouches[0].screenX - lbTouchStartX;
          if (Math.abs(diff) > 42) {{
            navigateLightbox(diff < 0 ? 1 : -1);
          }}
        }}, {{ passive: true }});
      }}
    }});
  </script>

__FOOTER__

</body>
</html>
"""
    return template.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
                   .replace('__HEADER__', generate_header("works", borderless=True))\
                   .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa"))

def generate_field_summer_island_page(base_path="../../"):
    summer_island = next((p for p in projects_data if p['id'] == 'summer-island'), None)
    if not summer_island:
        return ""
    
    # 10 curated images
    # 0: summer_island_10.jpg (Hero)
    # 1: summer_island_12.jpg (Split 1)
    # 2: summer_island_13.jpg (Split 2)
    # 3: summer_island_15.jpg (Horiz 1)
    # 4: summer_island_17.jpg (Horiz 2)
    # 5: summer_island_18.jpg (Horiz 3)
    # 6: summer_island_3.jpg  (Horiz 4)
    # 7: summer_island_5.jpg  (Pair 1)
    # 8: summer_island_6.jpg  (Pair 2)
    # 9: summer_island_8.jpg  (Masterplate)
    images = summer_island.get('images', [])
    full_images = [f"{base_path}{img}" for img in images]
    images_json = json.dumps(full_images).replace('</script>', '<\/script>')

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

    header_html = generate_header(active_nav="works", borderless=True, layout_mode="centered", font_mode="raleway", base_path=base_path)
    footer_html = generate_footer(borderless=True, bg="#f8f9fa", layout_mode="centered", font_mode="raleway", base_path=base_path)

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
      document.write('<script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"><\/script>');
    }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
  <title>Summer Island Coastal Resort &amp; Villas — Field Architecture Rendition &bull; Karpov Design LLC</title>
  <style>
    .font-raleway {{
      font-family: 'Raleway', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #f8f9fa;
      color: #1a1d20;
      overflow-x: hidden;
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
  <div class="w-full bg-[#f8f9fa] py-4 px-5 md:px-12 lg:px-16 border-b border-[#e2e5e8]/60">
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-7xl mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65] flex items-center justify-between overflow-x-auto no-scrollbar whitespace-nowrap">
      <div class="flex items-center">
        <a href="{home_url}" class="hover:text-[#1a1d20] transition-colors shrink-0">Home</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <a href="{works_url}" class="hover:text-[#1a1d20] transition-colors shrink-0">Works</a>
        <span class="mx-2 shrink-0">&bull;</span>
        <span class="text-[#1a1d20] font-semibold truncate font-raleway tracking-wider">Summer Island</span>
      </div>
      <div class="ml-auto flex items-center gap-2 pl-4 shrink-0 text-[11px] font-mono">
        <span class="text-[#767676] uppercase tracking-wider hidden sm:inline">Layout:</span>
        <a href="{standard_url}" class="px-2 py-0.5 text-[#595f65] hover:text-[#1a1d20] transition-colors">&larr; Standard</a>
        <span class="px-2 py-0.5 text-[#de602e] font-semibold border-b border-[#de602e]">Field Architecture</span>
      </div>
    </nav>
  </div>

  <main>
    <!-- 1. Cinematic Hero Banner: Full Viewport Cover + Subtle Minimalist Title -->
    <section class="relative w-full h-[80vh] md:h-[90vh] bg-[#1a1d20] overflow-hidden flex items-end">
      <img src="{hero_img}" alt="Summer Island Coastal Resort" class="absolute inset-0 w-full h-full object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/35 to-black/10"></div>
      
      <div class="relative z-10 max-w-7xl mx-auto w-full px-5 md:px-12 lg:px-16 pb-12 md:pb-16 flex flex-col md:flex-row md:items-end justify-between gap-4 md:gap-8">
        <div>
          <span class="text-[10px] md:text-xs font-mono uppercase tracking-[0.3em] text-[#de602e] block mb-2 font-semibold">Residential Resort &bull; Commission</span>
          <h1 class="text-3xl sm:text-5xl md:text-6xl lg:text-7xl font-light tracking-[0.18em] uppercase text-white font-raleway drop-shadow-md">SUMMER ISLAND</h1>
        </div>
        <div class="text-xs md:text-sm font-mono text-white/80 uppercase tracking-[0.25em] flex items-center gap-3">
          <span>Aegean Archipelago</span>
          <span>&bull;</span>
          <span>2018</span>
        </div>
      </div>
    </section>

    <!-- 2. Sticky Split Narrative Section (Field Architecture SKSectionStickySplit replication) -->
    <section class="w-full bg-[#f8f9fa] py-16 md:py-24 px-5 md:px-12 lg:px-16">
      <div class="max-w-7xl mx-auto flex flex-col lg:flex-row items-start gap-12 lg:gap-20">
        
        <!-- Left Column: Sticky on Desktop -->
        <div class="w-full lg:w-5/12 lg:sticky lg:top-28 space-y-6">
          <div class="space-y-2">
            <span class="text-[11px] font-mono uppercase tracking-[0.25em] text-[#de602e] font-semibold block">Design Intent</span>
            <h2 class="text-2xl sm:text-3xl md:text-4xl font-light tracking-[0.15em] uppercase text-[#1a1d20] font-raleway leading-tight">An Organic Dialogue With Aegean Limestone</h2>
          </div>

          <div class="space-y-4 text-sm md:text-base text-[#595f65] leading-relaxed">
            <p>
              Rather than build a fortress against the coastal elements, Summer Island was conceived as an organic incision into the Aegean limestone topography. The villas retreat beneath vegetative green roofs and native earth layers, establishing a respectful dialogue between tectonic permanence and the tidal horizon.
            </p>
            <p>
              Each pavilion is rotated along natural geological contours to harvest prevailing sea breezes while framing unhindered vistas across the archipelago. Subterranean courtyards filter daylight deep into thermal mass living quarters, significantly moderating cooling loads throughout arid summers.
            </p>
          </div>

          <!-- Quick Specifications Matrix -->
          <div class="pt-6 border-t border-[#e2e5e8] grid grid-cols-2 gap-4 text-xs font-mono">
            <div>
              <span class="text-[#67aec0] block font-semibold uppercase tracking-wider">Typology</span>
              <span class="text-[#1a1d20] font-semibold mt-1 block">Subterranean Villas</span>
            </div>
            <div>
              <span class="text-[#67aec0] block font-semibold uppercase tracking-wider">Site Scale</span>
              <span class="text-[#1a1d20] font-semibold mt-1 block">14,500 m&sup2; Cliffline</span>
            </div>
          </div>
        </div>

        <!-- Right Column: Scrolling Architectural Plates -->
        <div class="w-full lg:w-7/12 space-y-10 md:space-y-16">
          <div onclick="openLightbox(1)" class="group cursor-pointer overflow-hidden bg-[#1a1d20] shadow-sm">
            <div class="relative w-full aspect-[4/3] overflow-hidden">
              <img src="{split_1}" alt="Summer Island Cliffside Terrace and Infinity Pool" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white flex justify-between items-center text-[11px] font-mono text-[#595f65] border-t border-[#e2e5e8]">
              <span class="uppercase tracking-widest text-[#2b4951]">Plate 01 &bull; Infinity Terrace &bull; Sea Interface</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Click to Enlarge &rarr;</span>
            </div>
          </div>

          <div onclick="openLightbox(2)" class="group cursor-pointer overflow-hidden bg-[#1a1d20] shadow-sm">
            <div class="relative w-full aspect-[4/3] overflow-hidden">
              <img src="{split_2}" alt="Summer Island Cantilever Shade Pavilion" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white flex justify-between items-center text-[11px] font-mono text-[#595f65] border-t border-[#e2e5e8]">
              <span class="uppercase tracking-widest text-[#2b4951]">Plate 02 &bull; Cantilevered Pergola &bull; Shaded Living</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Click to Enlarge &rarr;</span>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 3. Scroll-Linked Horizontal Photo Scrubbing Track (Field Architecture SKHorizontalScroll replication) -->
    <section id="field-horizontal-section" class="relative w-full bg-[#1a1d20] lg:h-[250vh]">
      <div class="field-horizontal-pin flex flex-col justify-center py-10 lg:py-0">
        
        <!-- Header Info inside pin -->
        <div class="max-w-7xl mx-auto w-full px-5 md:px-12 lg:px-16 mb-4 md:mb-6 flex items-center justify-between text-white/70 text-xs font-mono uppercase tracking-[0.2em]">
          <span class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-[#de602e] animate-pulse"></span>
            <span class="text-white font-semibold">Panoramic Spatial Sequence</span>
          </span>
          <span id="horizontal-counter" class="text-white font-semibold">01 / 04</span>
        </div>

        <!-- The Horizontal Image Track -->
        <div class="w-full overflow-hidden">
          <div id="horizontal-track" class="flex items-center gap-6 md:gap-10 px-5 md:px-12 lg:px-16 w-max overflow-x-auto lg:overflow-visible no-scrollbar snap-x snap-mandatory will-change-transform">
            
            <div onclick="openLightbox(3)" class="snap-center shrink-0 w-[86vw] md:w-[72vw] lg:w-[65vw] max-w-[1080px] aspect-[16/10] bg-black/40 overflow-hidden cursor-pointer group relative shadow-2xl">
              <img src="{horiz_1}" alt="Limestone Cliff Cut Villa" class="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-700 ease-out">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-6 flex items-end justify-between">
                <span class="text-xs font-mono uppercase tracking-widest text-white">Plate 03 &bull; Cliff Excavation &amp; Living Volume</span>
                <span class="text-[10px] font-mono text-[#67aec0] bg-[#1a1d20]/80 px-2.5 py-1">Enlarge</span>
              </div>
            </div>

            <div onclick="openLightbox(4)" class="snap-center shrink-0 w-[86vw] md:w-[72vw] lg:w-[65vw] max-w-[1080px] aspect-[16/10] bg-black/40 overflow-hidden cursor-pointer group relative shadow-2xl">
              <img src="{horiz_2}" alt="Terrace Horizon Integration" class="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-700 ease-out">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-6 flex items-end justify-between">
                <span class="text-xs font-mono uppercase tracking-widest text-white">Plate 04 &bull; Horizon Terrace &amp; Water Basin</span>
                <span class="text-[10px] font-mono text-[#67aec0] bg-[#1a1d20]/80 px-2.5 py-1">Enlarge</span>
              </div>
            </div>

            <div onclick="openLightbox(5)" class="snap-center shrink-0 w-[86vw] md:w-[72vw] lg:w-[65vw] max-w-[1080px] aspect-[16/10] bg-black/40 overflow-hidden cursor-pointer group relative shadow-2xl">
              <img src="{horiz_3}" alt="Subterranean Daylight Courtyard" class="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-700 ease-out">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-6 flex items-end justify-between">
                <span class="text-xs font-mono uppercase tracking-widest text-white">Plate 05 &bull; Subterranean Lightwell Courtyard</span>
                <span class="text-[10px] font-mono text-[#67aec0] bg-[#1a1d20]/80 px-2.5 py-1">Enlarge</span>
              </div>
            </div>

            <div onclick="openLightbox(6)" class="snap-center shrink-0 w-[86vw] md:w-[72vw] lg:w-[65vw] max-w-[1080px] aspect-[16/10] bg-black/40 overflow-hidden cursor-pointer group relative shadow-2xl">
              <img src="{horiz_4}" alt="Tectonic Stone Assembly" class="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-700 ease-out">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity p-6 flex items-end justify-between">
                <span class="text-xs font-mono uppercase tracking-widest text-white">Plate 06 &bull; Tectonic Stone Massing</span>
                <span class="text-[10px] font-mono text-[#67aec0] bg-[#1a1d20]/80 px-2.5 py-1">Enlarge</span>
              </div>
            </div>

          </div>
        </div>

        <!-- Progress Indicator Bar on Desktop -->
        <div class="hidden lg:flex items-center justify-center gap-4 mt-8">
          <div class="w-64 h-[2px] bg-white/20 rounded overflow-hidden">
            <div id="horizontal-progress" class="h-full bg-[#de602e] w-0 transition-all duration-75"></div>
          </div>
          <span class="text-[10px] font-mono uppercase tracking-widest text-white/50">Scroll Down to Pan</span>
        </div>

      </div>
    </section>

    <!-- 4. Monolithic Architectural Pull-Quote in Raleway -->
    <section class="w-full bg-[#f8f9fa] py-20 md:py-32 px-5 md:px-12 lg:px-16">
      <div class="max-w-4xl mx-auto text-center space-y-6 md:space-y-8">
        <span class="text-3xl text-[#de602e] font-serif block">&sect;</span>
        <blockquote class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-light italic leading-snug tracking-wide text-[#1a1d20] font-raleway">
          &ldquo;Rather than imposing form upon the rugged Aegean coastline, the architecture yields to the topography&mdash;dissolving structural boundaries into monolithic stone terraces.&rdquo;
        </blockquote>
        <cite class="block text-xs md:text-sm font-mono uppercase tracking-[0.25em] text-[#38606a] font-semibold not-italic">
          &mdash; Aleksandre Karpov &bull; Principal Architect
        </cite>
      </div>
    </section>

    <!-- 5. Alternating Feature Plates (Paired Detail + Widescreen Masterplate) -->
    <section class="w-full bg-[#f8f9fa] pb-16 md:pb-24 px-5 md:px-12 lg:px-16">
      <div class="max-w-7xl mx-auto space-y-10 md:space-y-16">
        
        <!-- Paired Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
          <div onclick="openLightbox(7)" class="group cursor-pointer overflow-hidden bg-[#1a1d20] shadow-sm">
            <div class="relative w-full aspect-[4/3] overflow-hidden">
              <img src="{pair_1}" alt="Interior spatial daylight transition" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white flex justify-between items-center text-[11px] font-mono text-[#595f65] border-t border-[#e2e5e8]">
              <span class="uppercase tracking-widest text-[#2b4951]">Plate 07 &bull; Materiality &bull; Thermal Mass</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Click to Enlarge &rarr;</span>
            </div>
          </div>

          <div onclick="openLightbox(8)" class="group cursor-pointer overflow-hidden bg-[#1a1d20] shadow-sm">
            <div class="relative w-full aspect-[4/3] overflow-hidden">
              <img src="{pair_2}" alt="Cliffside pool and terrace detail" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700 ease-out">
            </div>
            <div class="p-4 bg-white flex justify-between items-center text-[11px] font-mono text-[#595f65] border-t border-[#e2e5e8]">
              <span class="uppercase tracking-widest text-[#2b4951]">Plate 08 &bull; Pool Terrace &bull; Tidal Elevation</span>
              <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Click to Enlarge &rarr;</span>
            </div>
          </div>
        </div>

        <!-- Full-Bleed Panorama Masterplate -->
        <div onclick="openLightbox(9)" class="group cursor-pointer overflow-hidden bg-[#1a1d20] shadow-lg">
          <div class="relative w-full aspect-[16/9] md:aspect-[21/9] overflow-hidden">
            <img src="{master_plate}" alt="Summer Island Master Architectural Panorama" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-700 ease-out">
          </div>
          <div class="p-4 bg-white flex justify-between items-center text-[11px] font-mono text-[#595f65] border-t border-[#e2e5e8]">
            <span class="uppercase tracking-widest text-[#2b4951]">Plate 09 &bull; Aerial Masterplan &bull; Coastal Integration</span>
            <span class="text-[#67aec0] group-hover:text-[#de602e] transition-colors">Click to Enlarge &rarr;</span>
          </div>
        </div>

      </div>
    </section>

    <!-- 6. Specifications & Credits Matrix -->
    <section class="w-full bg-[#f8f9fa] py-16 px-5 md:px-12 lg:px-16 border-t border-[#e2e5e8]">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 md:gap-10 text-xs font-mono">
          <div>
            <span class="text-[#67aec0] font-semibold block uppercase tracking-widest">Typology</span>
            <p class="text-sm font-semibold text-[#1a1d20] mt-1.5 font-sans">Subterranean Villas &amp; Coastal Resort</p>
          </div>
          <div>
            <span class="text-[#67aec0] font-semibold block uppercase tracking-widest">Location &amp; Site</span>
            <p class="text-sm font-semibold text-[#1a1d20] mt-1.5 font-sans">Aegean Archipelago &bull; 14,500 m&sup2;</p>
          </div>
          <div>
            <span class="text-[#67aec0] font-semibold block uppercase tracking-widest">Status &amp; Year</span>
            <p class="text-sm font-semibold text-[#1a1d20] mt-1.5 font-sans">Conceptual Masterplan &bull; 2018</p>
          </div>
          <div>
            <span class="text-[#67aec0] font-semibold block uppercase tracking-widest">Design Lead</span>
            <p class="text-sm font-semibold text-[#1a1d20] mt-1.5 font-sans">Aleksandre Karpov (Karpov Design LLC)</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. Previous / Next Editorial Pagination -->
    <div class="max-w-7xl mx-auto px-5 md:px-12 lg:px-16 py-12 border-t border-[#e2e5e8] flex items-center justify-between text-xs md:text-sm font-mono uppercase tracking-[0.2em]">
      <a href="{prev_url}" class="group flex items-center gap-3 text-[#595f65] hover:text-[#de602e] transition-colors">
        <span class="group-hover:-translate-x-1 transition-transform">&larr;</span>
        <span class="hidden sm:inline">Previous:</span>
        <span class="font-semibold text-[#1a1d20] group-hover:text-[#de602e]">Hand Study</span>
      </a>
      <a href="{next_url}" class="group flex items-center gap-3 text-[#595f65] hover:text-[#de602e] transition-colors">
        <span class="hidden sm:inline">Next:</span>
        <span class="font-semibold text-[#1a1d20] group-hover:text-[#de602e]">Tent Hill</span>
        <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
      </a>
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
    import os
    print("Building Version 1 (index.html): Default title appears on image on hover, clicks navigate to project pages...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="default"))
    print("Saved index.html")

    print("Building Version 2 (variant.html): Variant title appears in space below image on hover, clicks open pop-up modal...")
    with open('variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(variant_mode="variant"))
    print("Saved variant.html")

    print("Building Version 3 (variant2.html): Centered 3-column layout, Raleway headings, dark-veil hover...")
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
        f.write(generate_field_summer_island_page(base_path="../../"))
    print("Saved project-summer-island/variant/index.html")

    print("Building root convenience mirror project-summer-island-variant.html...")
    with open('project-summer-island-variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_field_summer_island_page(base_path=""))
    print("Saved project-summer-island-variant.html")

    print("All site pages built successfully with borderless desktop & mobile/tablet renditions!")

if __name__ == '__main__':
    main()