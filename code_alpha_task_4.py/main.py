import os     #helps work with folder and files
import shutil     #helps us to move file from one folder to another folder
source_folder = "source"
destination_folder = "destination"

files = os.listdir(source_folder)

for file in files:
    if file.endswith(".jgp"):
        shutil.move( os.path.join(source_folder, file),
    destination_folder)