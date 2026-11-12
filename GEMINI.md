# Karpov Design — Strict Project & Aesthetics Rules

## 1. Visual Zero-Clutter Principle (Strictly No Unrequested Visible Text)
- NEVER display visible metadata, labels, tags, categories, years, locations, dates, breadcrumbs, sub-labels, or helper texts on the front-end unless EXPLICITLY commanded in writing.
- Never assume standard web conventions (e.g. visible badges, category tags, timestamps, card outlines) apply to this site.
- If a visual UI element was not explicitly requested, IT MUST NOT BE RENDERED.

## 2. Technical SEO & Schema Integrity (Invisible / Backend Only)
- Preserve and organize rich semantic data, microdata, JSON-LD Schema.org, HTML semantic tags, and `data-*` attributes for search engines and technical SEO.
- All metadata (typology, year, location, status, awards) must be structured truthfully in the DOM/head/JSON-LD for machines, but kept completely invisible on the visual interface.

## 3. Universal Borderless Standard
- NEVER add decorative, container, outline, divider, or card borders (`border`, `border-t`, `border-b`, `border-x`, `outline`) to project cards, content cards, bio containers, forms, or about/contact elements.
- The aesthetic is strictly borderless and architectural, defined by negative space, crisp image rendering, and refined typography.

## 4. Project Cards Specification
- Visual Card Elements (Exclusively):
  1. The clean image thumbnail (4:3 aspect ratio, full color, zero overlay badges).
  2. The project title located in dedicated space beneath the image.
- Behavior (Historical Variant Standard):
  - On desktop: The title space beneath the image is empty by default; the project title appears on hover (`opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0 transition-all duration-300 ease-out`).
  - On mobile/touch: The title remains visible by default so touch users can browse seamlessly.
  - Zero visible container borders, zero visible dividing lines, zero visible typology/year/location text, zero visible "Built"/"Concept" badges.
  - Gutters between cards must be uniform horizontally and vertically (`gap-6 md:gap-8`).

## 5. About & Contact Pages Specification
- Completely borderless layout: no boxed cards, no divider lines, no category pill headers, no breadcrumb bars.
- Contact form inputs must use a clean, minimalist bottom underline (`border-b`, transparent background) with no outer box enclosure around the form.
