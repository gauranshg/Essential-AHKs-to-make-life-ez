import keyboard
import time
import pyperclip

file_name = ""
file_contents = ""

def send_ctrl_shift_c():
    # Simulate Ctrl + Shift + C press
    keyboard.press('ctrl')
    keyboard.press('shift')
    keyboard.press('c')
    time.sleep(1)  # Optional: Adjust as needed to ensure the keys are held long enough
    keyboard.release('c')
    keyboard.release('shift')
    keyboard.release('ctrl')

def on_key_event(event):
    global file_name, file_contents, file_path

    # Check if Ctrl + F5 is pressed
    if event.name == 'f5' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
        # Send Ctrl + Shift + C event (copy action)
        send_ctrl_shift_c()

        clipboard_content = pyperclip.paste().strip()
        if clipboard_content.endswith('.txt'):
            file_path = clipboard_content
        try:
            with open(file_path, 'r') as file:
                file_name = file.name
                file_contents = file.read()
                print(f'Read file: {file_name}')
        except Exception as e:
            print(f'Error reading file: {e}')

    # Check if Ctrl + F6 is pressed
    elif event.name == 'f6' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
        # Paste the file name
        keyboard.write(file_name)

    # Check if Ctrl + F7 is pressed
    elif event.name == 'f7' and event.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl'):
        # Paste the file contents
        keyboard.write(file_contents)

# Hook to keyboard events
keyboard.hook(on_key_event)

print("Press Ctrl + F5 to read the text file and copy it.")
print("Press Ctrl + F6 to paste the file name.")
print("Press Ctrl + F7 to paste the file contents.")
print("Press 'Ctrl + C' to stop the program.")

# Keep the script running
keyboard.wait('ctrl+c')

# Clean up hook (optional)
keyboard.unhook_all()
