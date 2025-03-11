import os
import shutil

def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

def move_file(src, dest_dir):
    ensure_directory(dest_dir)
    dest_file = os.path.join(dest_dir, os.path.basename(src))
    if os.path.exists(dest_file):
        os.remove(dest_file)
        print(f"Removed existing file '{dest_file}'")
    if os.path.exists(src):
        shutil.move(src, dest_dir)
        print(f"Moved '{src}' to '{dest_dir}'")
    else:
        print(f"File '{src}' does not exist.")

# Define source files and target directories
files_to_move = {
    'index.html': '/mnt/c/Projects/playground/lovable_clone/files/public',
    'scripts.js': '/mnt/c/Projects/playground/lovable_clone/files/public',
    'styles.css': '/mnt/c/Projects/playground/lovable_clone/files/public',
    'server.js': '/mnt/c/Projects/playground/lovable_clone/files'
}

# Move files
for file_name, target_dir in files_to_move.items():
    move_file(file_name, target_dir)
