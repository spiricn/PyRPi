import RPi.GPIO as GPIO


class IOPin:
    '''
    GPIO PIN wrapper
    '''

    PUD_DOWN = GPIO.PUD_DOWN
    PUD_UP = GPIO.PUD_UP

    def __init__(self, number, mode):
        self._number = number
        self._mode = mode

    @staticmethod
    def createInput(number, pullUpDown=GPIO.PUD_DOWN):
        '''
        Create input pin
        '''

        mode = GPIO.IN

        GPIO.setup(number, mode, pull_up_down=pullUpDown)

        return IOPin(number, mode)

    @staticmethod
    def createOutput(number):
        '''
        Create output pin
        '''

        mode = GPIO.OUT

        GPIO.setup(number, mode)

        return IOPin(number, mode)

    @property
    def input(self):
        '''
        Check if there's input on the PIN
        '''

        return GPIO.input(self._number)

    def setOutput(self, output):
        '''
        Set PIN output
        
        @param output: PIN output
        '''

        GPIO.output(self._number, GPIO.HIGH if output else GPIO.LOW)

    def setCallback(self, callback, mode=GPIO.BOTH, bounceTimeMs=10):
        '''
        Register rcallback to detect falling/rising edge or both
        
        @param param: callback Callback function
        @param mode: Edge mode
        @param bounceTimeMs: Debouncer time   
        '''

        # Register event
        GPIO.add_event_detect(
            self._number,
            mode,  # detect both rising and falling edge
            callback=lambda pin: callback(self),
            bouncetime=bounceTimeMs
        )

    @property
    def number(self):
        '''
        PIN number
        '''

        return self._number

    @staticmethod
    def init():
        '''
        Initialize PIN control
        '''

        GPIO.setmode(GPIO.BCM)
