
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from rpi.SSD1306.Renderer import Renderer
from rpi.IOPin import IOPin


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

        self._pins = []

        # Initialize button pins
        for pinNumber in self.BUTTON_PINS:
            self._pins.append(IOPin.createInput(pinNumber, IOPin.PUD_UP))

    def setButtonListener(self, button, callback):
        '''
        Registers button callback
        
        @param button: Button ID
        @param callback: Callback function  
        '''

        # Get button pin
        pin = self.getButtonPin(button)

        pin.setCallback(lambda ioPin: callback(button, self.isButtonPressed(button)))

    def isButtonPressed(self, button):
        '''
        Checks if button is pressed
        
        @param button: Button ID
        
        @return: True if pressed, False otherwise
        '''

        return not self.getButtonPin(button).input

    def getButtonPin(self, button):
        '''
        Get PIN number of corresponding button
        
        @param buutton: Button ID
        
        @return PIN number on success, None otherwise 
        '''

        return self._pins[button] if button < len(self._pins) else None

    @property
    def renderer(self):
        '''
        Display renderer
        '''

        return self._renderer
