import os
import shutil

def change_extension_recursive(directory, old_ext, new_ext):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(old_ext):
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, filename.rsplit('.', 1)[0] + '.' + new_ext)
                shutil.move(old_file_path, new_file_path)
                print(f"Changed extension of '{filename}' to '{new_ext}'")

# Example usage:
directory_path = '/path/to/your/directory'
old_extension = 'txt'  # Replace with the current extension you want to change
new_extension = 'csv'  # Replace with the new extension

change_extension_recursive(directory_path, old_extension, new_extension)
