import os

def get_all_files(root_folder):
    file_list = []
    # Files to ignore (hidden or system files)
    ignore_list = {'.DS_Store', 'desktop.ini', 'thumbs.db'}

    for root, dirs, files in os.walk(root_folder):
        for f in files:
            # Filter out hidden files and system trash
            if not f.startswith('.') and f not in ignore_list:
                # Get the full path so you know exactly WHERE the file is
                full_path = os.path.join(root, f)
                file_list.append(full_path)
                
    return file_list

# --- Execution ---
path = "C:\Backup 11-08-2021\Data_Old"  # Replace with your actual path
found_files = get_all_files(path)

if found_files:
    print(f"Total files found: {len(found_files)}")
    print("-" * 30)
    for file_path in found_files:
        print(file_path)
else:
    print("The folder and its subfolders are empty (or only contain hidden system files).")