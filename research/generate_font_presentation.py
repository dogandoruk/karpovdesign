import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

output_pptx = r"c:\Users\doruk\Documents\Karpovdesign\Karpov_Design_Font_Analysis_Presentation.pptx"
assets_dir = r"c:\Users\doruk\Documents\Karpovdesign\scratch\pptx_assets"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return RGBColor(*(int(hex_str[i:i+2], 16) for i in (0, 2, 4)))

# Exact computed CSS audit data
slides_data = [
    {
        "id": "big",
        "slide_num": "01",
        "studio": "BIG | Bjarke Ingels Group",
        "url": "big.dk",
        "bg_hex": "#FFFFFF",
        "img_file": "big_rich_crop.png",
        "card_file": "big_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Primary Text Ink"),
            ("#797979", "Secondary / Narrative"),
            ("#E5E5E5", "Border / Structure")
        ]
    },
    {
        "id": "field",
        "slide_num": "02",
        "studio": "Field Architecture",
        "url": "fieldarchitecture.com",
        "bg_hex": "#FFFFFF",
        "img_file": "field_rich_crop.png",
        "card_file": "field_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Body Narrative Ink"),
            ("#4E5254", "Heading & Nav"),
            ("#EEEDEB", "Section Container")
        ]
    },
    {
        "id": "fran",
        "slide_num": "03",
        "studio": "Fran Silvestre Arquitectos",
        "url": "fransilvestrearquitectos.com",
        "bg_hex": "#FFFFFF",
        "img_file": "fran_rich_crop.png",
        "card_file": "fran_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Paragraph Ink"),
            ("#777777", "Subhead / Nav"),
            ("#AEAEAE", "Display Meta")
        ]
    },
    {
        "id": "modernhouse",
        "slide_num": "04",
        "studio": "The Modern House",
        "url": "themodernhouse.com",
        "bg_hex": "#FFFFFF",
        "img_file": "modernhouse_rich_crop.png",
        "card_file": "modernhouse_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Editorial Serif Ink"),
            ("#313131", "Secondary Text"),
            ("#F5F3EF", "Paper Tint Container")
        ]
    },
    {
        "id": "insitu",
        "slide_num": "05",
        "studio": "In Situ Studio",
        "url": "insitustudio.us",
        "bg_hex": "#FFFFFF",
        "img_file": "insitu_rich_crop.png",
        "card_file": "insitu_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Primary Text Ink"),
            ("#3DBFE8", "Link Accent Cyan"),
            ("#BDE1F4", "Light Tint Container")
        ]
    },
    {
        "id": "ravn",
        "slide_num": "06",
        "studio": "RAVN Arkitektur",
        "url": "ravnarkitektur.dk",
        "bg_hex": "#FFFFFF",
        "img_file": "ravn_rich_crop.png",
        "card_file": "ravn_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Primary Text Ink"),
            ("#85868A", "Metadata Grey"),
            ("#666666", "Panel Frame")
        ]
    },
    {
        "id": "studiomm",
        "slide_num": "07",
        "studio": "Studio MM Architect",
        "url": "maricamckeel.com",
        "bg_hex": "#FFFFFF",
        "img_file": "studiomm_rich_crop.png",
        "card_file": "studiomm_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Primary Text Ink"),
            ("#666666", "Case Study Body"),
            ("#123A8A", "Link Accent Blue")
        ]
    },
    {
        "id": "den",
        "slide_num": "08",
        "studio": "Den Outdoors",
        "url": "denoutdoors.com",
        "bg_hex": "#FFFFFF",
        "img_file": "den_rich_crop.png",
        "card_file": "den_card.png",
        "palette": [
            ("#FFFFFF", "Primary Canvas"),
            ("#000000", "Text / Hero Dark"),
            ("#F0EEE9", "Warm Section BG"),
            ("#623CEA", "Interactive Purple")
        ]
    },
    {
        "id": "mclaren",
        "slide_num": "09",
        "studio": "McLaren Excell",
        "url": "mclarenexcell.com",
        "bg_hex": "#F7F7F7",
        "img_file": "mclaren_rich_crop.png",
        "card_file": "mclaren_card.png",
        "palette": [
            ("#F7F7F7", "Canvas / Background"),
            ("#242424", "Primary Dark Ink"),
            ("#4D4D4D", "Secondary Slate"),
            ("#DEDFE0", "Structure Border")
        ]
    },
    {
        "id": "mls",
        "slide_num": "10",
        "studio": "MacKay-Lyons Sweetapple",
        "url": "mlsarchitects.ca",
        "bg_hex": "#FFFFFF",
        "img_file": "mls_rich_crop.png",
        "card_file": "mls_card.png",
        "palette": [
            ("#FFFFFF", "Canvas / Background"),
            ("#000000", "Primary Text Ink"),
            ("#4F5861", "Atlantic Slate"),
            ("#9BA5AE", "Sea Mist Tint")
        ]
    }
]

