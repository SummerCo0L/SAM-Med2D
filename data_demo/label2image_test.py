import os
import json

# Define source directories
images_dir = r'\images'
masks_dir = r'\masks'

# Create a dictionary to hold mask-to-image mappings
label_to_images = {}

# Iterate over all validation files in the masks directory
for mask_file in os.listdir(masks_dir):
    if mask_file.endswith('.png'):  # Only consider PNG files
        # Extract the numeric prefix from the filename
        prefix = mask_file.split('_')[0]

        # Check if the prefix is numeric and within the desired range
        try:
            prefix_int = int(''.join(filter(str.isdigit, prefix)))
            print(prefix_int)
            if 41 <= prefix_int <= 50:
                # Create the mask and image paths with forward slashes
                mask_path = f"data_demo/masks/{mask_file}"
                image_path = f"data_demo/images/{mask_file}"
            
            # Check if the corresponding image exists
                if os.path.exists(os.path.join(images_dir, mask_file)):
                    # Add entry without square brackets for single image
                    label_to_images[mask_path] = image_path
        except ValueError:
            # Skip if the prefix cannot be converted to an integer
            continue

# Write the dictionary to a JSON file
json_file_path = r'\label2image_train.json'
with open(json_file_path, 'w') as json_file:
    json.dump(label_to_images, json_file, indent=4)

print(f'Generated {json_file_path} with {len(label_to_images)} entries.')
