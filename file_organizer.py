import os
import shutil

source_folder = "D:\CloudAIEngg\projects\sample_files"

folders = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):

        _, extension = os.path.splitext(file_name)

        for folder_name, extensions in folders.items():

            if extension.lower() in extensions:

                destination_folder = os.path.join(source_folder, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file_name)
                )

                print(f"Moved {file_name} -> {folder_name}")