#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import time
from ev3dev2.motor import *
#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

# TODO: Add code here



# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)






def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!, I am a dead reckoning robot')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code! I am a dead reckoning robot')

    # initilize a 3x3 grid array of integers that represent instructions for left and right motor speeds and durations of time

    # initialize the tank drive object and calibrate the gyro sensor

    # for each row in the grid array

        # get index one and set left motor to that speed
        # get index 2 and set right motor to that speed
        # get index 3 and set the duration of time to drive
        # execute drive command
        # next loop
    
    # stop both motors
    # get gyro sensor reading and print it to the screen

    # somehow compute the location? as a distance from it's origin point?


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(2)

if __name__ == '__main__':
    main()
