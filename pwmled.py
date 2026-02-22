import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 100)
p.start(0)

while True:
    for x in range(100):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)

    for x in range(99, -1, -1):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
