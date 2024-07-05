import os
import cairosvg
from PIL import Image

# Directory paths for normal and round input and output
input_normal_dir = "input_vectors/normal"
input_round_dir = "input_vectors/round"
output_normal_dir = "output_files/rgb/normal/svg"
output_normal_png_dir = "output_files/rgb/normal/png"
output_round_dir = "output_files/rgb/round/svg"
output_round_png_dir = "output_files/rgb/round/png"
output_black_dir = "output_files/black"
output_white_dir = "output_files/white"
output_black_normal_dir = os.path.join(output_black_dir, "normal/svg")
output_black_normal_png_dir = os.path.join(output_black_dir, "normal/png")
output_black_round_dir = os.path.join(output_black_dir, "round/svg")
output_black_round_png_dir = os.path.join(output_black_dir, "round/png")
output_white_normal_dir = os.path.join(output_white_dir, "normal/svg")
output_white_normal_png_dir = os.path.join(output_white_dir, "normal/png")
output_white_round_dir = os.path.join(output_white_dir, "round/svg")
output_white_round_png_dir = os.path.join(output_white_dir, "round/png")

objects = [
    {"object": "attack-pattern", "type": "sdo", "colour_rgb": "34,119,181"},
    {"object": "campaign", "type": "sdo", "colour_rgb": "80,182,30"},
    {"object": "course-of-action", "type": "sdo", "colour_rgb": "161,198,40"},
    {"object": "grouping", "type": "sdo", "colour_rgb": "163,53,139"},
    {"object": "identity", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "identity_group", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "identity_system", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "identity_organization", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "identity_individual", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "identity_class", "type": "sdo", "colour_rgb": "156,154,254"},
    {"object": "incident", "type": "sdo", "colour_rgb": "251,182,22"},
    {"object": "indicator", "type": "sdo", "colour_rgb": "220,149,71"},
    {"object": "infrastructure", "type": "sdo", "colour_rgb": "174,215,191"},
    {"object": "intrusion-set", "type": "sdo", "colour_rgb": "56,178,193"},
    {"object": "location", "type": "sdo", "colour_rgb": "252,159,157"},
    {"object": "malware", "type": "sdo", "colour_rgb": "212,163,203"},
    {"object": "malware_family", "type": "sdo", "colour_rgb": "221,140,187"},
    {"object": "malware-analysis", "type": "sdo", "colour_rgb": "231,118,172"},
    {"object": "note", "type": "sdo", "colour_rgb": "136,200,129"},
    {"object": "observed-data", "type": "sdo", "colour_rgb": "252,204,184"},
    {"object": "opinion", "type": "sdo", "colour_rgb": "144,157,199"},
    {"object": "report", "type": "sdo", "colour_rgb": "119,146,121"},
    {"object": "threat-actor", "type": "sdo", "colour_rgb": "230,27,92"},
    {"object": "tool", "type": "sdo", "colour_rgb": "87,80,157"},
    {"object": "vulnerability", "type": "sdo", "colour_rgb": "255,209,0"},
    {"object": "weakness", "type": "sdo", "colour_rgb": "94,49,128"},
    {"object": "artifact", "type": "sco", "colour_rgb": "149,229,250"},
    {"object": "autonomous-system", "type": "sco", "colour_rgb": "161,248,128"},
    {"object": "directory", "type": "sco", "colour_rgb": "183,245,206"},
    {"object": "domain-name", "type": "sco", "colour_rgb": "255,185,167"},
    {"object": "email-addr", "type": "sco", "colour_rgb": "145,128,242"},
    {"object": "email-message", "type": "sco", "colour_rgb": "249,129,229"},
    {"object": "file", "type": "sco", "colour_rgb": "199,148,187"},
    {"object": "ipv4-addr", "type": "sco", "colour_rgb": "222,130,171"},
    {"object": "ipv6-addr", "type": "sco", "colour_rgb": "222,130,171"},
    {"object": "mac-addr", "type": "sco", "colour_rgb": "247,184,203"},
    {"object": "mutex", "type": "sco", "colour_rgb": "240,228,153"},
    {"object": "network-traffic", "type": "sco", "colour_rgb": "132,207,240"},
    {"object": "process", "type": "sco", "colour_rgb": "187,199,153"},
    {"object": "software", "type": "sco", "colour_rgb": "233,145,202"},
    {"object": "url", "type": "sco", "colour_rgb": "206,207,241"},
    {"object": "user-account", "type": "sco", "colour_rgb": "213,191,132"},
    {"object": "windows-registry-key", "type": "sco", "colour_rgb": "132,196,170"},
    {"object": "x509-certificate", "type": "sco", "colour_rgb": "246,160,242"},
    {"object": "bank-account", "type": "sco", "colour_rgb": "232,228,170"},
    {"object": "bank-card", "type": "sco", "colour_rgb": "145,178,181"},
    {"object": "cryptocurrency-transaction", "type": "sco", "colour_rgb": "222,233,167"},
    {"object": "cryptocurrency-wallet", "type": "sco", "colour_rgb": "156,218,184"},
    {"object": "phone-number", "type": "sco", "colour_rgb": "226,189,239"},
    {"object": "user-agent", "type": "sco", "colour_rgb": "152,199,239"},
    {"object": "relationship", "type": "sro", "colour_rgb": "148,243,139"},
    {"object": "sighting", "type": "sro", "colour_rgb": "235,94,42"}
]

