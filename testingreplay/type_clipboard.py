import pyperclip
import pyautogui
import keyboard
import threading
import time

def type_clipboard_contents(stop_event):
    # Add a small delay before starting to type
    time.sleep(1)  # 1 second delay

    # Get the current contents of the clipboard
    clipboard_content = pyperclip.paste()
    
    # Type out the clipboard contents
    for char in clipboard_content:
        if stop_event.is_set():
            break
        pyautogui.typewrite(char)

def main():
    print("Press Alt + Ctrl + V to type clipboard contents. Press Esc to exit.")
    
    stop_event = threading.Event()
    
    def on_exit():
        print("Exiting...")
        stop_event.set()
    
    # Register the hotkey for typing clipboard contents
    keyboard.add_hotkey('alt+ctrl+v', lambda: threading.Thread(target=type_clipboard_contents, args=(stop_event,)).start())
    
    # Register the hotkey for exiting the program
    keyboard.add_hotkey('esc', on_exit)
    
    # Wait until the stop event is set
    stop_event.wait()

if __name__ == "__main__":
    main()
