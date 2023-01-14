import pyautogui
import keyboard
from time import sleep


def screenshot(file):
    keyboard.press("alt+tab")
    sleep(0.1)
    keyboard.press("left")
    keyboard.release("left")
    keyboard.press("left")
    keyboard.release("left")
    keyboard.release("alt+tab")
    sleep(0.1)
    pyautogui.screenshot(file)


if __name__ == "__main__":
    screenshot("screenshot.png")
