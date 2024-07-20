import keyboard  # Install using: pip install keyboard
import pyperclip  # Install using: pip install pyperclip
import re
import os
import time
from ctypes import windll, Structure, c_long, byref

# Define a structure for the POINT structure
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

# Function to fetch class name from clipboard C# code
def fetch_class_name_from_clipboard():
    # Fetch code from clipboard
    code_content = pyperclip.paste().strip()
    
    # Define a regex pattern to find class declarations
    pattern = r'class\s+(\w+)\s*{'
    
    # Search for the pattern in the code content
    match = re.search(pattern, code_content)
    
    if match:
        class_name = match.group(1)
        return class_name
    else:
        return None  # Return None if no class name is found

# Function to save text to a file
def save_to_file(folder_path, class_name, code_content):
    file_path = os.path.join(folder_path, class_name + '.txt')
    with open(file_path, 'w') as file:
        file.write(code_content)
    print_with_tooltip(f"Saved '{class_name}.txt' to {folder_path}")

# Function to display a tooltip near the cursor
def print_with_tooltip(message):
    # Get the current cursor position
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))

    # Display the message as a tooltip
    windll.user32.SetWindowTextA(None, message)
    windll.user32.SendMessageA(None, 0x0200, pt.x, pt.y)

    # Wait for 3 seconds
    time.sleep(3)

    # Clear the tooltip
    windll.user32.SendMessageA(None, 0x0200, 0, 0)

# Main function to listen for F9 key press
def main():
    folder_path = r'D:\JSON'  # Replace with your desired folder path

    print_with_tooltip("Press F9 to save the code from clipboard to a file. Press 'Esc' to exit.")

    while True:
        # Listen for F9 key press
        if keyboard.is_pressed('F9'):
            # Fetch class name from clipboard
            class_name = fetch_class_name_from_clipboard()
            if class_name:
                print_with_tooltip(f"Class name found: {class_name}")
                # Fetch code from clipboard
                code_content = pyperclip.paste().strip()
                save_to_file(folder_path, class_name, code_content)
            else:
                print_with_tooltip("No class name found in the clipboard content.")

        # Exit loop if Esc key is pressed
        if keyboard.is_pressed('Esc'):
            break

if __name__ == "__main__":
    main()