def find_colour_rgb(object_name, color='rgb'):
    for obj in objects:
        if obj['object'] == object_name:
            if color == 'black':
                return "0,0,0"
            elif color == 'white':
                return "255,255,255"
            else:
                return obj['colour_rgb']
    return None

def process_svg(svg_content, colour_rgb):
    svg_content = svg_content.replace('<path', f'<path style="fill:rgb({colour_rgb})"')
    svg_content = svg_content.replace('<rect', f'<rect style="fill:rgb({colour_rgb})"')
    svg_content = svg_content.replace('<circle', f'<circle style="fill:rgb({colour_rgb})"')
    svg_content = svg_content.replace('<ellipse', f'<ellipse style="fill:rgb({colour_rgb})"')
    return svg_content

def convert_svg_to_png(svg_path, png_path):
    try:
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=256, output_height=256)
    except Exception as e:
        print(f"Error with cairosvg conversion: {e}")

def process_directory(input_dir, output_dir, png_dir, color='rgb'):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                relative_path = os.path.relpath(svg_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                png_output_path = os.path.join(png_dir, relative_path).replace('.svg', '.png')
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                os.makedirs(os.path.dirname(png_output_path), exist_ok=True)
                
                object_name = os.path.splitext(file)[0]
                colour_rgb = find_colour_rgb(object_name, color)
                
                if colour_rgb:
                    with open(svg_path, 'r') as file:
                        svg_content = file.read()
                    
                    processed_svg = process_svg(svg_content, colour_rgb)
                    
                    with open(output_path, 'w') as file:
                        file.write(processed_svg)
                    
                    convert_svg_to_png(output_path, png_output_path)
                    print(f"Processed {svg_path} -> {output_path} and {png_output_path}")

def generate_markdown_table():
    markdown_table = "| Object | Type | RGB | RGB Circle | Black | Black Circle | White | White Circle |\n"
    markdown_table += "|--------|------|-----|-----------|-------|-------------|-------|-------------|\n"
    
    for obj in objects:
        object_name = obj['object']
        object_type = obj['type']
        rgb_png = os.path.join(output_normal_png_dir, object_type, f"{object_name}.png")
        rgb_circle_png = os.path.join(output_round_png_dir, object_type, f"{object_name}.png")
        black_png = os.path.join(output_black_normal_png_dir, object_type, f"{object_name}.png")
        black_circle_png = os.path.join(output_black_round_png_dir, object_type, f"{object_name}.png")
        white_png = os.path.join(output_white_normal_png_dir, object_type, f"{object_name}.png")
        white_circle_png = os.path.join(output_white_round_png_dir, object_type, f"{object_name}.png")

        markdown_table += f"| {object_name} | {object_type} | ![]({rgb_png}) | ![]({rgb_circle_png}) | ![]({black_png}) | ![]({black_circle_png}) | ![]({white_png}) | ![]({white_circle_png}) |\n"
    
    return markdown_table

def save_markdown_table_to_file():
    markdown_table = generate_markdown_table()
    with open("objects.md", "w") as file:
        file.write(markdown_table)
    print("Markdown table has been saved to objects.md")

# Track failed files
failed_files = []

# Process the directory for normal output (RGB)
process_directory(input_normal_dir, output_normal_dir, output_normal_png_dir)
# Process the directory for round output (RGB)
process_directory(input_round_dir, output_round_dir, output_round_png_dir)

# Process the directory for black output
process_directory(input_normal_dir, output_black_normal_dir, output_black_normal_png_dir, color='black')
process_directory(input_round_dir, output_black_round_dir, output_black_round_png_dir, color='black')

# Process the directory for white output
process_directory(input_normal_dir, output_white_normal_dir, output_white_normal_png_dir, color='white')
process_directory(input_round_dir, output_white_round_dir, output_white_round_png_dir, color='white')

# Save the Markdown table to a file
save_markdown_table_to_file()

# Print list of files that were not created
if failed_files:
    print("\nThe following files were not created:")
    for file in failed_files:
        print(file)
else:
    print("\nAll files were created successfully.")