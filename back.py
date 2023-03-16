import os

# Set the paths of the source and destination folders
source_folder = r"C:\Users\dower\OneDrive\____TE Meats____"
destination_folder = r"C:\Users\dower\OneDrive\_TE_MEATS_BACUP"

# Loop through each file in the source folder
for filename in os.listdir(source_folder):
    # Create the full path to the file in the source folder
    source_file_path = os.path.join(source_folder, filename)
    
    # Create the full path to the file in the destination folder
    destination_file_path = os.path.join(destination_folder, filename)
    
    # Copy the file from the source folder to the destination folder
    shutil.copy(source_file_path, destination_file_path)
