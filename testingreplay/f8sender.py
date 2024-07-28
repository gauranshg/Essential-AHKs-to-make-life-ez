import pyautogui
import time

def press_f8_every_minute(n,t):
    for _ in range(n):
        pyautogui.press('f8')
        time.sleep(t)  # Wait for 60 seconds (1 minute)

if __name__ == "__main__":
    n = int(input("Enter the number of times to press F8: "))
    t = int(input("Enter the time gap of times in seconds "))
    time.sleep(10)
    press_f8_every_minute(n,t)
