
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from rpi.SSD1306.Renderer import Renderer


class Ssd1306:
    '''
    Adafruit SSD1306 display control wrapper
    '''

    # Button definition
    BUTTON_LEFT, BUTTON_RIGHT, BUTTON_UP, BUTTON_DOWN, BUTTON_CENTER, BUTTON_A, BUTTON_B = range(7)

    # Buttons available
    BUTTONS = (BUTTON_LEFT, BUTTON_RIGHT, BUTTON_UP, BUTTON_DOWN, BUTTON_CENTER, BUTTON_A, BUTTON_B)

    # Button pins
    BUTTON_PINS = (27, 23, 4, 17, 22, 5, 6)

    def __init__(self):
        # Crate renderer
        self._renderer = Renderer()

        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)

        # Initialize button pins
        for pin in self.BUTTON_PINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def setButtonListener(self, button, callback):
        '''
        Registers button callback
        
        @param button: Button ID
        @param callback: Callback function  
        '''

        # Get button pin
        pin = self.getButtonPin(button)

        # Register event
        GPIO.add_event_detect(
            pin,
            GPIO.BOTH,  # detect both rising and falling edge
            callback=lambda pin: callback(button, self.isButtonPressed(button)),
                              bouncetime=10)

    def isButtonPressed(self, button):
        '''
        Checks if button is pressed
        
        @param button: Button ID
        
        @return: True if pressed, False otherwise
        '''

        return not GPIO.input(self.getButtonPin(button))

    def getButtonPin(self, button):
        '''
        Get PIN number of corresponding button
        
        @param buutton: Button ID
        
        @return PIN number on success, None otherwise 
        '''

        return self.BUTTON_PINS[button] if button < len(self.BUTTON_PINS) else None

    @property
    def renderer(self):
        '''
        Display renderer
        '''

        return self._renderer
