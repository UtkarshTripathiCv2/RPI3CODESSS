Arduino Code (Arduino IDE)
void setup() {
  pinMode(12, INPUT);
  Serial.begin(9600);
}

void loop() {
  int val = digitalRead(12);
  Serial.println(val);
  delay(500);
}


python
# Raspberry Pi Code (Python)
import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    s = ser.readline().decode().strip()
    try:
        val = int(s)
        print(val)
        if val == 1:
            GPIO.output(3, GPIO.LOW)
        else:
            GPIO.output(3, GPIO.HIGH)
    except ValueError:
        pass
    time.sleep(0.1)
