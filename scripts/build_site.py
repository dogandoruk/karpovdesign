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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
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
    .scroll-fade-right {
      mask-image: linear-gradient(to right, black 88%, transparent 100%);
      -webkit-mask-image: linear-gradient(to right, black 88%, transparent 100%);
    }
  </style>
"""

def generate_header(active_nav="works", borderless=True, is_variant=False):
    works_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "works" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"
    about_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "about" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"
    contact_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "contact" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"

    border_cls = "" if borderless else "border-b border-[#e2e5e8]"
    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    template = """
  <!-- Top Navigation: Logo + Stacked Text on Top Left, Inline Links on Tablet/Desktop, Field Architecture Light Sheet Toggle on Mobile -->
  <header class="w-full bg-[#f8f9fa]/95 backdrop-blur-md __BORDER_CLS__ z-50 sticky top-0 transition-all">
    <div class="__CONTAINER_CLS__ px-5 md:px-12 lg:px-16 flex items-center justify-between min-h-[72px] md:min-h-[84px]">
      
      <!-- Top Left Corner: Logo Monogram + Stacked Typography -->
      <a href="index.html" class="flex items-center gap-3 md:gap-3.5 group">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Monogram" class="h-9 md:h-11 w-auto">
        <div class="flex flex-col text-[11px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20]">
          <span>ALEKSANDRE</span>
          <span>KARPOV</span>
          <span class="text-[9px] tracking-[0.22em] text-[#595f65] font-normal">DESIGN LLC</span>
        </div>
      </a>

      <!-- Tablet & Desktop Navigation Links (>= 768px) -->
      <nav class="hidden md:flex items-center gap-8 text-xs tracking-[0.2em] uppercase">
        <a href="index.html#works" class="__WORKS_CLS__">Works</a>
        <a href="about.html" class="__ABOUT_CLS__">About</a>
        <a href="contact.html" class="__CONTACT_CLS__">Contact</a>
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
        <a href="index.html#works" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors">Works</span>
          <span class="text-xs font-mono text-[#38606a] uppercase tracking-widest">21 Projects &rarr;</span>
        </a>
        <a href="about.html" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors">About</span>
          <span class="text-xs font-mono text-[#38606a] uppercase tracking-widest">Pedigree &amp; BIM &rarr;</span>
        </a>
        <a href="contact.html" onclick="closeMobileMenu()" class="group flex items-baseline justify-between py-1">
          <span class="text-2xl font-semibold tracking-[0.15em] uppercase text-[#1a1d20] group-hover:text-[#de602e] transition-colors">Contact</span>
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
    function toggleMobileMenu() {
      const drawer = document.getElementById('mobile-drawer');
      const label = document.getElementById('mobile-menu-label');
      const l1 = document.getElementById('burger-line-1');
      const l2 = document.getElementById('burger-line-2');
      const l3 = document.getElementById('burger-line-3');
      const btn = document.getElementById('mobile-menu-btn');
      if (!drawer) return;
      const isOpen = !drawer.classList.contains('hidden');
      if (!isOpen) {
        drawer.classList.remove('hidden');
        drawer.classList.add('flex');
        if (label) label.textContent = 'Close';
        if (btn) btn.setAttribute('aria-expanded', 'true');
        if (l1) l1.style.transform = 'translateY(6px) rotate(45deg)';
        if (l2) l2.style.opacity = '0';
        if (l3) l3.style.transform = 'translateY(-6px) rotate(-45deg)';
        document.body.style.overflow = 'hidden';
      } else {
        closeMobileMenu();
      }
    }
    function closeMobileMenu() {
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
    }
  </script>
