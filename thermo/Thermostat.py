#!/usr/bin/env python3
########################################################################
# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : freenove
# modification: 2018/08/03
########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import time, sleep
from Freenove_DHT import DHT
from gpiozero import Button
import gpiozero
import os



current_temperature = 20
DHTpin = 17
buttonDecrementPin = Button(22)
buttonIncrementPin = Button(27)
temperatureTarget = 18.0
Relay_PIN = 16
relay = gpiozero.OutputDevice(Relay_PIN, active_high=False, initial_value=False,  )
activationTimeoutinSec = 300
timeOn = -60
counter = 0


def get_temperature():
    global current_temperature
    try:
        sensor = DHT(DHTpin)
        status = sensor.readDHT11()
        if status is sensor.DHTLIB_OK:
            current_temperature = sensor.temperature
            print(sensor.temperature))
        
    except Exception as e:
        print(e)

def buttonIncrement():
    global temperatureTarget
    temperatureTarget = temperatureTarget + 0.5
    

def chauffage():
    global temperatureTarget
    global timeOn
    global current_temperature
    if temperatureTarget > current_temperature:
        relay.on()
        timeOn = time()
    elif time() >= timeOn + activationTimeoutinSec:
        relay.off()
    
def restart():
    global temperatureTarget
    if temperatureTarget > 35:
        os.system("shutdown now -r")
    if temperatureTarget < 10:
        os.system("shutdown now -r")

def buttonDecrement():
    global temperatureTarget
    temperatureTarget = temperatureTarget - 0.5

def display():
    global temperatureTarget
    global current_temperature
    if current_temperature is None:
        lcd.message('Temperature error')
    else:
        lcd.message('Temp: ' + str(current_temperature) +'\n')
        print("UpdateTemp")
        lcd.message('Cible ' + str(temperatureTarget) +'\n')
        print("update cible")

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
        print('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4, 5, 6, 7], GPIO=mcp)
def setup():
    mcp.output(3, 1)     # turn on LCD backlight
    lcd.begin(16, 2)   
    lcd.setCursor(0, 0)


def loop():
    while (True):
        get_temperature() # this updates the current_temperature
        chauffage()
        buttonDecrementPin.when_pressed = buttonDecrement
        buttonIncrementPin.when_pressed = buttonIncrement 
        display()
        restart()
        sleep(0.1)
           
        
if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        setup()
        loop()
        
    except KeyboardInterrupt:
        destroy()
