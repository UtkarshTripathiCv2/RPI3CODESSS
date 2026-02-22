from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(_name_)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED1 = 2
LED2 = 3
LED3 = 4

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.output(LED3, GPIO.LOW)

print("Done Initializing Raspberry Pi")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def control(state):
    if state == 'A':
        GPIO.output(LED1, GPIO.HIGH)
    elif state == 'a':
        GPIO.output(LED1, GPIO.LOW)
    elif state == 'B':
        GPIO.output(LED2, GPIO.HIGH)
    elif state == 'b':
        GPIO.output(LED2, GPIO.LOW)
    elif state == 'C':
        GPIO.output(LED3, GPIO.HIGH)
    elif state == 'c':
        GPIO.output(LED3, GPIO.LOW)
    return render_template('index.html')

if _name_ == '_main_':
    print("Starting Flask app")
    app.run(debug=True, host='YOURIPADDRESS', port=80)