"""
    return template.replace('__BORDER_CLS__', border_cls)\
                   .replace('__CONTAINER_CLS__', container_cls)\
                   .replace('__WORKS_CLS__', works_cls)\
                   .replace('__ABOUT_CLS__', about_cls)\
                   .replace('__CONTACT_CLS__', contact_cls)

def generate_footer(borderless=True, bg="#f8f9fa", is_variant=False):
    border_cls = "" if borderless else "border-t border-[#e2e5e8]"
    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    return f"""
  <!-- Centered Architectural Footer: Borderless on #f8f9fa -->
  <footer class="w-full bg-[{bg}] {border_cls} py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-center justify-between gap-6 md:gap-8">
      
      <!-- Left: Logo & Studio Identity -->
      <div class="flex items-center gap-4">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Logo" class="h-9 md:h-10 w-auto">
        <div>
          <span class="text-sm font-semibold tracking-[0.2em] uppercase text-[#1a1d20] block">Karpov Design LLC</span>
          <span class="text-xs text-[#595f65] block">Aleksandre Karpov &bull; Charlotte, NC</span>
        </div>
      </div>

      <!-- Right: Links & Copyright -->
      <div class="flex flex-col items-center lg:items-end gap-3 text-xs text-[#595f65]">
        <div class="flex gap-8 tracking-[0.2em] uppercase font-medium">
          <a href="index.html#works" class="hover:text-[#de602e] transition-colors">Works</a>
          <a href="about.html" class="hover:text-[#de602e] transition-colors">About</a>
          <a href="contact.html" class="hover:text-[#de602e] transition-colors">Contact</a>
        </div>
        <span class="font-mono text-[11px] text-[#767676]">&copy; 2026 Karpov Design LLC. All rights reserved.</span>
      </div>

    </div>
  </footer>
