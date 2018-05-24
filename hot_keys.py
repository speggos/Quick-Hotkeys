import keyboard
from time import sleep

hotkeys = {
    "command+j": "Example Hotkey Pressed!",
}

def main():

    for hotkey, text in hotkeys.items():
        keyboard.add_hotkey(hotkey, keyboard.write, args=[text])

    keyboard.add_hotkey("command+l", list_hotkeys)

    while True:
        sleep(42)

def list_hotkeys():

    for hotkey, text in hotkeys.items():
        keyboard.write("Hotkey: " + hotkey + ", Text: " + text)

if __name__=="__main__":
    main()