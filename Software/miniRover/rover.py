# Core rover script for user I/O on the roverPi
# this is a top-level init/process control file, all processes should be separate and executed here.
# Authors: Alexander Olds,


# Package Imports
from evdev import *

# Local Imports
import drivetrain

# Initialization
print("Initializing...")

drive = drivetrain()
controller = InputDevice('dev/input/event3')  # Placeholder path

print("Connected to" + controller)

print("Initialization Complete")

# Main control loop
while True:
    for event in controller.read_loop():
        print(event)
