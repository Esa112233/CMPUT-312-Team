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


def draw_circle():
    ''' Draw a circle on the driving surface, stop after completing one complete circle'''

    # Initialize the tank drive object and calibrate the gyro sensor
    tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
    tank_drive.gyro = GyroSensor(INPUT_3)
    tank_drive.gyro.calibrate()
    
    # Drive in a circle
    tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(4), 360)



def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!, I am a circle drawing robot')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code! I am a circle drawing robot')

    # draw a line
    draw_circle()


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(2)

if __name__ == '__main__':
    main()
