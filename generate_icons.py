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
    # SDO - core
    {"object": "attack-pattern", "type": "SDO", "colour_rgb": "34, 119, 181", "description": "strong cobalt blue"},
    {"object": "campaign", "type": "SDO", "colour_rgb": "80, 182, 30", "description": "vivid grass green"},
    {"object": "course-of-action", "type": "SDO", "colour_rgb": "161, 198, 40", "description": "bright chartreuse green"},
    {"object": "grouping", "type": "SDO", "colour_rgb": "163, 53, 139", "description": "bold magenta purple"},
    {"object": "identity", "type": "SDO", "colour_rgb": "0, 150, 136", "description": "teal green"},
    {"object": "incident", "type": "SDO", "colour_rgb": "251, 182, 22", "description": "golden yellow"},
    {"object": "indicator", "type": "SDO", "colour_rgb": "220, 149, 71", "description": "warm amber orange"},
    {"object": "infrastructure", "type": "SDO", "colour_rgb": "255, 87, 34", "description": "bright orange-red"},
    {"object": "intrusion-set", "type": "SDO", "colour_rgb": "56, 178, 193", "description": "turquoise blue"},
    {"object": "location", "type": "SDO", "colour_rgb": "233, 30, 99", "description": "hot pink"},
    {"object": "malware", "type": "SDO", "colour_rgb": "244, 67, 54", "description": "vivid red"},
    {"object": "malware-analysis", "type": "SDO", "colour_rgb": "231, 118, 172", "description": "bright rose pink"},
    {"object": "note", "type": "SDO", "colour_rgb": "46, 125, 50", "description": "forest green"},
    {"object": "observed-data", "type": "SDO", "colour_rgb": "27, 94, 32", "description": "dark evergreen"},
    {"object": "opinion", "type": "SDO", "colour_rgb": "139, 195, 74", "description": "fresh lime green"},
    {"object": "report", "type": "SDO", "colour_rgb": "194, 24, 91", "description": "deep raspberry magenta"},
    {"object": "threat-actor", "type": "SDO", "colour_rgb": "230, 27, 92", "description": "crimson pink-red"},
    {"object": "tool", "type": "SDO", "colour_rgb": "87, 80, 157", "description": "royal purple"},
    {"object": "vulnerability", "type": "SDO", "colour_rgb": "255, 209, 0", "description": "bright sunflower yellow"},

    # SDO - custom
    {"object": "weakness", "type": "SDO", "colour_rgb": "94,49,128", "description": "dark violet purple"},
    {"object": "exploit", "type": "SDO", "colour_rgb": "0,132,80", "description": "emerald green"},

    # SDO - MITRE ATT&CK
    {"object": "x-mitre-detection-strategy", "type": "SDO", "colour_rgb": "0, 191, 255", "description": "vivid cyan blue"},
    {"object": "x-mitre-analytic", "type": "SDO", "colour_rgb": "255, 61, 0", "description": "blazing orange-red"},
    {"object": "x-mitre-log-source", "type": "SDO", "colour_rgb": "72, 61, 139", "description": "deep slate indigo"},
    {"object": "x-mitre-tactic", "type": "SDO", "colour_rgb": "198, 40, 40", "description": "dark scarlet red"},
    {"object": "x-mitre-asset", "type": "SDO", "colour_rgb": "0, 255, 127", "description": "neon spring green"},
    {"object": "x-mitre-data-source", "type": "SDO", "colour_rgb": "0, 188, 212", "description": "bright aqua blue"},
    {"object": "x-mitre-data-component", "type": "SDO", "colour_rgb": "63, 81, 181", "description": "indigo blue"},

    # SDO - Attack Flow
    {"object": "attack-flow", "type": "SDO", "colour_rgb": "156, 39, 176", "description": "vivid violet purple"},
    {"object": "attack-action", "type": "SDO", "colour_rgb": "0, 105, 92", "description": "dark teal green"},

    # SCO - core
    {"object": "artifact", "type": "SCO", "colour_rgb": "149,229,250", "description": "pastel sky blue"},
    {"object": "autonomous-system", "type": "SCO", "colour_rgb": "161,248,128", "description": "pastel lime green"},
    {"object": "directory", "type": "SCO", "colour_rgb": "183,245,206", "description": "mint green"},
    {"object": "domain-name", "type": "SCO", "colour_rgb": "255,185,167", "description": "peach pink"},
    {"object": "email-addr", "type": "SCO", "colour_rgb": "186,168,250", "description": "lavender violet"},
    {"object": "email-message", "type": "SCO", "colour_rgb": "249,177,233", "description": "soft rose pink"},
    {"object": "file", "type": "SCO", "colour_rgb": "199,148,187", "description": "dusty mauve"},
    {"object": "ipv4-addr", "type": "SCO", "colour_rgb": "222,130,171", "description": "pastel magenta"},
    {"object": "ipv6-addr", "type": "SCO", "colour_rgb": "222,130,171", "description": "pastel magenta"},
    {"object": "mac-addr", "type": "SCO", "colour_rgb": "247,184,203", "description": "light rose"},
    {"object": "mutex", "type": "SCO", "colour_rgb": "240,228,153", "description": "pastel yellow"},
    {"object": "network-traffic", "type": "SCO", "colour_rgb": "132,207,240", "description": "baby blue"},
    {"object": "process", "type": "SCO", "colour_rgb": "187,199,153", "description": "sage green"},
    {"object": "software", "type": "SCO", "colour_rgb": "233,145,202", "description": "orchid pink"},
    {"object": "url", "type": "SCO", "colour_rgb": "206,207,241", "description": "periwinkle"},
    {"object": "user-account", "type": "SCO", "colour_rgb": "213,191,132", "description": "khaki beige"},
    {"object": "windows-registry-key", "type": "SCO", "colour_rgb": "132,196,170", "description": "seafoam green"},
    {"object": "x509-certificate", "type": "SCO", "colour_rgb": "246,160,242", "description": "light fuchsia"},

    # SCO - custom
    {"object": "bank-account", "type": "SCO", "colour_rgb": "232,228,170", "description": "pale sand yellow"},
    {"object": "bank-card", "type": "SCO", "colour_rgb": "145,178,181", "description": "muted teal grey"},
    {"object": "cryptocurrency-transaction", "type": "SCO", "colour_rgb": "222,233,167", "description": "pastel olive green"},
    {"object": "cryptocurrency-wallet", "type": "SCO", "colour_rgb": "156,218,184", "description": "mint teal"},
    {"object": "cryptocurrency-exchange", "type": "SCO", "colour_rgb": "173,205,255", "description": "pastel cornflower blue"},
    {"object": "phone-number", "type": "SCO", "colour_rgb": "226,189,239", "description": "soft lilac"},
    {"object": "user-agent", "type": "SCO", "colour_rgb": "152,199,239", "description": "powder blue"},

    # SRO - core
    {"object": "relationship", "type": "SRO", "colour_rgb": "255, 20, 147", "description": "fluorescent neon pink"},
    {"object": "sighting", "type": "SRO", "colour_rgb": "57, 255, 20", "description": "fluorescent neon green"},
    
    # SMO - core
    {"object": "extension-definition", "type": "SMO", "colour_rgb": "224,224,224", "description": "soft light grey"},
    {"object": "marking-definition", "type": "SMO", "colour_rgb": "158,158,158", "description": "medium grey"},
    {"object": "language-content", "type": "SMO", "colour_rgb": "97,97,97", "description": "dark grey charcoal"}
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

