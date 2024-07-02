import os
import cairosvg
from bs4 import BeautifulSoup

# object_list from the provided object_list.py
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

# Function to get color for a given object name
def get_color(object_name):
    for obj in objects:
        if obj["object"] == object_name:
            return obj["colour_rgb"]
    return "0,0,0"  # Default color if not found

# Function to process SVG and change color
def process_svg(input_path, output_path, color_rgb):
    with open(input_path, 'r') as file:
        svg_content = file.read()

    soup = BeautifulSoup(svg_content, 'xml')
    styles = soup.find_all("style")

    for style in styles:
        style.string = style.string.replace('fill:none;', f'fill:rgb({color_rgb});')

    with open(output_path, 'w') as file:
        file.write(str(soup))

    cairosvg.svg2png(url=output_path, write_to=output_path.replace('.svg', '.png'), output_width=1200, output_height=1200)

# Directories to process
directories = ['normal', 'round']

for directory in directories:
    for root, _, files in os.walk(f'vectors/{directory}'):
        for file in files:
            if file.endswith('.svg'):
                object_name = file.replace('.svg', '')
                color_rgb = get_color(object_name)
                input_path = os.path.join(root, file)
                output_path = os.path.join(root, file)
                process_svg(input_path, output_path, color_rgb)

print("SVG to PNG conversion complete.")
