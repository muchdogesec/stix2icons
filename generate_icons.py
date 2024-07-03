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
    {
        "object": "attack-pattern",
        "type": "sdo",
        "colour_rgb": "34,119,181"
    },
    {
        "object": "campaign",
        "type": "sdo",
        "colour_rgb": "80,182,30"
    },
    {
        "object": "course-of-action",
        "type": "sdo",
        "colour_rgb": "161,198,40"
    },
    {
        "object": "grouping",
        "type": "sdo",
        "colour_rgb": "163,53,139"
    },
    {
        "object": "identity",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "identity_group",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "identity_system",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "identity_organization",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "identity_individual",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "identity_class",
        "type": "sdo",
        "colour_rgb": "146,150,151"
    },
    {
        "object": "incident",
        "type": "sdo",
        "colour_rgb": "251,182,22"
    },
    {
        "object": "indicator",
        "type": "sdo",
        "colour_rgb": "220,149,71"
    },
    {
        "object": "infrastructure",
        "type": "sdo",
        "colour_rgb": "174,215,191"
    },
    {
        "object": "intrusion-set",
        "type": "sdo",
        "colour_rgb": "56,178,193"
    },
    {
        "object": "location",
        "type": "sdo",
        "colour_rgb": "80,86,87"
    },
    {
        "object": "malware",
        "type": "sdo",
        "colour_rgb": "212,163,203"
    },
    {
        "object": "malware_family",
        "type": "sdo",
        "colour_rgb": "221,140,187"
    },
    {
        "object": "malware-analysis",
        "type": "sdo",
        "colour_rgb": "231,118,172"
    },
    {
        "object": "note",
        "type": "sdo",
        "colour_rgb": "80,86,87"
    },
    {
        "object": "observed-data",
        "type": "sdo",
        "colour_rgb": "0,0,0"
    },
    {
        "object": "opinion",
        "type": "sdo",
        "colour_rgb": "80,86,87"
    },
    {
        "object": "report",
        "type": "sdo",
        "colour_rgb": "119,146,121"
    },
    {
        "object": "threat-actor",
        "type": "sdo",
        "colour_rgb": "230,27,92"
    },
    {
        "object": "tool",
        "type": "sdo",
        "colour_rgb": "87,80,157"
    },
    {
        "object": "vulnerability",
        "type": "sdo",
        "colour_rgb": "255,209,0"
    },
    {
        "object": "weakness",
        "type": "sdo",
        "colour_rgb": "134,0,255"
    },
    {
        "object": "artifact",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "autonomous-system",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "directory",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "domain-name",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "email-addr",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "email-message",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "file",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "ipv4-addr",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "ipv6-addr",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "mac-addr",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "mutex",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "network-traffic",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "process",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "software",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "url",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "user-account",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "windows-registry-key",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "x509-certificate",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "bank-account",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "bank-card",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "cryptocurrency-transaction",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "cryptocurrency-wallet",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "phone-number",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "user-agent",
        "type": "sco",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "relationship",
        "type": "sro",
        "colour_rgb": "205,214,216"
    },
    {
        "object": "sighting",
        "type": "sro",
        "colour_rgb": "235,94,42"
    },
    {
        "object": "language-content",
        "type": "smo",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "marking-definition",
        "type": "smo",
        "colour_rgb": "192,192,192"
    },
    {
        "object": "marking-definition_tlpv1_white",
        "type": "smo",
        "colour_rgb": "255,255,255"
    },
    {
        "object": "marking-definition_tlpv1_green",
        "type": "smo",
        "colour_rgb": "51,255,0"
    },
    {
        "object": "marking-definition_tlpv1_amber",
        "type": "smo",
        "colour_rgb": "255,192,0"
    },
    {
        "object": "marking-definition_tlpv1_red",
        "type": "smo",
        "colour_rgb": "255,0,51"
    },
    {
        "object": "marking-definition_tlpv2_clear",
        "type": "smo",
        "colour_rgb": "255,255,255"
    },
    {
        "object": "marking-definition_tlpv2_green",
        "type": "smo",
        "colour_rgb": "51,255,0"
    },
    {
        "object": "marking-definition_tlpv2_amber",
        "type": "smo",
        "colour_rgb": "255,192,0"
    },
    {
        "object": "marking-definition_tlpv2_amber_strict",
        "type": "smo",
        "colour_rgb": "255,192,0"
    },
    {
        "object": "marking-definition_tlpv2_red",
        "type": "smo",
        "colour_rgb": "255,0,51"
    },
    {
        "object": "extension-definition",
        "type": "smo",
        "colour_rgb": "192,192,192"
    }
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
    return svg_content.replace('<path', f'<path style="fill:rgb({colour_rgb})"')

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
                png_output_path = os.path.join(png_dir, os.path.splitext(relative_path)[0] + '.png')
                
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

# Print list of files that were not created
if failed_files:
    print("\nThe following files were not created:")
    for file in failed_files:
        print(file)
else:
    print("\nAll files were created successfully.")