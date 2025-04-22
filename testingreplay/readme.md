# Testing Replay

This repository contains a script to record and replay mouse and keyboard events using Python.

## How to use

1. Install the required libraries by running `pip install -r requirements.txt`
2. Run the script by executing `python testingreplay.py`
3. Press F9 to start recording, and F9 again to stop recording
4. Press F8 to replay the recorded events
5. Press Esc to exit the script

## Features

* Record and replay mouse and keyboard events
* Supports absolute and relative mouse coordinates
* Supports saving and loading recordings to/from a file

## Known issues

* The script does not handle events that occur while the script is not in focus (e.g. if you switch to another window while recording)
* The script does not handle events that occur while the script is minimized
* The script does not handle events that occur while the script is running on a different desktop or virtual machine

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

This project uses the following libraries:

* pynput: A Python library for monitoring input devices
* pyautogui: A Python library for controlling the mouse and keyboard
* pickle: A Python library for serializing and deserializing data

Please report any issues or feature requests to the Issues page.