for d in slides_data:
    slide = prs.slides.add_slide(blank_layout)
    
    # 1. Slide Background
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = hex_to_rgb(d["bg_hex"])
    
    # 2. Header Bar
    header_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(8.0), Inches(0.5))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = d["studio"].upper()
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGBColor(26, 26, 26)
    
    p_url = tf.add_paragraph()
    p_url.text = f"https://{d['url']}"
    p_url.font.name = "Arial"
    p_url.font.size = Pt(10)
    p_url.font.color.rgb = RGBColor(120, 120, 120)
    
    counter_box = slide.shapes.add_textbox(Inches(10.5), Inches(0.4), Inches(2.2), Inches(0.5))
    tf_c = counter_box.text_frame
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.alignment = PP_ALIGN.RIGHT
    p_c.text = f"{d['slide_num']} / 10"
    p_c.font.name = "Arial"
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = RGBColor(150, 150, 150)
    
    line = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(0.6), Inches(1.05), Inches(12.133), Inches(0.01)
    )
    line.fill.solid()
    line.fill.fore_color.rgb = RGBColor(225, 225, 225)
    line.line.color.rgb = RGBColor(225, 225, 225)
    
    # -------------------------------------------------------------
    # LEFT HALF (50%): SCROLLED RICH TEXT SNIPPET & STRICT CSS SWATCHES
    # -------------------------------------------------------------
    img_path = os.path.join(assets_dir, d["img_file"])
    left_x = Inches(0.6)
    left_w = Inches(5.8)
    
    if os.path.exists(img_path):
        img_top = Inches(1.3)
        img_h = Inches(3.26)
        
        frame = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            left_x - Inches(0.04), img_top - Inches(0.04),
            left_w + Inches(0.08), img_h + Inches(0.08)
        )
        frame.fill.solid()
        frame.fill.fore_color.rgb = RGBColor(255, 255, 255)
        frame.line.color.rgb = RGBColor(215, 215, 215)
        frame.line.width = Pt(1)
        
        slide.shapes.add_picture(img_path, left_x, img_top, width=left_w, height=img_h)
    
    swatch_y = Inches(4.8)
    swatch_w = Inches(1.35)
    swatch_gap = Inches(0.13)
    swatch_h = Inches(1.8)
    
    for idx, (hex_code, css_role) in enumerate(d["palette"]):
        cur_x = left_x + idx * (swatch_w + swatch_gap)
        
        card = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            cur_x, swatch_y, swatch_w, swatch_h
        )
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(255, 255, 255)
        card.line.color.rgb = RGBColor(220, 220, 220)
        card.line.width = Pt(0.75)
        
        chip = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            cur_x + Inches(0.08), swatch_y + Inches(0.08),
            swatch_w - Inches(0.16), Inches(0.95)
        )
        chip.fill.solid()
        chip.fill.fore_color.rgb = hex_to_rgb(hex_code)
        chip.line.color.rgb = RGBColor(200, 200, 200) if hex_code.upper() in ["#FFFFFF", "#FAFAFA", "#F8F7F4", "#F6F5F2", "#F5F3EF", "#F7F7F7"] else hex_to_rgb(hex_code)
        chip.line.width = Pt(0.5)
        
        hex_tb = slide.shapes.add_textbox(cur_x + Inches(0.08), swatch_y + Inches(1.1), swatch_w - Inches(0.16), Inches(0.25))
        tf_hex = hex_tb.text_frame
        tf_hex.margin_left = tf_hex.margin_top = tf_hex.margin_right = tf_hex.margin_bottom = 0
        p_hex = tf_hex.paragraphs[0]
        p_hex.text = hex_code.upper()
        p_hex.font.name = "Arial"
        p_hex.font.size = Pt(9.5)
        p_hex.font.bold = True
        p_hex.font.color.rgb = RGBColor(30, 30, 30)
        
        role_tb = slide.shapes.add_textbox(cur_x + Inches(0.08), swatch_y + Inches(1.35), swatch_w - Inches(0.16), Inches(0.35))
        tf_role = role_tb.text_frame
        tf_role.word_wrap = True
        tf_role.margin_left = tf_role.margin_top = tf_role.margin_right = tf_role.margin_bottom = 0
        p_role = tf_role.paragraphs[0]
        p_role.text = css_role
        p_role.font.name = "Arial"
        p_role.font.size = Pt(8.0)
        p_role.font.color.rgb = RGBColor(100, 100, 100)
        
    # -------------------------------------------------------------
    # RIGHT HALF (50%): STRICT CSS SPECIMEN CARD
    # -------------------------------------------------------------
    right_x = Inches(6.8)
    right_y = Inches(1.3)
    right_w = Inches(5.9)
    right_h = Inches(5.3)
    
    card_path = os.path.join(assets_dir, d["card_file"])
    if os.path.exists(card_path):
        slide.shapes.add_picture(card_path, right_x, right_y, width=right_w, height=right_h)

prs.save(output_pptx)
print(f"Successfully generated 100% strict CSS PPTX at:\n  {output_pptx}")
print(f"File size: {os.path.getsize(output_pptx) // 1024} KB")
