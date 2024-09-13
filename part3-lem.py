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


def draw_lemniscate():
    ''' Draw a lemniscate (figure-eight) pattern on the driving surface '''

    # Initialize the tank drive object and calibrate the gyro sensor
    tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
    tank_drive.gyro = GyroSensor(INPUT_3)
    tank_drive.gyro.calibrate()
    
    # Define the number of rotations for moving forward
    rotations = 2  # Adjust this value based on the radius of the lemniscates circles once we ficure out how big they will be.
    
    # Move forward using the defined number of rotations
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 3.51)
    
    # Turn 270 degrees to the right, with both tires at speeds >=0
    tank_drive.on_for_degrees(SpeedPercent(4), SpeedPercent(10), 270)
    
    # Move forward using the defined number of rotations to return to the origin
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 3.51)
    
    # Move forward using the defined number of rotations again
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 3.51)
    
    # Turn 270 degrees to the left, with both tires at speeds >=0
    tank_drive.on_for_degrees(SpeedPercent(10), SpeedPercent(4), 0)

    # Move forward using the defined number of rotations to return to the origin
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), 3.51)



def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!, I am a lemniscate drawing robot')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code! I am a lemniscate drawing robot')

    # draw a lemniscate
    draw_lemniscate()


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(2)

if __name__ == '__main__':
    main()
