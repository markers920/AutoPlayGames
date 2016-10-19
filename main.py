
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
    
    image = autopy.bitmap.capture_screen()
    get_rgb(image, 10, 10)
#END def main():
###############################################################################

def get_rgb(image, x, y):
    color = image.get_color(x, y)
    color = autopy.color.hex_to_rgb(color)
    color = [c/256.0 for c in color]
    print color
#END def get_color():


###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
    