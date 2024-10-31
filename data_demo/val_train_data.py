import os
import shutil

# Source and destination directories
source_dir = r'C:\Users\mingy\Desktop\SMU\CS701\Project\Public_leaderboard_data\val_images'
dest_dir = r'C:\Users\mingy\Desktop\SMU\CS701\PROJECT\PUBLIC_LEADERBOARD_DATA\data_demo\images'

# Create the destination directory if it does not exist
os.makedirs(dest_dir, exist_ok=True)

# Traverse the source directory
for subdir, _, files in os.walk(source_dir):
    # Get the subfolder name (e.g., '01', '02', etc.)
    subfolder_name = os.path.basename(subdir)
    
    for file in files:
        if file.endswith('.png'):  # Adjust the file extension as needed
            # Construct full file paths
            source_image_path = os.path.join(subdir, file)
            
            # Remove the file extension from the original file name
            file_name_without_extension = os.path.splitext(file)[0]
            # Construct the new filename with subfolder name
            new_filename = f'{subfolder_name}_{file_name_without_extension}.png'
            destination_image_path = os.path.join(dest_dir, new_filename)
            
            # Copy the image file to the destination directory
            shutil.copy(source_image_path, destination_image_path)
            print(f'Copied: {source_image_path} to {destination_image_path}')
