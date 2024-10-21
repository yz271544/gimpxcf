from PIL import Image, ImageDraw, ImageFont
import math

if __name__ == '__main__':
    # Create image
    width_px = int(42 * 300)
    height_px = int(29.7 * 300)
    image = Image.new("RGB", (width_px, height_px), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw border
    border_thickness = 12
    draw.rectangle([(0, 0), (width_px - 1, height_px - 1)], outline=(0, 0, 0), width=border_thickness)

    # Add main title
    title_font = ImageFont.truetype("/home/etl/.fonts/simhei.ttf", 30)
    title_text = "主标题"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    title_x = (width_px - title_width) / 2
    title_y = 3 * 300 + 1
    draw.text((title_x, title_y), title_text, fill=(0, 0, 0), font=title_font)

    # Add index title
    index_font = ImageFont.truetype("/home/etl/.fonts/simhei.ttf", 14)
    index_text = "索引标题内容"
    index_bbox = draw.textbbox((0, 0), index_text, font=index_font)
    index_width = index_bbox[2] - index_bbox[0]
    index_height = index_bbox[3] - index_bbox[1]
    index_x = width_px - 0.5 * 300
    index_y = 0.5 * 300
    for char in index_text:
        char_bbox = draw.textbbox((0, 0), char, font=index_font)
        char_width = char_bbox[2] - char_bbox[0]
        char_height = char_bbox[3] - char_bbox[1]
        draw.text((index_x, index_y), char, fill=(0, 0, 0), font=index_font)
        index_y += char_height

    # Add credit
    credit_font = ImageFont.truetype("/home/etl/.fonts/simhei.ttf", 12)
    credit_text = "XXXXXX 制"
    credit_bbox = draw.textbbox((0, 0), credit_text, font=credit_font)
    credit_width = credit_bbox[2] - credit_bbox[0]
    credit_height = credit_bbox[3] - credit_bbox[1]
    credit_x = width_px - 0.5 * 300 - credit_width
    credit_y = height_px - 0.5 * 300
    draw.text((credit_x, credit_y), credit_text, fill=(0, 0, 0), font=credit_font)

    # Save image
    image.save("output.png")