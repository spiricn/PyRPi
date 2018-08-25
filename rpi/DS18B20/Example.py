import sys
import time
from rpi.DS18B20.TemperatureSensor import TemperatureSensor


def main(deviceId):
    '''
    Example demonstrating the usage of the DS18B20 temperature probe 
    '''

    # Create the sensor
    sensor = TemperatureSensor(deviceId)

    print('Press ctrl+c to stop')

    while True:
        # Read the temperature
        temperatureC = sensor.getTemperatureCelsius()

        # Check if the reading is valid
        if temperatureC == TemperatureSensor.TEMP_INVALID_C:
            print('Error reading temperature, aborting ..')
            return -1

        # Print & wait a bit
        print('Current temperature: %.2f C' % temperatureC)

        time.sleep(1)

    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # Print usage
        print('Usage: Example.py <w1 device ID>')
        sys.exit(-1)

    # Run example
    sys.exit(main(sys.argv[1]))
