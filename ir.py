import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

IRSENSORPIN = 3
BUZZER_PIN = 5

GPIO.setup(IRSENSORPIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        sensorvalue = GPIO.input(IRSENSOR_PIN)
        print(sensor_value)

        if sensor_value == 1:
            GPIO.output(BUZZER_PIN, GPIO.LOW)
        else:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()
