import os
import shutil

from_dir = "/Users/staples/Downloads"
to_dir = "/Users/staples/Documents/WhiteHatJr/Module3/Projects/Project102"

list_of_files = os.listdir(from_dir)
print("List of Files:")
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if not extension:
        continue

    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        # Create directory paths
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", file_name)
        
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
            # Create the destination directory
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
