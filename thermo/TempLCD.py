#!/usr/bin/env python3
########################################################################
# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : freenove
# modification: 2018/08/03
########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime
from Freenove_DHT import DHT
 
DHTpin = 11


def get_temperature():    
    sensor = DHT(DHTpin)
    status= sensor.readDHT11()
    if status is sensor.DHTLIB_OK:
        return sensor.temperature 
    else:
        return None
 
 def get_humidity():    
    sensor = DHT(DHTpin)
    status= sensor.readDHT11()
    if status is sensor.DHTLIB_OK:
        return sensor.humidity 
    else:
        return None
       
 def display_temperature (temperature):  
    if temperature is None:
        lcd.message( 'Temperature error')
    else:
        lcd.message( 'Temp: ' + str(temperature)+'\n' )

def display_humidity (humidity):
    if humidity is None:
        lcd.message( 'Humidity error')
    else:
        lcd.message( 'Hum:' + str(humidity)+ '/n')


def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    while(True):  
        temperature = get_temperature()  
        humidity = get_humidity()     
        lcd.setCursor(0,0)  
        display_temperature(temperature)
        display_humidity(humidity)
        sleep(1)
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

