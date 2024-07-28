from pynput import mouse, keyboard
import time
import threading
import pickle
import os

# Lists to store the events
mouse_events = []
keyboard_events = []

recording = False
replaying = False
use_absolute_coordinates = True  # Set to True for absolute coordinates, False for relative
recording_file = "stock.pkl"  # File to save/load recordings

# Record mouse events
def on_click(x, y, button, pressed):
    if recording:
        mouse_events.append(('click', x, y, button, pressed, time.time()))

def on_move(x, y):
    if recording:
        mouse_events.append(('move', x, y, time.time()))

def on_scroll(x, y, dx, dy):
    if recording:
        mouse_events.append(('scroll', x, y, dx, dy, time.time()))

# Record keyboard events
def on_press(key):
    if recording and key != keyboard.Key.f9:
        keyboard_events.append(('press', key, time.time()))

def on_release(key):
    global recording, replaying
    if key == keyboard.Key.f9:
        recording = not recording
        if recording:
            print("Started recording.")
        else:
            print("Stopped recording.")
            save_recording()
    elif key == keyboard.Key.f8 and not recording:
        if not replaying:
            replaying = True
            print("Replaying now.")
            replay_thread = threading.Thread(target=replay_events)
            replay_thread.start()
    elif key == keyboard.Key.esc:
        print("Exiting...")
        stop_listeners()
        exit(0)
    if recording and key != keyboard.Key.f9:
        keyboard_events.append(('release', key, time.time()))

# Replay the recorded events
def replay_events():
    global replaying
    if not load_recording():
        print("No events recorded to replay.")
        replaying = False
        return

    # Combine and sort events by time
    all_events = sorted(mouse_events + keyboard_events, key=lambda event: event[-1])
    start_time = all_events[0][-1]

    for event in all_events:
        if not replaying:
            break
        event_type = event[0]
        event_time = event[-1]
        time_to_sleep = event_time - start_time
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
        start_time = event_time
        
        if event_type == 'click':
            _, x, y, button, pressed, _ = event
            if use_absolute_coordinates:
                mouse_controller.position = (x, y)
            if pressed:
                mouse_controller.press(button)
            else:
                mouse_controller.release(button)
        elif event_type == 'move':
            _, x, y, _ = event
            if use_absolute_coordinates:
                mouse_controller.position = (x, y)
            else:
                mouse_controller.move(x - mouse_controller.position[0], y - mouse_controller.position[1])
        elif event_type == 'scroll':
            _, x, y, dx, dy, _ = event
            if use_absolute_coordinates:
                mouse_controller.position = (x, y)
            mouse_controller.scroll(dx, dy)
        elif event_type == 'press':
            _, key, _ = event
            keyboard_controller.press(key)
        elif event_type == 'release':
            _, key, _ = event
            keyboard_controller.release(key)

    replaying = False
    print("Replay completed.")

# Save the recorded events to a file
def save_recording():
    with open(recording_file, 'wb') as f:
        pickle.dump((mouse_events, keyboard_events), f)
    print(f"Recording saved to {recording_file}")

# Load the recorded events from a file
def load_recording():
    global mouse_events, keyboard_events
    if os.path.exists(recording_file):
        with open(recording_file, 'rb') as f:
            mouse_events, keyboard_events = pickle.load(f)
        return True
    return False

# Stop listeners
def stop_listeners():
    mouse_listener.stop()
    keyboard_listener.stop()

# Set up the mouse and keyboard listeners
mouse_listener = mouse.Listener(
    on_click=on_click,
    on_move=on_move,
    on_scroll=on_scroll
)

keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Start the listeners
mouse_listener.start()
keyboard_listener.start()

print("Press F9 to start/stop recording, F8 to replay the events, and Esc to exit.")

# Keep the script running
mouse_listener.join()
keyboard_listener.join()
