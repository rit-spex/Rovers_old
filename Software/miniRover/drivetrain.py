# Drivetrain Class to handle movement
# Authors: Alexander Olds,

# Imports
import Adafruit_PCA9685


class drivetrain:

    def __init__(self):
        pwm = Adafruit_PCA9685.PCA9685()

    def move(self, speed, turn):
        thing = 1

    # Helper function to help set PWM cycles up
    def set_duty_cycle(self, ):
        thing = 1
