import os

def get_folder_storage(root_folder):
    total_size = 0
    file_count = 0
    ignore_list = {'.DS_Store', 'desktop.ini', 'thumbs.db'}

    for root, dirs, files in os.walk(root_folder):
        for f in files:
            if not f.startswith('.') and f not in ignore_list:
                fp = os.path.join(root, f)
                # skip if it is a symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
                    file_count += 1
                    
    return total_size, file_count

def format_size(bytes):
    """Converts bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

# --- Execution ---
path = r"C:\\Users\\Hp\\Desktop\\My Music"

if os.path.exists(path):
    size_in_bytes, count = get_folder_storage(path)
    print(f"Analysis for: {os.path.abspath(path)}")
    print(f"Total Files: {count}")
    print(f"Total Storage: {format_size(size_in_bytes)}")
else:
    print("Path does not exist.")