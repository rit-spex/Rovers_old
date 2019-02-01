"""
Core rover script for user I/O on the roverPi
this is a top-level init/process control file, all processes should be separate and executed here.
Authors: Alexander Olds,
"""

# Package Imports
import pygame

# Local Imports
# rom drivetrain import *
from sensors import *

if __name__ == '__main__':
    # Initialization

    print("Initializing Pygame...", end='')
    pygame.joystick.init()
    print("Done")

    print("Initializing Sensors...", end='')
    sensors = Sensors()
    print("Done")

    print("Initializing Drivetrain...", end='')
    # drive = drivetrain()
    print("Done")

    print("Initializing Controllers...", end='')
    # controller = pygame.joystick.Joystick(0)
    #controller.init()
    print("Done")

    #print("Connected to" + controller.get_name())

    print("Initialization Complete")

    # Main control loop
    while True:
        sensors.uplink()

        # update & pull controller inputs
        #pygame.event.pump()

        # send inputs to drive
        drive.move(controller.getAxis(0), controller.getAxis(1))

        # TODO: add more drive functionality than movement
