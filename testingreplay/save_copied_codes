import keyboard  # Install using: pip install keyboard
import pyperclip  # Install using: pip install pyperclip
import re
import os


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
    print(f"Saved '{class_name}.txt' to {folder_path}")

    # Get current mouse position


# Main function to listen for F9 key press
def main():
    folder_path = r'D:\JSON'  # Replace with your desired folder path

    print("Press F9 to save the code from clipboard to a file. Press 'Esc' to exit.")

    while True:
        # Listen for F9 key press
        if keyboard.is_pressed('F9'):
            # Fetch class name from clipboard
            class_name = fetch_class_name_from_clipboard()
            if class_name:
                print(f"Class name found: {class_name}")
                # Fetch code from clipboard
                code_content = pyperclip.paste().strip()
                save_to_file(folder_path, class_name, code_content)
            else:
                print("No class name found in the clipboard content.")

        # Exit loop if Esc key is pressed
        if keyboard.is_pressed('Esc'):
            break

if __name__ == "__main__":
    main()
