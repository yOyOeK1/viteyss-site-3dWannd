from pynput.keyboard import Key, Controller

keyboard = Controller()
with keyboard.pressed(Key.ctrl):
   keyboard.press(Key.f4)
   keyboard.release(Key.f4)