"""

def generate_workflow_section(is_variant=False):
    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    return f"""
  <!-- Workflow Section: Conceptual Sketch Image + 2 Lorem Ipsum Paragraphs (Directly Below Hero Banner, Borderless on #f8f9fa) -->
  <section id="workflow" class="w-full bg-[#f8f9fa] pt-12 md:pt-20 pb-10 md:pb-14 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- H2 Header above section -->
        <div class="mb-6 md:mb-8">
          <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Workflow</h2>
        </div>

        <!-- 50/50 Side-by-Side: Conceptual Sketch (Natural 4:3, Click to Enlarge) & 2 Lorem Ipsum Paragraphs -->
        <div class="flex flex-col md:flex-row items-center gap-8 lg:gap-12">
          
          <div onclick="openWorkflowLightbox()" class="group cursor-pointer w-full md:w-1/2 aspect-[4/3] bg-transparent overflow-hidden shrink-0 relative" title="Click to view full size">
            <img src="assets/official/projects/travel-sketches/ak_4.jpg" 
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
  </section>

  <!-- Full-Size Image Lightbox Modal for Workflow Sketch -->
  <div id="workflow-lightbox" class="fixed inset-0 z-50 bg-[#1a1d20]/85 backdrop-blur-md hidden flex items-center justify-center p-4 sm:p-6 md:p-10 cursor-pointer" onclick="closeWorkflowLightbox()">
    <div class="relative max-w-5xl max-h-[90vh] flex items-center justify-center cursor-default" onclick="event.stopPropagation()">
      <!-- Authentic Eyeblue X Button on top-left corner of the container -->
      <button onclick="closeWorkflowLightbox()" class="absolute top-3 left-3 z-30 text-[#67aec0] hover:text-[#de602e] text-2xl md:text-3xl font-bold bg-[#1a1d20]/80 hover:bg-[#1a1d20] w-10 h-10 flex items-center justify-center transition-colors focus:outline-none cursor-pointer" title="Close (Esc)" aria-label="Close popup">✕</button>
      <img src="assets/official/projects/travel-sketches/ak_4.jpg" alt="Conceptual Architectural Sketch — Full View" class="max-w-[94vw] max-h-[85vh] object-contain drop-shadow-2xl">
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

def generate_accolades_section(is_variant=False):
    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    return f"""
  <!-- Accolades Section: Left 25% Pure Negative Space, Unified Borderless 2-Column Layout -->
  <section class="w-full bg-[#f8f9fa] py-14 md:py-20 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- Heading (No extra labels) -->
        <div class="mb-6 md:mb-8">
          <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Competitions & Accolades</h2>
        </div>

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
  </section>
"""

def generate_landing_contact_section(is_variant=False):
    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    return f"""
  <!-- Get in Touch CTA Section at Bottom of Landing Page (Seamless #f8f9fa, Borderless) -->
  <section id="contact-section" class="w-full bg-[#f8f9fa] py-16 md:py-20 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space -->
      <div class="w-full lg:w-3/4 lg:pl-12 flex flex-col sm:flex-row sm:items-center justify-between gap-6 md:gap-8 pt-4">
        <div>
          <h2 class="text-xl md:text-3xl font-semibold tracking-tight text-[#38606a] mb-3">Get in touch</h2>
          <p class="text-sm md:text-base text-[#595f65] max-w-xl leading-relaxed">
            Direct dialogue for architectural commissions, strategic collaborations, and urban consultations.
          </p>
        </div>
        <a href="contact.html" class="inline-flex items-center justify-center w-full sm:w-auto px-10 py-4 bg-[#de602e] hover:bg-[#ad4b24] text-white text-xs font-mono uppercase tracking-[0.2em] font-semibold transition-colors shadow-sm whitespace-nowrap">
          Get in touch &rarr;
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
                <h3 class="touch-default-title text-base md:text-lg font-semibold text-white leading-tight drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)] opacity-0 group-hover:opacity-100 transition-opacity duration-500">${p.title}</h3>
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
    });
  </script>
"""

def generate_landing_page(is_variant=False):
    title_suffix = "Works Archive (Default)" if not is_variant else "Works Archive (Variant)"
    
    # Hero: Centered circles on variant only, zero status pills
    dots_markup = """
    <!-- Circular Pagination Dots (Variant Only) -->
    <div id="hero-dots-container" class="absolute bottom-6 md:bottom-8 left-1/2 -translate-x-1/2 z-20 flex items-center gap-2.5 md:gap-3"></div>
""" if is_variant else ""

    hero_markup = f"""
  <!-- Hero Banner: 5x Enlarged White Vector Line-Art Logo + Multi-Project Slideshow (Click to Pause) -->
  <section class="relative w-full h-[74svh] sm:h-[80svh] md:h-[90dvh] bg-[#1a1d20] overflow-hidden flex items-center justify-center select-none cursor-pointer">
    
    <!-- Slideshow Background Container -->
    <div id="hero-slideshow-container" class="absolute inset-0 w-full h-full">
      <!-- Injected via JS -->
    </div>
    
    <!-- Dark Scrim Veil -->
    <div class="absolute inset-0 bg-black/45 z-5 pointer-events-none"></div>

    <!-- Centerpiece: 5x Enlarged White Vector Line-Art Logo + Aleksandre Karpov (No extra subtitles) -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center px-6 pointer-events-none">
      <img src="assets/official/logo_white.svg" alt="Aleksandre Karpov Logo" class="w-56 sm:w-72 md:w-96 lg:w-[480px] h-auto drop-shadow-2xl">
      <h1 class="text-lg sm:text-xl md:text-2xl lg:text-3xl font-semibold tracking-[0.25em] uppercase text-white mt-5 md:mt-6 drop-shadow-md">
        Aleksandre Karpov
      </h1>
    </div>

    {dots_markup}
  </section>
"""

    if not is_variant:
        filter_bar_markup = """
  <!-- Default Version Typographic Filters: BIG.dk Horizontal Touch Ribbon on Mobile + Borderless Collapsible Secondary Row -->
  <div class="w-full bg-[#f8f9fa] pt-5 md:pt-8 pb-3 md:pb-4 space-y-3 md:space-y-4">
    <!-- Row 1: Typology Open Buttons -->
    <div class="flex items-center gap-6 md:gap-10 text-xs md:text-sm font-mono uppercase tracking-[0.2em] pb-2 overflow-x-auto no-scrollbar scroll-fade-right whitespace-nowrap">
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
      <!-- Left: Typology Open Buttons -->
      <div class="flex items-center gap-6 md:gap-10 text-xs md:text-sm font-mono uppercase tracking-[0.2em] overflow-x-auto no-scrollbar scroll-fade-right whitespace-nowrap pb-1">
        <button onclick="setTypology('all')" id="btn-typ-all" class="filter-typ-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1.5 shrink-0">All</button>
        <button onclick="setTypology('Residential')" id="btn-typ-residential" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Residential</button>
        <button onclick="setTypology('Commercial')" id="btn-typ-commercial" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Commercial</button>
        <button onclick="setTypology('Cultural')" id="btn-typ-cultural" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Cultural</button>
        <button onclick="setTypology('Conceptual')" id="btn-typ-conceptual" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Conceptual</button>
        <button onclick="setTypology('Art')" id="btn-typ-art" class="filter-typ-btn text-[#767676] hover:text-[#1a1d20] pb-1.5 transition-colors shrink-0">Art</button>
      </div>

      <!-- Right: Simplistic No-Background Dropdowns (Recency, Completion, Award) -->
      <div id="secondary-filters-row" class="hidden md:flex flex-wrap items-center gap-6 sm:gap-8 text-xs md:text-sm font-mono uppercase tracking-[0.2em]">
        
        <!-- Recency Dropdown -->
        <div class="relative inline-block">
          <select id="select-recency" onchange="setRecency(this.value)" class="bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors">
            <option value="newest" class="bg-white text-[#1a1d20]">Newest</option>
            <option value="oldest" class="bg-white text-[#1a1d20]">Oldest</option>
          </select>
        </div>

        <!-- Completion Dropdown (Built / Concept) -->
        <div class="relative inline-block">
          <select id="select-completion" onchange="setCompletion(this.value)" class="bg-transparent text-xs md:text-sm font-mono uppercase tracking-[0.2em] text-[#767676] hover:text-[#1a1d20] focus:outline-none cursor-pointer py-1 transition-colors">
            <option value="all" class="bg-white text-[#1a1d20]">All Status</option>
            <option value="built" class="bg-white text-[#1a1d20]">Built</option>
            <option value="concept" class="bg-white text-[#1a1d20]">Concept</option>
          </select>
        </div>

        <!-- Award Dropdown -->
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

    container_cls = "w-full" if is_variant else "max-w-[1920px] mx-auto"
    grid_section = f"""
  <!-- Works Grid Section: 25% Pure Negative Space Desktop + 75% 3-Column Works Grid (Borderless on #f8f9fa) -->
  <section id="works" class="w-full bg-[#f8f9fa] py-12 md:py-16 px-5 md:px-12 lg:px-16">
    <div class="{container_cls} flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Column: 100% PURE EMPTY NEGATIVE SPACE -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Grid Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- Header: PORTFOLIO in Eyeblue + Mobile Borderless Filter & Sort Trigger -->
        <div class="flex items-center justify-between">
          <h2 class="text-lg sm:text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">PORTFOLIO</h2>
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

    </div>
  </section>
"""

    rendered_js = JS_TEMPLATE.replace('__PROJECTS_JSON__', projects_json_str)\
                             .replace('__HERO_SLIDES_JSON__', hero_slides_json_str)\
                             .replace('__IS_VARIANT__', 'true' if is_variant else 'false')

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
               .replace('__HEADER__', generate_header("works", borderless=True, is_variant=is_variant))\
               .replace('__HERO__', hero_markup)\
               .replace('__GRID__', grid_section)\
               .replace('__WORKFLOW__', generate_workflow_section(is_variant=is_variant))\
               .replace('__ACCOLADES__', generate_accolades_section(is_variant=is_variant))\
               .replace('__CONTACT_FORM__', generate_landing_contact_section(is_variant=is_variant))\
               .replace('__FOOTER__', generate_footer(borderless=True, bg="#f8f9fa", is_variant=is_variant))\
               .replace('__MODAL__', generate_interactive_modal())\
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

      <!-- 75% Right Column Content (Pure Typographic, No Box Outlines) -->
      <div class="w-full lg:w-3/4 lg:pl-12 space-y-14 md:space-y-16">
        
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

      <!-- 75% Right Active Column -->
      <div class="w-full lg:w-3/4 lg:pl-12 space-y-14 md:space-y-16">
        
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

      <!-- 75% Right Active Column -->
      <div class="w-full lg:w-3/4 lg:pl-12 space-y-16">
      
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
    <nav aria-label="Breadcrumb" class="breadcrumb-bar max-w-[1920px] mx-auto text-xs md:text-sm font-mono uppercase tracking-widest text-[#595f65] flex items-center overflow-x-auto no-scrollbar whitespace-nowrap">
      <a href="index.html" class="hover:text-[#1a1d20] transition-colors shrink-0">Home</a>
      <span class="mx-2 shrink-0">&bull;</span>
      <a href="index.html#works" class="hover:text-[#1a1d20] transition-colors shrink-0">Works</a>
      <span class="mx-2 shrink-0">&bull;</span>
      <span class="text-[#1a1d20] font-semibold truncate">{p['title']}</span>
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

        <!-- 75% Right Active Column -->
        <div class="w-full lg:w-3/4 lg:pl-12 space-y-12">
          
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

def main():
    print("Building Version 1 (index.html): Default title appears on image on hover, clicks navigate to project pages...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(is_variant=False))
    print("Saved index.html")

    print("Building Version 2 (variant.html): Variant title appears in space below image on hover, clicks open pop-up modal...")
    with open('variant.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(is_variant=True))
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

    print("Building 21 individual project pages...")
    for idx, p in enumerate(projects_data):
        prev_p = projects_data[(idx - 1 + len(projects_data)) % len(projects_data)]
        next_p = projects_data[(idx + 1) % len(projects_data)]
        fname = f"project-{p['id']}.html"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(generate_project_page(p, prev_p, next_p))
    print(f"Saved {len(projects_data)} individual project pages!")

    print("All site pages built successfully with borderless desktop & mobile/tablet renditions!")

if __name__ == '__main__':
    main()
