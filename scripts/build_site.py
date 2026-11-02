import os
import json

def load_projects():
    with open('assets/official/projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

projects_data = load_projects()
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
    }
    .card-frame {
      border: 1px solid transparent;
      transition: border-color 0.3s ease, transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .card-frame:hover {
      border-color: #1a1d20;
    }
    ::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f3f5;
    }
    ::-webkit-scrollbar-thumb {
      background: #adb5bd;
    }
    @media (hover: none) {
      .variant-hover-overlay {
        opacity: 0.95 !important;
        transform: translateY(0) !important;
        background: linear-gradient(to top, rgba(15, 18, 22, 0.85) 0%, rgba(15, 18, 22, 0.30) 60%, transparent 100%) !important;
      }
      .variant-title-space h3 {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
    }
  </style>
"""

def generate_header(active_nav="works"):
    works_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "works" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"
    about_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "about" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"
    contact_cls = "text-[#1a1d20] font-semibold border-b-2 border-[#de602e] pb-0.5" if active_nav == "contact" else "text-[#595f65] hover:text-[#1a1d20] transition-colors"

    template = """
  <!-- Top Navigation: Logo + Stacked Text on the Top Left Corner per Figma Design -->
  <header class="w-full bg-[#f8f9fa]/95 backdrop-blur-md border-b border-[#e2e5e8] z-50 sticky top-0 transition-all">
    <div class="max-w-[1920px] mx-auto px-6 md:px-12 lg:px-16 flex items-center justify-between min-h-[84px]">
      
      <!-- Top Left Corner: Logo Monogram + Stacked Typography -->
      <a href="index.html" class="flex items-center gap-3.5 group">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Monogram" class="h-10 md:h-11 w-auto">
        <div class="flex flex-col text-[11px] font-semibold tracking-[0.2em] uppercase leading-tight text-[#1a1d20]">
          <span>ALEKSANDRE</span>
          <span>KARPOV</span>
          <span class="text-[9px] tracking-[0.22em] text-[#595f65] font-normal">DESIGN LLC</span>
        </div>
      </a>

      <!-- Top Right: Navigation Links -->
      <nav class="flex items-center gap-8 text-xs tracking-[0.2em] uppercase">
        <a href="index.html#works" class="__WORKS_CLS__">Works</a>
        <a href="about.html" class="__ABOUT_CLS__">About</a>
        <a href="contact.html" class="__CONTACT_CLS__">Contact</a>
      </nav>

    </div>
  </header>
"""
    return template.replace('__WORKS_CLS__', works_cls).replace('__ABOUT_CLS__', about_cls).replace('__CONTACT_CLS__', contact_cls)

def generate_footer():
    return """
  <!-- Centered Architectural Footer: Cleaned of legal blurb -->
  <footer class="w-full bg-[#ffffff] border-t border-[#e2e5e8] py-16 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-center justify-between gap-8">
      
      <!-- Left: Logo & Studio Identity -->
      <div class="flex items-center gap-4">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Logo" class="h-10 w-auto">
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

def generate_workflow_section():
    return """
  <!-- Five-Phase Workflow Section: H2 Left-Aligned within 75% Space, Left 25% Pure Negative Space -->
  <section class="w-full border-b border-[#e2e5e8] bg-[#ffffff] py-16 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- H2 Header above section -->
        <div class="mb-8">
          <h2 class="text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Five-Phase Architectural Workflow</h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
          
          <!-- Phase 1 -->
          <div class="border border-[#e2e5e8] bg-[#f8f9fa] p-4 flex flex-col justify-between group hover:border-[#1a1d20] transition-colors">
            <div class="aspect-[4/3] w-full overflow-hidden bg-[#e9ecef] mb-3">
              <img src="assets/official/projects/hand-study/hand_study02.jpg" alt="Phase 1 Sketch" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">01 / Concept</span>
              <h4 class="text-xs font-semibold uppercase tracking-wider text-[#1a1d20] mt-1">Analog Sketch</h4>
            </div>
          </div>

          <!-- Phase 2 -->
          <div class="border border-[#e2e5e8] bg-[#f8f9fa] p-4 flex flex-col justify-between group hover:border-[#1a1d20] transition-colors">
            <div class="aspect-[4/3] w-full overflow-hidden bg-[#e9ecef] mb-3">
              <img src="assets/official/projects/growing-cell/growingcell_1.jpg" alt="Phase 2 Massing" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">02 / Form</span>
              <h4 class="text-xs font-semibold uppercase tracking-wider text-[#1a1d20] mt-1">Massing Study</h4>
            </div>
          </div>

          <!-- Phase 3 -->
          <div class="border border-[#e2e5e8] bg-[#f8f9fa] p-4 flex flex-col justify-between group hover:border-[#1a1d20] transition-colors">
            <div class="aspect-[4/3] w-full overflow-hidden bg-[#e9ecef] mb-3">
              <img src="assets/official/projects/life-bridge/life_bridge_17.jpg" alt="Phase 3 Technical" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">03 / Precision</span>
              <h4 class="text-xs font-semibold uppercase tracking-wider text-[#1a1d20] mt-1">Technical Plans</h4>
            </div>
          </div>

          <!-- Phase 4 -->
          <div class="border border-[#e2e5e8] bg-[#f8f9fa] p-4 flex flex-col justify-between group hover:border-[#1a1d20] transition-colors">
            <div class="aspect-[4/3] w-full overflow-hidden bg-[#e9ecef] mb-3">
              <img src="assets/official/projects/seed-retreat/seed_2.jpg" alt="Phase 4 BIM 3D" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">04 / Model</span>
              <h4 class="text-xs font-semibold uppercase tracking-wider text-[#1a1d20] mt-1">3D BIM Model</h4>
            </div>
          </div>

          <!-- Phase 5 -->
          <div class="border border-[#e2e5e8] bg-[#f8f9fa] p-4 flex flex-col justify-between group hover:border-[#1a1d20] transition-colors">
            <div class="aspect-[4/3] w-full overflow-hidden bg-[#e9ecef] mb-3">
              <img src="assets/official/projects/izka-tower/izka_10.jpg" alt="Phase 5 Realized" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">05 / Realization</span>
              <h4 class="text-xs font-semibold uppercase tracking-wider text-[#1a1d20] mt-1">Realized Work</h4>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>
"""

def generate_accolades_section():
    return """
  <!-- Accolades Section: Cleaned of 'Recognition' label, Left 25% Pure Negative Space -->
  <section class="w-full border-b border-[#e2e5e8] bg-[#f8f9fa] py-20 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Content Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- Heading (No extra labels) -->
        <div class="mb-8">
          <h2 class="text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Competitions & Accolades</h2>
        </div>

        <div class="divide-y divide-[#e2e5e8] border-t border-b border-[#e2e5e8]">
          
          <!-- Item 1 -->
          <div class="py-6 flex flex-col md:flex-row md:items-baseline justify-between gap-4">
            <div class="md:w-1/2">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">1st Place Winner &bull; Invited Competition</span>
              <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Eskişehir Industrial Regeneration (Multi-City)</h3>
              <p class="text-xs text-[#595f65] mt-1">51,000 m² municipal depot adaptive reuse into cultural and tech center.</p>
            </div>
            <div class="md:w-1/4 text-xs text-[#595f65]">
              <span>Two-Phase International Jury Selection</span>
            </div>
            <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#1a1d20]">
              <span>2015 &bull; Eskişehir, TR</span>
            </div>
          </div>

          <!-- Item 2 -->
          <div class="py-6 flex flex-col md:flex-row md:items-baseline justify-between gap-4">
            <div class="md:w-1/2">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">2nd Place Award &bull; National Competition</span>
              <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Caferağa Community Center & Plaza</h3>
              <p class="text-xs text-[#595f65] mt-1">Civic cultural gathering venue, public library, and tiered urban courtyards.</p>
            </div>
            <div class="md:w-1/4 text-xs text-[#595f65]">
              <span>Kadıköy Municipality Civic Council</span>
            </div>
            <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#1a1d20]">
              <span>2016 &bull; Istanbul, TR</span>
            </div>
          </div>

          <!-- Item 3 -->
          <div class="py-6 flex flex-col md:flex-row md:items-baseline justify-between gap-4">
            <div class="md:w-1/2">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">Competition Selection & Finalist</span>
              <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">Sivas Unity Bridge & Cultural Crossing</h3>
              <p class="text-xs text-[#595f65] mt-1">Inhabited civic bridge weaving public amphitheatres and active promenade.</p>
            </div>
            <div class="md:w-1/4 text-xs text-[#595f65]">
              <span>Sivas Kızılırmak River Commission</span>
            </div>
            <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#1a1d20]">
              <span>2015 &bull; Sivas, TR</span>
            </div>
          </div>

          <!-- Item 4 -->
          <div class="py-6 flex flex-col md:flex-row md:items-baseline justify-between gap-4">
            <div class="md:w-1/2">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">Academic Pedigree & Honors</span>
              <h3 class="text-base md:text-lg font-semibold text-[#1a1d20] mt-1">UNC Charlotte School of Architecture &bull; 3.488 GPA</h3>
              <p class="text-xs text-[#595f65] mt-1">Bachelor of Arts in Architecture. Advanced digital lab fellow, Studio X.</p>
            </div>
            <div class="md:w-1/4 text-xs text-[#595f65]">
              <span>Lund University Architecture Fellowship (Sweden)</span>
            </div>
            <div class="md:w-1/4 text-left md:text-right font-mono text-xs text-[#1a1d20]">
              <span>2018–2021 &bull; USA / SE</span>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>
"""

def generate_landing_contact_section():
    return """
  <!-- Contact Form Section Embedded at Bottom of Landing Page (25% Left Pure Negative Space) -->
  <section id="contact-section" class="w-full bg-[#f8f9fa] py-20 px-6 md:px-12 lg:px-16 border-t border-[#e2e5e8]">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Form Container -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        <div class="mb-8">
          <h2 class="text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">Get in touch</h2>
        </div>

        <form onsubmit="handleInquirySubmit(event)" class="space-y-6 bg-white border border-[#e2e5e8] p-8 md:p-10">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Name *</label>
              <input type="text" required placeholder="Your full name" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Email *</label>
              <input type="email" required placeholder="your.email@domain.com" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Site Location</label>
              <input type="text" placeholder="e.g. Asheville, NC" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
            </div>
            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Telephone</label>
              <input type="tel" placeholder="e.g. +1 (704) 000-0000" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
            </div>
          </div>

          <div>
            <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Project Scope & Program Requirements *</label>
            <textarea id="landing-scope-textarea" rows="5" required placeholder="Describe your vision, site parameters, program requirements..." oninput="autoExpandTextarea(this)" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-4 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e] resize-none leading-relaxed"></textarea>
          </div>

          <div class="flex items-center justify-between pt-2">
            <span class="text-[11px] text-[#595f65]">Confidentiality guaranteed.</span>
            <!-- Orange Submit Button -->
            <button type="submit" class="px-10 py-3 bg-[#de602e] hover:bg-[#ad4b24] text-white text-xs font-mono uppercase tracking-widest font-semibold transition-colors shadow-sm">
              Submit &rarr;
            </button>
          </div>
          
          <div id="form-success" class="hidden p-4 bg-[#e4f0f2] border border-[#38606a] text-xs text-[#2b4951]">
            Thank you. Your message has been sent directly to Aleksandre Karpov.
          </div>
        </form>
      </div>

    </div>
  </section>
"""

def generate_interactive_modal():
    return """
  <!-- Project Deep Dive Inspection Modal -->
  <div id="project-modal" class="fixed inset-0 z-50 bg-[#1a1d20]/80 backdrop-blur-md hidden flex items-center justify-center p-4 md:p-8">
    <div class="bg-[#ffffff] border border-[#1a1d20] w-full max-w-6xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl relative">
      
      <!-- Modal Top Bar -->
      <div class="flex items-center justify-between border-b border-[#e2e5e8] px-6 py-4 bg-[#f8f9fa]">
        <div class="flex items-center gap-3">
          <span id="modal-typology" class="text-[10px] font-mono uppercase tracking-widest px-2 py-0.5 bg-[#1a1d20] text-white">Typology</span>
          <span id="modal-status" class="text-[10px] font-mono uppercase tracking-widest text-[#de602e]">Status</span>
        </div>
        <button onclick="closeModal()" class="text-[#595f65] hover:text-[#1a1d20] transition-colors p-1" title="Close (Esc)">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="flex-1 overflow-y-auto p-6 md:p-8 flex flex-col lg:flex-row gap-8">
        
        <!-- Left: Image Viewer -->
        <div class="w-full lg:w-3/5 flex flex-col gap-4">
          <div class="w-full aspect-[16/10] bg-[#1a1d20] overflow-hidden border border-[#e2e5e8]">
            <img id="modal-main-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'/%3E" alt="Project Image" class="w-full h-full object-cover">
          </div>
          <!-- Thumbnails Strip -->
          <div id="modal-thumbs" class="flex gap-2 overflow-x-auto pb-2"></div>
        </div>

        <!-- Right: Architectural Specification -->
        <div class="w-full lg:w-2/5 flex flex-col justify-between">
          <div>
            <span id="modal-location-year" class="text-xs font-mono text-[#595f65] tracking-wider uppercase block mb-1">Location &bull; Year</span>
            <h2 id="modal-title" class="text-2xl md:text-3xl font-semibold tracking-tight text-[#1a1d20] mb-3">Project Title</h2>
            <div id="modal-award-box" class="p-3 bg-[#f8f9fa] border-l-2 border-[#de602e] mb-4 hidden">
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#de602e] block">Recognition</span>
              <p id="modal-award-text" class="text-xs font-semibold text-[#1a1d20] mt-0.5"></p>
            </div>
            <p id="modal-description" class="text-xs md:text-sm text-[#595f65] leading-relaxed mb-6"></p>
          </div>

          <div class="border-t border-[#e2e5e8] pt-4 mt-auto">
            <div class="flex justify-between items-center">
              <button onclick="navigateModal(-1)" class="text-xs font-mono tracking-wider uppercase text-[#595f65] hover:text-[#1a1d20] transition-colors flex items-center gap-1">
                &larr; Prev Project
              </button>
              <button onclick="navigateModal(1)" class="text-xs font-mono tracking-wider uppercase text-[#595f65] hover:text-[#1a1d20] transition-colors flex items-center gap-1">
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
        dot.className = `w-3 h-3 rounded-full border border-white transition-all duration-300 ${idx === 0 ? 'bg-[#de602e] border-[#de602e]' : 'bg-transparent'}`;
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
          dot.className = `w-3 h-3 rounded-full border border-white transition-all duration-300 ${idx === currentSlide ? 'bg-[#de602e] border-[#de602e]' : 'bg-transparent'}`;
        }
      });
    }

    // --- Works Grid Logic ---
    let currentTypology = 'all';
    let currentModalIndex = 0;
    let activeOrderedList = [...PROJECTS];

    function renderCards() {
      const container = document.getElementById('works-grid');
      container.innerHTML = '';

      const matches = [];
      const nonMatches = [];

      PROJECTS.forEach(p => {
        if (currentTypology === 'all' || p.typology.toLowerCase() === currentTypology.toLowerCase()) {
          matches.push(p);
        } else {
          nonMatches.push(p);
        }
      });

      const hasActiveFilter = (currentTypology !== 'all');
      activeOrderedList = hasActiveFilter ? [...matches, ...nonMatches] : [...matches];

      activeOrderedList.forEach((p, index) => {
        const isMatched = matches.includes(p);
        const card = document.createElement('div');
        
        const dimClass = hasActiveFilter && !isMatched ? 'opacity-40 hover:opacity-100 transition-opacity' : '';
        card.className = `group cursor-pointer bg-white card-frame flex flex-col justify-between overflow-hidden ${dimClass}`;
        card.onclick = () => openModal(p.id);

        if (!IS_VARIANT) {
          // DEFAULT VERSION (index.html): TITLE APPEARS ON IMAGE ON HOVER (NO SPACE UNDERNEATH)
          card.innerHTML = `
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="${p.primary_image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
              
              <!-- Subtle dark veil on hover -->
              <div class="absolute inset-0 bg-black/0 group-hover:bg-black/55 transition-colors duration-500 ease-out"></div>
              
              <!-- Title appears ON THE IMAGE when hovered -->
              <div class="variant-hover-overlay absolute inset-0 p-6 flex flex-col justify-end opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0 transition-all duration-500 ease-out">
                <h3 class="text-base md:text-lg font-semibold text-white leading-tight drop-shadow-sm">${p.title}</h3>
              </div>
            </div>
          `;
        } else {
          // VARIANT VERSION (variant.html): DEDICATED SPACE BELOW IMAGE (EMPTY INITIALLY, TITLE REVEALS IN THAT SPACE ON HOVER)
          card.innerHTML = `
            <div class="relative w-full aspect-[4/3] overflow-hidden bg-[#1a1d20]">
              <img src="${p.primary_image}" alt="${p.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
            </div>
            <!-- Dedicated space UNDERNEATH image: empty by default, title appears on hover -->
            <div class="variant-title-space p-4 min-h-[64px] bg-white border-t border-[#e2e5e8] flex items-center">
              <h3 class="text-sm md:text-base font-semibold text-[#1a1d20] leading-snug opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0 transition-all duration-300">
                ${p.title}
              </h3>
            </div>
          `;
        }

        container.appendChild(card);
      });
    }

    function setFilter(value) {
      currentTypology = value;
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.className = 'filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors';
      });
      const activeBtn = document.getElementById(`btn-typ-${value.toLowerCase()}`);
      if (activeBtn) {
        activeBtn.className = 'filter-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1';
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

      const mainImg = document.getElementById('modal-main-img');
      mainImg.src = p.primary_image;

      const thumbs = document.getElementById('modal-thumbs');
      thumbs.innerHTML = '';
      if (p.images && p.images.length > 0) {
        p.images.forEach(imgUrl => {
          const t = document.createElement('img');
          t.src = imgUrl;
          t.className = 'w-16 h-12 object-cover border border-[#e2e5e8] cursor-pointer hover:border-[#1a1d20] transition-colors shrink-0';
          t.onclick = () => { mainImg.src = imgUrl; };
          thumbs.appendChild(t);
        });
      }
    }

    function autoExpandTextarea(el) {
      el.style.height = 'auto';
      el.style.height = (el.scrollHeight + 4) + 'px';
    }

    function handleInquirySubmit(e) {
      e.preventDefault();
      document.getElementById('form-success').classList.remove('hidden');
      e.target.reset();
      const ta = document.getElementById('landing-scope-textarea');
      if (ta) ta.style.height = 'auto';
    }

    window.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeModal();
      if (!document.getElementById('project-modal').classList.contains('hidden')) {
        if (e.key === 'ArrowLeft') navigateModal(-1);
        if (e.key === 'ArrowRight') navigateModal(1);
      }
    });

    window.addEventListener('DOMContentLoaded', () => {
      initHeroSlideshow();
      renderCards();
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
    <div id="hero-dots-container" class="absolute bottom-8 left-1/2 -translate-x-1/2 z-20 flex items-center gap-3"></div>
""" if is_variant else ""

    hero_markup = f"""
  <!-- Hero Banner: 5x Enlarged White Vector Line-Art Logo + Multi-Project Slideshow (Click to Pause) -->
  <section class="relative w-full h-[85dvh] md:h-[90dvh] bg-[#1a1d20] overflow-hidden flex items-center justify-center select-none cursor-pointer">
    
    <!-- Slideshow Background Container -->
    <div id="hero-slideshow-container" class="absolute inset-0 w-full h-full">
      <!-- Injected via JS -->
    </div>
    
    <!-- Dark Scrim Veil -->
    <div class="absolute inset-0 bg-black/45 z-5 pointer-events-none"></div>

    <!-- Centerpiece: 5x Enlarged White Vector Line-Art Logo + Aleksandre Karpov (No extra subtitles) -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center px-6 pointer-events-none">
      <img src="assets/official/logo_white.svg" alt="Aleksandre Karpov Logo" class="w-64 sm:w-80 md:w-96 lg:w-[480px] h-auto drop-shadow-2xl">
      <h1 class="text-xl md:text-2xl lg:text-3xl font-semibold tracking-[0.25em] uppercase text-white mt-6 drop-shadow-md">
        Aleksandre Karpov
      </h1>
    </div>

    {dots_markup}
  </section>
"""

    # Figma Typographic Filter Bar (Zero Button Borders, Zero Dropdowns, Pure Horizontal Text Tabs)
    filter_bar_markup = """
  <!-- Figma Typographic Filter Bar: Underneath PORTFOLIO, Zero Button Borders -->
  <div class="w-full bg-[#f8f9fa] pt-8 pb-4">
    <div class="flex flex-wrap items-center gap-6 md:gap-10 text-xs font-mono uppercase tracking-[0.2em] border-b border-[#e2e5e8] pb-4">
      <button onclick="setFilter('all')" id="btn-typ-all" class="filter-btn text-[#de602e] font-semibold border-b-2 border-[#de602e] pb-1">All</button>
      <button onclick="setFilter('Residential')" id="btn-typ-residential" class="filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Residential</button>
      <button onclick="setFilter('Commercial')" id="btn-typ-commercial" class="filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Commercial</button>
      <button onclick="setFilter('Cultural')" id="btn-typ-cultural" class="filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Cultural</button>
      <button onclick="setFilter('Conceptual')" id="btn-typ-conceptual" class="filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Conceptual</button>
      <button onclick="setFilter('Art')" id="btn-typ-art" class="filter-btn text-[#767676] hover:text-[#1a1d20] pb-1 transition-colors">Art</button>
    </div>
  </div>
"""

    grid_section = f"""
  <!-- Works Grid Section: 25% Pure Negative Space Desktop + 75% 3-Column Works Grid -->
  <section id="works" class="w-full bg-[#f8f9fa] py-16 px-6 md:px-12 lg:px-16 border-b border-[#e2e5e8]">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Column: 100% PURE EMPTY NEGATIVE SPACE -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Active Grid Space -->
      <div class="w-full lg:w-3/4 lg:pl-12">
        
        <!-- Header is strictly PORTFOLIO in Eyeblue (No 'Selected Works' H2) -->
        <div>
          <h2 class="text-xl md:text-2xl font-semibold tracking-[0.25em] uppercase text-[#38606a]">PORTFOLIO</h2>
        </div>

        {filter_bar_markup}

        <!-- Generous Spacing between cards (gap-8 md:gap-10) -->
        <div id="works-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10 mt-10">
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
    __GRID__
    __WORKFLOW__
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
               .replace('__HEADER__', generate_header("works"))\
               .replace('__HERO__', hero_markup)\
               .replace('__GRID__', grid_section)\
               .replace('__WORKFLOW__', generate_workflow_section())\
               .replace('__ACCOLADES__', generate_accolades_section())\
               .replace('__CONTACT_FORM__', generate_landing_contact_section())\
               .replace('__FOOTER__', generate_footer())\
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

  <!-- Breadcrumb Navigation -->
  <div class="w-full bg-white border-b border-[#e2e5e8] py-3 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto text-xs font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20]">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">About</span>
    </div>
  </div>

  <main class="w-full bg-[#f8f9fa] py-20 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto flex flex-col lg:flex-row items-stretch">
      
      <!-- 25% Left Pure Negative Space -->
      <div class="hidden lg:block lg:w-1/4"></div>

      <!-- 75% Right Column Content -->
      <div class="w-full lg:w-3/4 lg:pl-12 space-y-16">
        
        <!-- Header -->
        <div class="border-b border-[#e2e5e8] pb-6">
          <h1 class="text-3xl md:text-4xl font-semibold tracking-tight text-[#1a1d20]">Aleksandre Karpov</h1>
          <p class="text-xs font-mono text-[#595f65] uppercase tracking-wider mt-2">
            B.A. in Architecture &bull; UNCC 3.488 GPA &bull; Lund University (Sweden)
          </p>
        </div>

        <!-- Bio Narrative -->
        <div class="max-w-3xl">
          <h2 class="text-xl md:text-2xl font-semibold text-[#1a1d20] mb-4">Dual Mastery: Analog Fine Art & Computational BIM</h2>
          <p class="text-sm md:text-base text-[#595f65] leading-relaxed mb-4">
            Aleksandre Karpov operates at the convergence of tactile architectural draftsmanship and advanced digital building information modeling. Raised with a rigorous foundation in classical drawing, watercolor plein-air representation, and structural sculpture, he approaches each project with visceral sensitivity to materials, topography, and natural light.
          </p>
          <p class="text-sm md:text-base text-[#595f65] leading-relaxed mb-4">
            Parallel to this analog mastery, Aleksandre possesses extensive experience in computational building coordination, parametric modeling, and Revit/BIM management. He has led technical documentation across international commercial towers, complex mixed-use industrial regenerations, and bespoke mountain residences.
          </p>
          <p class="text-sm md:text-base text-[#595f65] leading-relaxed">
            As principal of Karpov Design LLC, he provides complete residential design commissions and architectural consultation.
          </p>
        </div>

        <!-- Academic & Technical Capabilities -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 border-t border-[#e2e5e8] pt-12">
          <div class="bg-white border border-[#e2e5e8] p-6 card-frame">
            <h3 class="text-base font-semibold uppercase tracking-wider text-[#1a1d20] mb-3">Academic Foundation</h3>
            <ul class="space-y-3 text-xs md:text-sm text-[#595f65]">
              <li><strong class="text-[#1a1d20]">UNC Charlotte:</strong> Bachelor of Arts in Architecture (3.488 GPA). Recipient of studio merit recognitions.</li>
              <li><strong class="text-[#1a1d20]">Lund University (Sweden):</strong> Advanced sustainable urbanism and Nordic housing morphology.</li>
              <li><strong class="text-[#1a1d20]">UNCC Innovative Housing Lab & Studio X:</strong> Research fellow prototyping mass-timber structural assemblies.</li>
            </ul>
          </div>

          <div class="bg-white border border-[#e2e5e8] p-6 card-frame">
            <h3 class="text-base font-semibold uppercase tracking-wider text-[#1a1d20] mb-3">Software & Technical Stack</h3>
            <ul class="space-y-3 text-xs md:text-sm text-[#595f65]">
              <li><strong class="text-[#1a1d20]">Computational BIM:</strong> Autodesk Revit, ArchiCAD, Navisworks clash detection.</li>
              <li><strong class="text-[#1a1d20]">Parametric & Form-Generation:</strong> Rhino 3D, Grasshopper, SketchUp Pro.</li>
              <li><strong class="text-[#1a1d20]">Visualization & Media:</strong> Enscape, V-Ray, Lumion, Adobe Creative Cloud Suite.</li>
              <li><strong class="text-[#1a1d20]">Analog Methods:</strong> Ink drafting, charcoal massing, watercolor rendering.</li>
            </ul>
          </div>
        </div>

        <!-- Awards Summary -->
        __ACCOLADES__

      </div>

    </div>
  </main>

  __FOOTER__

</body>
</html>
"""
    return page.replace('__SHARED_HEAD__', SHARED_HEAD_TAGS)\
               .replace('__HEADER__', generate_header("about"))\
               .replace('__ACCOLADES__', generate_accolades_section())\
               .replace('__FOOTER__', generate_footer())

def generate_contact_page():
    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Contact & Inquiries &bull; Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  __HEADER__

  <!-- Breadcrumb Navigation -->
  <div class="w-full bg-white border-b border-[#e2e5e8] py-3 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto text-xs font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20]">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">Contact</span>
    </div>
  </div>

  <main class="w-full bg-[#f8f9fa] py-16 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        
        <!-- Left Column: Alex's Portrait (40% Viewport on Large Screens, zero rounded corners) -->
        <div class="lg:col-span-5 flex flex-col">
          <div class="w-full aspect-[4/5] bg-[#1a1d20] border border-[#1a1d20] overflow-hidden">
            <img src="assets/official/alex_portrait.png" alt="Aleksandre Karpov" class="w-full h-full object-cover">
          </div>
          <div class="mt-4 p-4 bg-white border border-[#e2e5e8]">
            <span class="text-sm font-semibold tracking-wider uppercase text-[#1a1d20] block">Aleksandre Karpov</span>
            <span class="text-xs font-mono text-[#595f65] uppercase tracking-widest block mt-0.5">Karpov Design LLC &bull; Charlotte, NC</span>
          </div>
        </div>

        <!-- Right Column: Direct Coordinates & Dynamic Inquiry Form -->
        <div class="lg:col-span-7 space-y-10">
          
          <div>
            <h1 class="text-3xl md:text-4xl font-semibold tracking-tight text-[#1a1d20] mb-4">Get in touch</h1>
            <p class="text-sm text-[#595f65] leading-relaxed max-w-xl">
              For residential design commissions, computational BIM consulting, or competition collaborations, reach out directly.
            </p>
          </div>

          <!-- Direct Coordinates Grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 border-t border-b border-[#e2e5e8] py-6">
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#595f65] block">United States Direct</span>
              <a href="tel:+17048459596" class="text-sm font-semibold text-[#1a1d20] hover:text-[#de602e] transition-colors mt-1 block">
                +1 (704) 845-9596
              </a>
              <span class="text-xs text-[#767676]">Charlotte, North Carolina</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#595f65] block">International Line</span>
              <a href="tel:+905385907458" class="text-sm font-semibold text-[#1a1d20] hover:text-[#de602e] transition-colors mt-1 block">
                +90 (538) 590-7458
              </a>
              <span class="text-xs text-[#767676]">Aegean Basin / European Projects</span>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#595f65] block">Electronic Mail</span>
              <a href="mailto:contact@karpovdesign.com" class="text-sm font-semibold text-[#1a1d20] hover:text-[#de602e] transition-colors mt-1 block">
                contact@karpovdesign.com
              </a>
            </div>
            <div>
              <span class="text-[10px] font-mono uppercase tracking-widest text-[#595f65] block">Studio Location</span>
              <span class="text-sm font-semibold text-[#1a1d20] mt-1 block">Charlotte, NC 28223</span>
              <span class="text-xs text-[#767676]">By Appointment Only</span>
            </div>
          </div>

          <!-- Form: 'Get in touch', zero labels on textarea, orange submit button -->
          <form onsubmit="handleInquirySubmit(event)" class="space-y-6 bg-white border border-[#e2e5e8] p-8">
            <h3 class="text-base font-semibold uppercase tracking-wider text-[#1a1d20]">Get in touch</h3>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Name *</label>
                <input type="text" required placeholder="Your full name" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
              </div>
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Email *</label>
                <input type="email" required placeholder="your.email@domain.com" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Site Location</label>
                <input type="text" placeholder="e.g. Asheville, NC" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
              </div>
              <div>
                <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Telephone</label>
                <input type="tel" placeholder="e.g. +1 (704) 000-0000" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-3 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e]">
              </div>
            </div>

            <div>
              <label class="block text-xs font-mono uppercase tracking-wider text-[#1a1d20] mb-2">Project Scope & Program Requirements *</label>
              <textarea id="contact-scope-textarea" rows="6" required placeholder="Describe your vision, site parameters, program requirements..." oninput="autoExpandTextarea(this)" class="w-full bg-[#f8f9fa] border border-[#e2e5e8] p-4 text-xs text-[#1a1d20] focus:outline-none focus:border-[#de602e] resize-none leading-relaxed"></textarea>
            </div>

            <div class="flex items-center justify-between pt-2">
              <span class="text-[11px] text-[#595f65]">Confidentiality guaranteed.</span>
              <!-- Orange Submit Button -->
              <button type="submit" class="px-10 py-3 bg-[#de602e] hover:bg-[#ad4b24] text-white text-xs font-mono uppercase tracking-widest font-semibold transition-colors shadow-sm">
                Submit &rarr;
              </button>
            </div>
            
            <div id="form-success" class="hidden p-4 bg-[#e4f0f2] border border-[#38606a] text-xs text-[#2b4951]">
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
               .replace('__HEADER__', generate_header("contact"))\
               .replace('__FOOTER__', generate_footer())

def generate_academy_page():
    page = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  __SHARED_HEAD__
  <title>Academy & Masterclasses &bull; Aleksandre Karpov &bull; Karpov Design LLC</title>
</head>
<body class="antialiased bg-[#f8f9fa] text-[#1a1d20]">

  <!-- Dedicated Header for Academy (Unlinked from Main Nav) -->
  <header class="w-full bg-[#f8f9fa]/95 backdrop-blur-md border-b border-[#e2e5e8] z-50 sticky top-0 transition-all">
    <div class="max-w-[1920px] mx-auto px-6 md:px-12 lg:px-16 flex items-center justify-between min-h-[84px]">
      <a href="index.html" class="flex items-center gap-3.5">
        <img src="assets/official/logo_charcoal.svg" alt="KAD Logo" class="h-10 w-auto">
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

  <!-- Breadcrumb Navigation -->
  <div class="w-full bg-white border-b border-[#e2e5e8] py-3 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto text-xs font-mono uppercase tracking-widest text-[#595f65]">
      <a href="index.html" class="hover:text-[#1a1d20]">Home</a>
      <span class="mx-2">&bull;</span>
      <span class="text-[#1a1d20] font-semibold">Academy (Private Syllabus)</span>
    </div>
  </div>

  <main class="w-full bg-[#f8f9fa] py-16 px-6 md:px-12 lg:px-16">
    <div class="max-w-[1920px] mx-auto space-y-16">
      
      <!-- Centerpiece Masterclass Player -->
      <div class="border border-[#1a1d20] bg-white p-6 md:p-10 card-frame">
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
              <h2 class="text-xl md:text-2xl font-semibold text-[#1a1d20] mb-3">Tectonic Synthesis: From Watercolor Intuition to BIM Execution</h2>
              <p class="text-xs md:text-sm text-[#595f65] leading-relaxed mb-4">
                Aleksandre Karpov breaks down the complete workflow of bridging analog artistic gesture with rigorous Revit parametric families, daylight simulation, and constructible documentation.
              </p>
            </div>
            <div class="border-t border-[#e2e5e8] pt-4">
              <span class="text-xs font-mono text-[#595f65] block mb-2">Lecturer: Aleksandre Karpov &bull; UNCC Studio Fellow</span>
              <button class="w-full py-2.5 bg-[#1a1d20] hover:bg-[#de602e] text-white text-xs font-mono uppercase tracking-widest transition-colors font-semibold">
                Access Full Studio Lecture &rarr;
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Video Tutorial Modules -->
      <div>
        <h3 class="text-lg font-semibold uppercase tracking-wider text-[#1a1d20] mb-6">Technical Video Modules</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white border border-[#e2e5e8] card-frame overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden">
              <img src="assets/official/projects/seed-retreat/seed_8.jpg" alt="Tutorial 1" class="w-full h-full object-cover">
            </div>
            <div class="p-5">
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-2">Mass-Timber Envelope Systems</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Passive ventilation, cross-laminated timber thermal mass, and envelope integration.</p>
            </div>
          </div>

          <div class="bg-white border border-[#e2e5e8] card-frame overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden">
              <img src="assets/official/projects/multi-city/multi_city_15.jpg" alt="Tutorial 2" class="w-full h-full object-cover">
            </div>
            <div class="p-5">
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-2">Adaptive Reuse & Structural BIM</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Laser scanning registration, point-cloud integration, and historic masonry rehabilitation.</p>
            </div>
          </div>

          <div class="bg-white border border-[#e2e5e8] card-frame overflow-hidden">
            <div class="aspect-video bg-[#1a1d20] overflow-hidden">
              <img src="assets/official/projects/travel-sketches/ak_10.jpg" alt="Tutorial 3" class="w-full h-full object-cover">
            </div>
            <div class="p-5">
              <h4 class="text-sm font-semibold text-[#1a1d20] mb-2">Plein-Air Spatial Perception</h4>
              <p class="text-xs text-[#595f65] leading-relaxed">Translating atmospheric perspective and wash depth into physical spatial sequences.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Downloadable BIM Resources -->
      <div class="border-t border-[#e2e5e8] pt-12">
        <h3 class="text-lg font-semibold uppercase tracking-wider text-[#1a1d20] mb-6">Computational Resources & Templates</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="p-6 bg-white border border-[#e2e5e8] flex items-center justify-between">
            <div>
              <h4 class="text-sm font-semibold text-[#1a1d20] mt-0.5">Parametric Louver & Shading Family Pack</h4>
              <span class="text-xs text-[#595f65]">Dynamo + Revit Adaptive Components (.rfa)</span>
            </div>
            <a href="#" class="px-4 py-2 border border-[#1a1d20] hover:bg-[#de602e] hover:border-[#de602e] hover:text-white text-xs font-mono uppercase tracking-wider transition-colors">
              Download .ZIP
            </a>
          </div>

          <div class="p-6 bg-white border border-[#e2e5e8] flex items-center justify-between">
            <div>
              <h4 class="text-sm font-semibold text-[#1a1d20] mt-0.5">Architectural Line-Weight & Graphic Standard</h4>
              <span class="text-xs text-[#595f65]">UNCC / Karpov Design Pen Weights & Layouts (.ctb / .pdf)</span>
            </div>
            <a href="#" class="px-4 py-2 border border-[#1a1d20] hover:bg-[#de602e] hover:border-[#de602e] hover:text-white text-xs font-mono uppercase tracking-wider transition-colors">
              Download .PDF
            </a>
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
               .replace('__FOOTER__', generate_footer())

def main():
    print("Building Version 1 (index.html): Default title appears on image on hover...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_landing_page(is_variant=False))
    print("Saved index.html")

    print("Building Version 2 (variant.html): Variant title appears in space below image on hover...")
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

    print("All site pages built successfully with zero extraneous labels!")

if __name__ == '__main__':
    main()
