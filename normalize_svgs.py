import os
import re

# Directory paths
input_dir = "input_vectors/normal"
normalized_dir = "input_vectors/normalized"

def normalize_svg(svg_content):
    # Ensure SVG has Layer 1 and Layer 2 structure
    if not re.search(r'data-name="Layer 1"', svg_content):
        svg_content = re.sub(r'(<svg[^>]*>)', r'\1<g data-name="Layer 1">', svg_content)
        svg_content = re.sub(r'(</svg>)', r'</g>\1', svg_content)
    
    if not re.search(r'data-name="Layer 2"', svg_content):
        svg_content = re.sub(r'(<g data-name="Layer 1">)', r'\1<g data-name="Layer 2">', svg_content)
        svg_content = re.sub(r'(</g></svg>)', r'</g>\1', svg_content)
    
    return svg_content

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.svg'):
                svg_path = os.path.join(root, file)
                relative_path = os.path.relpath(svg_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Normalize the SVG content
                with open(svg_path, 'r') as file:
                    svg_content = file.read()
                normalized_content = normalize_svg(svg_content)
                
                # Write the normalized SVG content to the new file in the output directory
                with open(output_path, 'w') as file:
                    file.write(normalized_content)
                print(f"Normalized {svg_path} -> {output_path}")

# Process the directory for normalization
process_directory(input_dir, normalized_dir)