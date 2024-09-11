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


def draw_line():
    ''' Draw a straight line on the driving surface, correcting steering as it goes '''

    # Initialize the tank drive object and calibrate the gyro sensor
    tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
    tank_drive.gyro = GyroSensor(INPUT_3)
    tank_drive.gyro.calibrate()
    
    # while rotations is less than variable_1(some distance we want it to drive)
        # get current gyro output and multiply it by (-10)
        # if gyro output is less than 0, then adjust speed of left motor by gyro output
        # else adjust speed of right motor by gyro output
    # exit while loop
    # stop both motors



def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!, I am a line drawing robot')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code! I am a line drawing robot')

    # draw a line
    draw_line()


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(2)

if __name__ == '__main__':
    main()
