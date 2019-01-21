"""
Core rover script for user I/O on the roverPi
this is a top-level init/process control file, all processes should be separate and executed here.
Authors: Alexander Olds,
"""

# Package Imports
import pygame

# Local Imports
from drivetrain import *


def __main__():
    # Initialization
    print("Initializing...")

    pygame.joystick.init()

    drive = drivetrain()

    controller = pygame.joystick.Joystick(0)
    controller.init()

    print("Connected to" + controller.get_name())

    print("Initialization Complete")

    # Main control loop
    while True:
        pygame.event.pump()
        drive.move(controller.getAxis(0), controller.getAxis(1))

        # TODO: add more functionality than movement
