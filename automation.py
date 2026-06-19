import os
import shutil
import logging

# Set up automatic operations logging
logging.basicConfig(
    filename='file_cleanup.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organize_folder():
    print("\n--- Python File Automation Tool ---")
    target_dir = input("Enter the full path of the folder to clean up: ").strip()

    if not os.path.exists(target_dir):
        print(f"Error: The path '{target_dir}' does not exist.")
        return

    extension_map = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Media': ['.mp3', '.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.tar', '.gz']
    }

    try:
        files = os.listdir(target_dir)
        moved_count = 0

        for file in files:
            file_path = os.path.join(target_dir, file)
            if os.path.isdir(file_path) or file == 'file_cleanup.log':
                continue
                
            _, ext = os.path.splitext(file.lower())
            target_folder_name = "Others"
            
            for folder, extensions in extension_map.items():
                if ext in extensions:
                    target_folder_name = folder
                    break
            
            destination_dir = os.path.join(target_dir, target_folder_name)
            os.makedirs(destination_dir, exist_ok=True)
            
            shutil.move(file_path, os.path.join(destination_dir, file))
            logging.info(f"Moved: '{file}' -> To: '{target_folder_name}'")
            moved_count += 1

        print(f"Cleanup finished! Successfully organized {moved_count} files.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    organize_folder()