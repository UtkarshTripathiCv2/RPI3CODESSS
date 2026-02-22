import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # Set the GPIO pin numbering mode to BOARD
GPIO.setup(3, GPIO.OUT)  # Set pin 3 as an output pin

while True:
    GPIO.output(3, True)  # Turn LED on (logic 1)
    time.sleep(1)         # Wait for 1 second
    GPIO.output(3, False) # Turn LED off (logic 0)
    time.sleep(1)         # Wait for 1 second
