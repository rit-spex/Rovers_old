"""
Drivetrain Class to handle movement
Authors: Alexander Olds,
"""

import adafruit_pca9685
import board
# Imports
import busio
from adafruit_motor import servo

# Local Imports
from constants import *


class drivetrain:

    def __init__(self):
        # init i2c bus
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # init PWM controller
        self.pwm = adafruit_pca9685.PCA9685(self.i2c)
        self.pwm.frequency = 60

        # init drive motors on pins listed in constants.py
        self.frontLeft = self.pwm.channels[LF_PORT]
        self.centerLeft = self.pwm.channels[LC_PORT]
        self.rearLeft = self.pwm.channels[LR_PORT]

        self.frontRight = self.pwm.channels[RF_PORT]
        self.centerRight = self.pwm.channels[RC_PORT]
        self.rearRight = self.pwm.channels[RR_PORT]

        # init cornersteer servos on pins listed in constants.py
        # TODO: Verify and set servo pulse limits
        self.servoFrontLeft = servo.Servo(self.pwm.channels[CS_LF_PORT])
        self.servoRearLeft = servo.Servo(self.pwm.channels[CS_LR_PORT])

        self.servoFrontRight = servo.Servo(self.pwm.channels[CS_RF_PORT])
        self.servoRearRight = servo.Servo(self.pwm.channels[CS_RR_PORT])

    def move(self, throttle, turn):

        # set motor PWM duty cycles and direction
        if 0 <= throttle <= 1:
            self.frontLeft.duty_cycle = (0xffff)
            self.centerLeft.duty_cycle = (0xffff)
            self.rearLeft.duty_cycle = (0xffff)

            self.frontRight.duty_cycle = (0xffff)
            self.centerRight.duty_cycle = (0xffff)
            self.rearRight.duty_cycle = (0xffff)
        else:
            ValueError("Throttle should be a multiplier between -1 and 1")

        # set cornersteer servo angles
        if -1 <= turn < 0:
            self.servoFrontLeft.angle = (90 * (turn + 1))
            self.servoFrontRight.angle = (90 * (turn + 1))

            self.servoRearLeft.angle = (90 + (180 * (turn + 1)))
            self.servoRearRight.angle = (90 + (180 * (turn + 1)))
        elif 0 <= turn <= 1:
            self.servoFrontLeft.angle = (0 + (90 * turn))
            self.servoFrontRight.angle = (0 + (90 * turn))

            self.servoRearLeft.angle = (90 * turn)
            self.servoRearRight.angle = (90 * turn)
