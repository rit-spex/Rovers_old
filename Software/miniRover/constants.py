"""
Constants file for miniRover
For clarity, contains all constants (usually port numbers)
Authors: Alexander Olds,
"""

# DEBUG
DEBUG = True

# Drive Motors
# TODO: Verify Motor and servo port #s
THROTTLE_MULTIPLIER = 0.7

LF_PORT = 4  # Front-Left
LC_PORT = 5  # Central-Left
LR_PORT = 6  # Rear-Left

RF_PORT = 7  # Front-Right
RC_PORT = 8  # Central-Right
RR_PORT = 9  # Rear-Right

# Corner Steering
CS_LF_PORT = 0  # Front-Left
CS_LR_PORT = 1  # Rear-Left

CS_RF_PORT = 2  # Front-Right
CS_RR_PORT = 3  # Rear-Right

# Controller input codes (may need to be changed for different controllers)
# TODO: Verify controller input codes
IN_A = 1
IN_B = 1
IN_X = 1
IN_Y = 1
IN_L = 1
IN_R = 1
IN_U = 1
IN_D = 1
IN_RT = 1
IN_LT = 1
IN_RB = 1
IN_LB = 1
IN_START = 1
IN_SEL = 1

# Sensor-related pins