def rgb_to_hex(rgb):
    r, g, b = map(int, rgb.split(','))
    return f"#{r:02x}{g:02x}{b:02x}"

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
    markdown_table = "| Object | Type | RGB | HEX | RGB Icon | RGB Circle Icon | Black Icon | Black Circle Icon | White Icon | White Circle Icon |\n"
    markdown_table += "|--------|------|-----|-----|----------|-----------------|------------|------------------|------------|------------------|\n"
    
    for obj in objects:
        object_name = obj['object']
        object_type = obj['type']
        colour_rgb = obj['colour_rgb']
        colour_hex = rgb_to_hex(colour_rgb)
        rgb_png = os.path.join(output_normal_png_dir, object_type, f"{object_name}.png")
        rgb_circle_png = os.path.join(output_round_png_dir, object_type, f"{object_name}.png")
        black_png = os.path.join(output_black_normal_png_dir, object_type, f"{object_name}.png")
        black_circle_png = os.path.join(output_black_round_png_dir, object_type, f"{object_name}.png")
        white_png = os.path.join(output_white_normal_png_dir, object_type, f"{object_name}.png")
        white_circle_png = os.path.join(output_white_round_png_dir, object_type, f"{object_name}.png")

        markdown_table += f"| {object_name} | {object_type} | {colour_rgb} | {colour_hex} | ![]({rgb_png}) | ![]({rgb_circle_png}) | ![]({black_png}) | ![]({black_circle_png}) | ![]({white_png}) | ![]({white_circle_png}) |\n"
    
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