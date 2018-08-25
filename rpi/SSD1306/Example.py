import sys
import time
from rpi.SSD1306.Ssd1306 import Ssd1306
from rpi import SSD1306


def main():
    '''
    Example demonstrating the usage of the SSD 1306 wrapper
    
    Includes rendering & button handling
    '''

    # Initialize controller
    ssd = Ssd1306()

    # Register button callbacks
    for button in ssd.BUTTONS:
        ssd.setButtonListener(button,
                              lambda button, pressed: print('Button %s %d' % ('pressed' if pressed else 'released', button))
                              )

    counter = 0

    # Some text to animate trough
    animation = '\\', '|', '/', '-'

    print('Press ctrl+c to stop')

    while True:

        # Go to next character in animation
        counter = (counter + 1) % len(animation)

        # First line of text
        text = ' %s Press any button %s' % (animation[counter], animation[len(animation) - counter - 1])

        text += '\n'

        # Second line of text (button status)
        for button in ssd.BUTTONS:
            text += '' if not ssd.isButtonPressed(button) else ' %d' % button

        # Clear background
        ssd.renderer.clear()

        # Draw text
        ssd.renderer.drawText((0, 0), text)

        # Display image
        ssd.renderer.display()

        # Wait a bit
        time.sleep(0.1)

    return 0


if __name__ == '__main__':
    sys.exit(main())
