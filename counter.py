
import keyboard
import pyautogui

number = 40124

def send_number():
    global number

    pyautogui.write(str(number))
    number += 2

print("Counter running! Press / to type the next number.")
print("Press Ctrl+C in the terminal to stop.")

keyboard.add_hotkey('/', send_number, suppress=True)

keyboard.wait()
