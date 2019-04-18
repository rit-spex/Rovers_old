"""
Core rover script for user I/O on the roverPi
this is a top-level init/process control file, all processes should be separate and executed here.
Authors: Alexander Olds, Thomas Hall
"""

# Package Imports
import sys

import evdev
from adafruit_servokit import ServoKit

from constants import *
# Local Imports
from sensors import *

if __name__ == '__main__':

    import board
    import busio
    import adafruit_pca9685

    # Initialization

    print("Initializing Sensors...", end='')
    sensors = Sensors()
    print("Done")

    print("Initializing Drivetrain...", end='')
    i2c = busio.I2C(board.SCL, board.SDA)
    pwm = adafruit_pca9685.PCA9685(i2c)
    pwm.frequency = 50

    servoKit = ServoKit(channels=16, i2c=i2c)

    driveLeft = pwm.channels[L_PORT]
    driveRight = pwm.channels[R_PORT]

    frontLeftServo = servoKit.servo[CS_LF_PORT]
    rearLeftServo = servoKit.servo[CS_LR_PORT]

    frontRightServo = servoKit.servo[CS_RF_PORT]
    rearRightServo = servoKit.servo[CS_RR_PORT]

    print("Done")

    print("Initializing Controllers...", end='')

    xAxis = 0
    yAxis = 0
    controller = 0
    try:
        controller = evdev.InputDevice('/dev/input/event0')
        controller_connected = 1

    except KeyboardInterrupt:
        controller_connected = -1

    if controller_connected > 0:
        print("Done")
        print("Connected to input device")
    else:
        print("Failed!")
        print("Controller Not Connected")

    print("Initialization Complete")

    # Main control loop
    while True:
        try:
            """try:
                sensors.uplink()
            except UnicodeDecodeError:
                print("Unicode Error, Trying Again...")"""

            # update & pull controller inputs
            if controller_connected > 0:
                for event in controller.read_loop():
                    if event.type == evdev.ecodes.EV_ABS:
                        if event.code == 1:
                            yAxis = round((-(event.value / 32767) + 1), 3)
                        elif event.code == 1:
                            xAxis = round((event.value / 32767), 3)

                    # send inputs to drive
                    # 0x1444 center, 0x0ccc full reverse, 0x1ddd full forward
                    throttle = (yAxis * THROTTLE_MULTIPLIER * 0x0778) + 0x1444

                    # 0x1333 center, 0x08f5 for left, 0x1d70 for right
                    # turn = (xAxis * 90) + 90

                    print(hex(int(throttle)))

                    # motors
                    driveLeft.duty_cycle = int(throttle)
                    driveRight.duty_cycle = int(throttle)

                    # servos
                    # frontLeftServo.angle = turn
                    # frontRightServo.angle = turn

                    # rearLeftServo.angle = -(turn - 180)
                    # rearRightServo.angle = -(turn - 180)
            else:
                throttle = 0x1444  # 0x1444
                turn = 90

            # motors

            # print(throttle, turn)

            # driveLeft.duty_cycle = throttle
            # driveRight.duty_cycle = throttle

            # servos
            # frontLeftServo.angle = turn
            # frontRightServo.angle = turn

            # rearLeftServo.angle = -(turn - 180)
            # rearRightServo.angle = -(turn - 180)

        except KeyboardInterrupt:

            #  Stop all motors
            driveLeft.duty_cycle = 0x1444
            driveRight.duty_cycle = 0x1444

            # center all servos
            frontLeftServo.angle = 90
            frontRightServo.angle = 90

            rearLeftServo.angle = 90
            rearRightServo.angle = 90

            print('\n')
            print("Program Terminated by User")
            sys.exit()
