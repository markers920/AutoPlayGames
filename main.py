
#   http://www.autopy.org/
#   https://pypi.python.org/pypi/autopy
import autopy

import time
import random
import math
import numpy

###############################################################################
def main():
    #autopy.alert.alert("Hello, world")             #alert box
    #autopy.mouse.move(1, 1)                        #move mouse
    #autopy.bitmap.capture_screen()                 #capture screen
    #hex(autopy.bitmap.capture_screen().get_color(1, 1)) #get capture color
    
    MAX_CAPTURE_INDEX = 1000
    CAPTURE_SLEEP_TIME = 1.0
    
    for capture_index in range(MAX_CAPTURE_INDEX):
        image = autopy.bitmap.capture_screen()
        rgb = get_rgb(image, 300, 300)
        print capture_index, float(capture_index)/MAX_CAPTURE_INDEX, rgb
        time.sleep(CAPTURE_SLEEP_TIME)
#END def main():
###############################################################################

def get_rgb(image, x, y):
    color = image.get_color(x, y)
    color = autopy.color.hex_to_rgb(color)
    color = [c/256.0 for c in color]
    return color
#END def get_color():


###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
    