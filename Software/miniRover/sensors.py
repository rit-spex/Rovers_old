"""
Multiple sensors-related classes to handle all external sensors, GPS, etc
Authors: Alexander Olds,
"""

# imports
import time

import adafruit_gps
import serial


# local imports


# TODO: Implement other sensors


class Sensors:

    def __init__(self):

        # vars
        self.last_print = 0
        self.current = 0

        # data
        self.uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=3000)  # Assume GPS connected via USB

        # object instantiation
        self.gps = adafruit_gps.GPS(self.uart, debug=False)

        # configuration (see adafruit libs)
        self.gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b'PMTK220,1000')

        self.last_print = time.monotonic()

    # Connect to GPS sats
    def uplink(self):

        self.gps.update()

        self.current = time.monotonic()
        if self.current - self.last_print >= 1.0:
            self.last_print = self.current
            if not self.gps.has_fix:
                print('Waiting for fix...')
            else:
                print('=' * 40)  # Print a separator line.
                print('Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(
                    self.gps.timestamp_utc.tm_mon,
                    self.gps.timestamp_utc.tm_mday,
                    self.gps.timestamp_utc.tm_year,
                    self.gps.timestamp_utc.tm_hour,
                    self.gps.timestamp_utc.tm_min,
                    self.gps.timestamp_utc.tm_sec))

                print('Latitude: {0:.6f} degrees'.format(self.gps.latitude))
                print('Longitude: {0:.6f} degrees'.format(self.gps.longitude))
                print('Fix quality: {}'.format(self.gps.fix_quality))

                # may not be present, check before printing

                # Number of connected sats
                if self.gps.satellites is not None:
                    print('# satellites: {}'.format(self.gps.satellites))

                # Altitude in Meters
                if self.gps.altitude_m is not None:
                    print('Altitude: {} meters'.format(self.gps.altitude_m))

                # Estimated ground speed in Knots
                if self.gps.speed_knots is not None:
                    print('Speed: {} knots'.format(self.gps.speed_knots))

                # Active sat track angle
                if self.gps.track_angle_deg is not None:
                    print('Track angle: {} degrees'.format(self.gps.track_angle_deg))

                # Estimated current Dilution of Precision
                if self.gps.horizontal_dilution is not None:
                    print('Horizontal dilution: {}'.format(self.gps.horizontal_dilution))

                # Height above surface ellipsoid
                if self.gps.height_geoid is not None:
                    print('Height geo ID: {} meters'.format(self.gps.height_geoid))
