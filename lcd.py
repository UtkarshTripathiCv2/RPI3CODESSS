import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd_rs = 12
lcd_en = 7
lcd_d4 = 8
lcd_d5 = 25
lcd_d6 = 24
lcd_d7 = 23

lcd_columns = 16
lcd_rows = 2

lcd = LCD.AdafruitCharLCD(lcdrs, lcden, lcdd4, lcdd5, lcdd6, lcd_d7,
                           lcdcolumns, lcdrows)

lcd.message('Hello World')
