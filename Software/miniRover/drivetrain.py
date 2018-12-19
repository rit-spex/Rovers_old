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
        i2c = busio.I2C(SCL, SDA)

        # init PWM controller
        pwm = PCA9685(i2c)
        pwm.frequency = 50

        # init drive motors on pins listed in constants.py
        frontLeft = PCA9685.PWMChannel(pwm, LF_PORT)
        frontRight = PCA9685.PWMChannel(pwm, RF_PORT)
        centerLeft = PCA9685.PWMChannel(pwm, LC_PORT)
        centerRigth = PCA9685.PWMChannel(pwm, RC_PORT)
        rearLeft = PCA9685.PWMChannel(pwm, LR_PORT)
        rearRight = PCA9685.PWMChannel(pwm, RC_PORT)

        # init cornersteer servos TODO: Verify and set servo pulse limits
        servoFrontLeft = servo.Servo(pwm.channels[CS_LF_PORT])
        servoFrontRigth = servo.Servo(pwm.channels[CS_RF_PORT])
        servoRearLeft = servo.Servo(pwm.channels[CS_LR_PORT])
        servoRearRight = servo.Servo(pwm.channels[CS_RR_PORT])

    def move(self, throttle, turn):

        if -1 <= throttle <= 1:
            # set motor PWM duty cycles
            self.frontLeft.duty_cycle = (0xffff * throttle)
            self.frontRight.duty_cycle = (0xffff * throttle)
            self.centerLeft.duty_cycle = (0xffff * throttle)
            self.centerRight.duty_cycle = (0xffff * throttle)
            self.rearLeft.duty_cycle = (0xffff * throttle)
            self.rearRight.duty_cycle = (0xffff * throttle)
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
