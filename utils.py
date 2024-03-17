# utils.py

import os
import shutil

def backup_files(source_dir, dest_dir):
    """Backup files from source directory to destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, os.path.relpath(src_file, source_dir))
            dest_path = os.path.dirname(dest_file)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            shutil.copy2(src_file, dest_file)
