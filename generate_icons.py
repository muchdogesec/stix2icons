import os
import re
import cairosvg

# Directory paths for normal and round input and output
input_normal_dir = "input_vectors/normal"
output_normal_dir = "output/normal/rgb"
input_round_dir = "input_vectors/round"
output_round_dir = "output/round/rgb"

objects = [
    {"object": "attack-pattern", "type": "sdo", "colour_rgb": "34,119,181"},
    {"object": "campaign", "type": "sdo", "colour_rgb": "80,182,30"},
    {"object": "course-of-action", "type": "sdo", "colour_rgb": "161,198,40"},
    {"object": "grouping", "type": "sdo", "colour_rgb": "163,53,139"},
    {"object": "identity", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "identity_group", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "identity_system", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "identity_organization", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "identity_individual", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "identity_class", "type": "sdo", "colour_rgb": "146,150,151"},
    {"object": "incident", "type": "sdo", "colour_rgb": "251,182,22"},
    {"object": "indicator", "type": "sdo", "colour_rgb": "220,149,71"},
    {"object": "infrastructure", "type": "sdo", "colour_rgb": "174,215,191"},
    {"object": "intrusion-set", "type": "sdo", "colour_rgb": "56,178,193"},
    {"object": "location", "type": "sdo", "colour_rgb": "80,86,87"},
    {"object": "malware", "type": "sdo", "colour_rgb": "212,163,203"},
    {"object": "malware_family", "type": "sdo", "colour_rgb": "221,140,187"},
    {"object": "malware-analysis", "type": "sdo", "colour_rgb": "231,118,172"},
    {"object": "note", "type": "sdo", "colour_rgb": "80,86,87"},
    {"object": "observed-data", "type": "sdo", "colour_rgb": "0,0,0"},
    {"object": "opinion", "type": "sdo", "colour_rgb": "80,86,87"},
    {"object": "report", "type": "sdo", "colour_rgb": "119,146,121"},
    {"object": "threat-actor", "type": "sdo", "colour_rgb": "230,27,92"},
    {"object": "tool", "type": "sdo", "colour_rgb": "87,80,157"},
    {"object": "vulnerability", "type": "sdo", "colour_rgb": "255,209,0"},
    {"object": "weakness", "type": "sdo", "colour_rgb": "134,0,255"},
    {"object": "artifact", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "autonomous-system", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "directory", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "domain-name", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "email-addr", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "email-message", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "file", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "ipv4-addr", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "ipv6-addr", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "mac-addr", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "mutex", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "network-traffic", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "process", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "software", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "url", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "user-account", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "windows-registry-key", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "x509-certificate", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "bank-account", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "bank-card", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "cryptocurrency-transaction", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "cryptocurrency-wallet", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "phone-number", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "user-agent", "type": "sco", "colour_rgb": "192,192,192"},
    {"object": "relationship", "type": "sro", "colour_rgb": "205,214,216"},
    {"object": "sighting", "type": "sro", "colour_rgb": "235,94,42"}
]

def find_colour_rgb(object_name):
    for obj in objects:
        if obj['object'] == object_name:
            return obj['colour_rgb']
    return None

# Working normal processing function
def process_svg_normal(svg_path, output_path, colour_rgb):
    with open(svg_path, 'r') as file:
        svg_content = file.read()

    # Patterns to match and replace fill:none for Layer 1 and fill for Layer 2
    layer1_pattern = r'(<g[^>]*data-name="Layer 1"[^>]*>)(.*?)(</g>)'
    layer2_pattern = r'(<g[^>]*data-name="Layer 2"[^>]*>)(.*?)(</g>)'
    
    # Ensure Layer 1 has fill:none
    svg_content = re.sub(layer1_pattern, r'\1\2\3', svg_content, flags=re.DOTALL)
    svg_content = re.sub(r'fill="none"', 'fill="none"', svg_content, flags=re.IGNORECASE)
    
    # Ensure Layer 2 has the specified fill color
    svg_content = re.sub(layer2_pattern, f'\\1<g style="fill:rgb({colour_rgb});">\\2</g>\\3', svg_content, flags=re.DOTALL)

    # Write the modified SVG content to the new file in the output directory
    with open(output_path, 'w') as file:
        file.write(svg_content)

# Corrected round processing function
def process_svg_round(svg_path, output_path, colour_rgb):
    with open(svg_path, 'r') as file:
        svg_content = file.read()

    # Ensure Layer 1 has the specified fill color
    svg_content = re.sub(r'(<g[^>]*data-name="Layer 1"[^>]*>)', f'\\1<style>.colour-fill {{fill:rgb({colour_rgb});}}</style><g class="colour-fill">', svg_content, flags=re.IGNORECASE)
    
    # Ensure Layer 2 has fill:none
    svg_content = re.sub(r'(<g[^>]*data-name="Layer 2"[^>]*>)', r'\1<style>.no-fill {fill:none;}</style><g class="no-fill">', svg_content, flags=re.IGNORECASE)

    # Ensure proper closing of the added groups
    svg_content = re.sub(r'(</g>\s*</svg>)', r'</g></g>\1', svg_content, flags=re.IGNORECASE)

    # Write the modified SVG content to the new file in the output directory
    with open(output_path, 'w') as file:
        file.write(svg_content)

def process_directory(input_dir, output_dir, is_round=False):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                relative_path = os.path.relpath(svg_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Extract object name from the file name
                object_name = os.path.splitext(file)[0]
                colour_rgb = find_colour_rgb(object_name)
                
                if colour_rgb:
                    if is_round:
                        process_svg_round(svg_path, output_path, colour_rgb)
                    else:
                        process_svg_normal(svg_path, output_path, colour_rgb)
                    print(f"Processed {svg_path} -> {output_path}")

# Process the directory for normal output
process_directory(input_normal_dir, output_normal_dir)

# Process the directory for round output with input from round directory
process_directory(input_round_dir, output_round_dir, is_round=True)