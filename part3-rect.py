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

def draw_rectangle(gyro_sensor):
    ''' Draw a rectangle upon the driving surface by moving the robot in a rectangle pattern'''
    tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)
    tank_drive.gyro = gyro_sensor
    
    for _ in range(4):
        # drive staright for 5 rotations of the outer motor
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 5)
        # turn 90 degrees to the right
        # if this doesn't give good results we might want to use the tank_drive.turn_degrees method instead?
        target_angle = gyro_sensor.angle + 90
        while gyro_sensor.angle < target_angle:
            tank_drive.on(SpeedPercent(10), SpeedPercent(-10))
        tank_drive.off()



def main():
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!, I am a rectangle drawing robot')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code! I am a rectangle drawing robot')

    # calibrate the gyro sensor
    gyro_sensor = GyroSensor(INPUT_3)
    gyro_sensor.calibrate()

    # draw a rectangle
    draw_rectangle(gyro_sensor)


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(2)

if __name__ == '__main__':
    main()
