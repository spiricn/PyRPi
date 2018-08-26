
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import RPi.GPIO as GPIO
from threading import Lock


class Renderer:
    '''
    Adafruit SSD1306 display control wrapper
    '''

    def __init__(self):
        # Initialize library
        self._disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

        # Create display
        self._disp.begin()
        self._disp.display()

        # Create image & draw interface
        self._image = Image.new('1', (self.width, self.height))
        self._draw = ImageDraw.Draw(self._image)

        # Load font
        self._font = ImageFont.load_default()

        self._lock = Lock()

    @property
    def width(self):
        '''
        Display width
        '''

        return self._disp.width

    @property
    def height(self):
        '''
        Display height
        '''

        return self._disp.height

    def clear(self, color=0):
        '''
        Clear the display with  given color 
        
        @param color: Color in range [0, 255] 
        '''

        with self._lock:
            self._draw.rectangle(self.rect, outline=0, fill=color)

    def drawText(self, position, text, color=255):
        '''
        Draws a text
        
        @param position: Display coordinates
        @param text: Text
        @param color: Text color 
        '''
        with self._lock:
            x, y = position

            # Go trough the text line by line
            for line in text.splitlines():
                # Draw single line
                self._draw.text((x, y), line, font=self._font, fill=color)

                # Move to the next row
                y += self.measureText(line)[1]

    def display(self):
        '''
        Displays drawn image
        '''

        with self._lock:
            self._disp.image(self._image)
            self._disp.display()

    def measureText(self, text):
        '''
        Measures text (may bbe multiline)
        '''

        # Split it into lines
        lines = text.splitlines()

        width = 0
        height = 0

        for line in lines:
            # Measure line
            size = self._font.getsize(line)

            # Calculate new size
            width = max(width, size[0])
            height += size[1]

        return width, height

    @property
    def rect(self):
        '''
        Display dimensions
        '''

        return (0, 0, self.width, self.height)
