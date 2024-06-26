import keyboard  # Install using: pip install keyboard
import pyperclip  # Install using: pip install pyperclip
import re
import os
import tkinter as tk

def sanitize_filename(filename):
    """
    Sanitize a filename by replacing unsupported characters with underscores.
    
    Args:
    - filename (str): The original filename to sanitize.
    
    Returns:
    - str: The sanitized filename.
    """
    # Define unsupported characters
    unsupported_chars = '/\\?%*:|"<>!$'

    # Replace unsupported characters with underscores
    for char in unsupported_chars:
        filename = filename.replace(char, '_')

    return filename

# Function to fetch class name from clipboard C# code
def fetch_class_name_from_clipboard(patterns):
    # Fetch code from clipboard
    code_content = pyperclip.paste().strip()
    
    # Define a regex pattern to find class declarations
    #pattern = r'strategy\("([^"]+)"'
    
    # Search for the pattern in the code content
    for pattern in patterns:
        match = re.search(pattern, code_content)
    
        if match:
            class_name = match.group(1)
            return class_name
    return None  # Return None if no class name is found

# Function to save text to a file
def save_to_file(folder_path, class_name, code_content):
    class_name = sanitize_filename(class_name)
    file_path = os.path.join(folder_path, class_name + '.txt')
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(code_content)
    print(f"Saved '{class_name}.txt' to {folder_path}")

    # Create and configure tooltip window
    tooltip = tk.Tk()
    tooltip.overrideredirect(True)  # Remove window decorations (border, title bar)
    tooltip.attributes('-topmost', True)  # Keep tooltip window on top
    tooltip.geometry(f"+{tooltip.winfo_screenwidth()}+{tooltip.winfo_screenheight()}")  # Move off-screen

    # Calculate tooltip position near the cursor
    mouse_x, mouse_y = tooltip.winfo_pointerxy()
    tooltip_x = mouse_x + 20
    tooltip_y = mouse_y + 20
    tooltip.geometry(f"+{tooltip_x}+{tooltip_y}")

    # Tooltip label
    tooltip_label = tk.Label(tooltip, text=f"Saved '{class_name}.txt' to {folder_path}", bg='white', padx=10, pady=5, borderwidth=1, relief='solid')
    tooltip_label.pack()

    # Close tooltip after 5 seconds
    tooltip.after(5000, tooltip.destroy)

    # Display tooltip
    tooltip.mainloop()

# Main function to listen for F9 key press
def main():
    folder_path_s = r'C:\Users\gaura\Documents\Coding\PineCodes\Temp\Strategy'  # Replace with your desired folder path
    folder_path_i = r'C:\Users\gaura\Documents\Coding\PineCodes\Temp\Indicators'
    print("Press F9 to save the code from clipboard to a file. Press 'Esc' to exit.")
    patterns = [r'strategy\("([^"]+)"',r"strategy\(\s*'([^']+)'"]
    patterni = [r'indicator\("([^"]+)"', r"indicator\(\s*'([^']+)'"]
    while True:
        # Listen for F9 key press
        if keyboard.is_pressed('F9'):
            # Fetch class name from clipboard
            strategy = fetch_class_name_from_clipboard(patterns)
            indicator = fetch_class_name_from_clipboard(patterni)
            if strategy:
                print(f"Class name found: {strategy}")
                # Fetch code from clipboard
                code_content = pyperclip.paste().strip()
                save_to_file(folder_path_s, strategy, code_content)
            else:
                if indicator:
                    print(f"Class name found: {indicator}")
                    # Fetch code from clipboard
                    code_content = pyperclip.paste().strip()
                    save_to_file(folder_path_i, indicator, code_content)
                else:
                    print("No class name found in the clipboard content.")

        # Exit loop if Esc key is pressed
        if keyboard.is_pressed('Esc'):
            break

if __name__ == "__main__":
    main()
