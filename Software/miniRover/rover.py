"""
Core rover script for user I/O on the roverPi
this is a top-level init/process control file, all processes should be separate and executed here.
Authors: Alexander Olds,
"""

# Package Imports
import sys

import pygame

# Local Imports
from drivetrain import *
from sensors import *

if __name__ == '__main__':

    import board
    import busio
    import adafruit_pca9685

    # Initialization

    print("Initializing Pygame...", end='')
    pygame.joystick.init()
    print("Done")

    print("Initializing Sensors...", end='')
    sensors = Sensors()
    print("Done")

    print("Initializing Drivetrain...", end='')
    i2c = busio.I2C(board.SCL, board.SDA)
    pwm = adafruit_pca9685.PCA9685(i2c)
    pwm.frequency = 50

    frontLeft = pwm.channels[LF_PORT]
    centerLeft = pwm.channels[LC_PORT]
    rearLeft = pwm.channels[LR_PORT]

    frontRight = pwm.channels[RF_PORT]
    centerRight = pwm.channels[RC_PORT]
    rearRight = pwm.channels[RR_PORT]

    print("Done")

    print("Initializing Controllers...", end='')

    controller = 0
    try:
        controller = pygame.joystick.Joystick(0)
        controller.init()
        controller_connected = 1

    except KeyboardInterrupt:  # TODO: figure out what exception is thrown when there's no controller connected
        controller_connected = -1

    if controller_connected > 0:
        print("Done")
        print("Connected to" + controller.get_name())
    else:
        print("failed!")
        print("Controller not connected")

    print("Initialization Complete")

    # Main control loop
    while True:
        try:
            sensors.uplink()

            # update & pull controller inputs
            if controller_connected > 0:
                pygame.event.pump()

                # send inputs to drive
                throttle = (controller.getAxis(
                    0) * 0x0667) + 0x1333  # 0x1333 center, 0x0ccc full reverse, 0x1999  full forward
                turn = controller.getAxis(1)  # TODO: servo encoding
            else:
                throttle = 0x000
                turn = 0x000

            frontLeft.duty_cycle = throttle
            centerLeft.duty_cycle = throttle
            rearLeft.duty_cycle = throttle

            frontRight.duty_cycle = throttle
            centerRight.duty_cycle = throttle
            rearRight.duty_cycle = throttle

            # TODO: Servo control

        except KeyboardInterrupt:
            frontLeft.duty_cycle = 0x0000
            centerLeft.duty_cycle = 0x0000
            rearLeft.duty_cycle = 0x0000

            frontRight.duty_cycle = 0x0000
            centerRight.duty_cycle = 0x0000
            rearRight.duty_cycle = 0x0000

            print('\n')
            print("Program Terminated by User")
            sys.exit()
