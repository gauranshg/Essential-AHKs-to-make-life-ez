import keyboard
import pyperclip
import os

selected_file_name = None
selected_file_contents = None

def on_key_event(event):
    global selected_file_name, selected_file_contents

    # Listen for Ctrl + F5 (to copy file path)
    if event.name == 'f5' and keyboard.is_pressed('ctrl'):
        #keyboard.wait('ctrl')  # Wait for both keys to be released
            # Simulate Ctrl + Shift + C (copy file path in Windows)
        #keyboard.press_and_release('ctrl+shift+c')
        # Get file path from clipboard
        #keyboard.press_and_release('ctrl+shift+c')
        selected_file_name = pyperclip.paste().strip()
        selected_file_name = selected_file_name.replace('"','')
        print(f"Selected file path: {selected_file_name}")
        if selected_file_name.lower().endswith('.txt'):
            
            with open(selected_file_name, 'r') as file:
                selected_file_contents = file.read()
            print(f"File contents:\n{selected_file_contents}")
            selected_file_name = os.path.basename(selected_file_name).split('.')[0]
            print(selected_file_name)
        else:
            selected_file_contents = None
            print("Selected file is not a .txt file.")

    # Listen for Ctrl + F6 (to paste file name)
    elif event.name == 'f6' and keyboard.is_pressed('ctrl'):
 # Wait for both keys to be released
        if selected_file_name:
            pyperclip.copy(selected_file_name)
            #keyboard.press_and_release('ctrl+v')
            #keyboard.write(selected_file_name)

    # Listen for Ctrl + F7 (to paste file contents)
    elif event.name == 'f7' and keyboard.is_pressed('ctrl'):
 # Wait for both keys to be released
        if selected_file_contents:
            pyperclip.copy(selected_file_contents)
            #keyboard.press_and_release('ctrl+v')
            #keyboard.write(selected_file_contents)
# Register the callback function
keyboard.on_release(on_key_event)

# Keep the script running until user presses 'q'q
print("Press Ctrl + F5 to select a file and copy its path.")
print("Press Ctrl + F6 to paste the file name.")
print("Press Ctrl + F7 to paste the file contents.")
print("Press 'q' to quit.")

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('q'):
        break

# Clean up - unhook the keyboard listener
keyboard.unhook_all()
