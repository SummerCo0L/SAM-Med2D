import os
import json

# Define source directories
images_dir = r'\images'
masks_dir = r'\masks'

# Create a dictionary to hold image-to-mask mappings
image_to_masks = {}

# Iterate over all image files in the images directory
for image_file in os.listdir(images_dir):
    if image_file.endswith('.png'):  # Only consider PNG files
        # Extract the numeric prefix from the filename
        prefix = image_file.split('_')[0]

        # Check if the prefix is numeric and within the desired range
        if prefix.isdigit() and 1 <= int(prefix) <= 40:
            # Create the image and mask paths with forward slashes
            image_path = f"data_demo/images/{image_file}"
            mask_path = f"data_demo/masks/{image_file}"
            
            # Check if the corresponding mask exists
            if os.path.exists(os.path.join(masks_dir, image_file)):
                # Add entry without square brackets for single mask
                image_to_masks[image_path] = mask_path

# Write the dictionary to a JSON file
json_file_path = r'\image2label_train.json'
with open(json_file_path, 'w') as json_file:
    json.dump(image_to_masks, json_file, indent=4)

print(f'Generated {json_file_path} with {len(image_to_masks)} entries.')

