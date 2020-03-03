import board
import digitalio
import time
import board
import neopixel

display = board.DISPLAY

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)

while True:
    led.value = True
    time.sleep(1.0)
    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels[2] = (0, 0, 0)
    pixels[3] = (0, 0, 0)
    pixels[4] = (0, 0, 0)
    pixels.show()
    led.value = False
    time.sleep(1.0)
    pixels[0] = (10, 0, 0)
    pixels[1] = (0, 10, 0)
    pixels[2] = (0, 0, 10)
    pixels[3] = (10, 10, 0)
    pixels[4] = (0, 10, 10)
    pixels.show()
