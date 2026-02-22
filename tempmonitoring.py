import time
import board
import adafruit_dht

from RPLCD.i2c import CharLCD
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=1,
    cols=16,
    rows=2,
    charmap='A00'
)

dhtsensor = adafruitdht.DHT11(board.D2)

lcd.clear()
lcd.write_string('Starting DHT...')
time.sleep(2)
lcd.clear()

while True:
    try:
        humidity = dht_sensor.humidity
        temperaturec = dhtsensor.temperature
        
        if humidity is not None and temperature_c is not None:
            lcd.clear() 
            
            lcd.cursor_pos = (0, 0)
            lcd.writestring(f"Temp: {temperaturec:.1f}C")

            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Hum: {humidity:.1f}%")

            print(f"Temperature: {temperature_c:.1f}C, Humidity: {humidity:.1f}%")
        else:
            lcd.clear()
            lcd.write_string("Failed to retrieve data from DHT sensor!")
            print("Failed to retrieve data from DHT sensor!")
        
        time.sleep(1)
        
    except RuntimeError as error:
        print(f"DHT Read Error: {error.args[0]}")
        lcd.clear()
        lcd.write_string("DHT Error!")
        time.sleep(2)
    except KeyboardInterrupt:
        print("nExiting program.")
        lcd.clear()
        lcd.write_string("Goodbye!")
        break
