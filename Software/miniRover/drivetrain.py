"""
Drivetrain Class to handle movement
Authors: Alexander Olds,
"""

# Imports
import busio
from Adafruit_PCA9685 import *
from adafruit_motor import servo
from board import SCL, SDA

# Local Imports
from constants import *


class drivetrain:

    def __init__(self):
        # init i2c bus
        self.i2c = busio.I2C(SCL, SDA)

        # init PWM controller
        self.pwm = PCA9685(self.i2c)
        self.pwm.frequency = 50

        # init drive motors on pins listed in constants.py
        self.frontLeft = self.pwm.PWMChannel(self.pwm, LF_PORT)
        self.centerLeft = self.pwm.PWMChannel(self.pwm, LC_PORT)
        self.rearLeft = self.pwm.PWMChannel(self.pwm, LR_PORT)

        self.frontRight = self.pwm.PWMChannel(self.pwm, RF_PORT)
        self.centerRight = self.pwm.PWMChannel(self.pwm, RC_PORT)
        self.rearRight = self.pwm.PWMChannel(self.pwm, RC_PORT)

        # init cornersteer servos on pins listed in constants.py
        # TODO: Verify and set servo pulse limits
        self.servoFrontLeft = servo.Servo(self.pwm.channels[CS_LF_PORT])
        self.servoRearLeft = servo.Servo(self.pwm.channels[CS_LR_PORT])

        self.servoFrontRight = servo.Servo(self.pwm.channels[CS_RF_PORT])
        self.servoRearRight = servo.Servo(self.pwm.channels[CS_RR_PORT])

    def move(self, throttle, turn):

        # set motor PWM duty cycles and direction
        if 0 <= throttle <= 1:
            self.frontLeft.duty_cycle = (0xffff * throttle)
            self.centerLeft.duty_cycle = (0xffff * throttle)
            self.rearLeft.duty_cycle = (0xffff * throttle)

            self.frontRight.duty_cycle = (0xffff * throttle)
            self.centerRight.duty_cycle = (0xffff * throttle)
            self.rearRight.duty_cycle = (0xffff * throttle)
        elif -1 <= throttle < 0:
            # TODO: implement motor reverse
            self.frontLeft.duty_cycle = (0xffff * abs(throttle))
            self.centerLeft.duty_cycle = (0xffff * abs(throttle))
            self.rearLeft.duty_cycle = (0xffff * abs(throttle))

            self.frontRight.duty_cycle = (0xffff * abs(throttle))
            self.centerRight.duty_cycle = (0xffff * abs(throttle))
            self.rearRight.duty_cycle = (0xffff * abs(throttle))
        else:
            ValueError("Throttle should be a multiplier between -1 and 1")

        # set cornersteer servo angles
        if -1 <= turn < 0:
            self.servoFrontLeft.angle = (90 * (turn + 1))
            self.servoFrontRight.angle = (90 * (turn + 1))

            self.servoRearLeft.angle = (90 + (180 * (turn + 1)))
            self.servoRearRight.angle = (90 + (180 * (turn + 1)))
        elif 0 <= turn <= 1:
            self.servoFrontLeft.angle = (90 + (180 * turn))
            self.servoFrontRight.angle = (90 + (180 * turn))

            self.servoRearLeft.angle = (90 * turn)
            self.servoRearRight.angle = (90 * turn)
