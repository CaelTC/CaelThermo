#!/usr/bin/env python3
########################################################################
# Filename    : Tablelamp.py
# Description : DIY MINI table lamp
# Author      : www.freenove.com
# modification: 2019/12/27
####################################################################
from gpiozero import Button
from time import sleep


buttonDecrementPin = Button(24)
buttonIncrementPin = Button(23)
count = 10.0


def buttonIncrement():
    global count
    if buttonIncrementPin.is_pressed:
        count = count + 0.5
        sleep (5)


def buttonDecrement():
    global count
    if buttonDecrementPin.is_pressed:
        count = count - 0.5
        sleep (0.3)




def loop():
    while True:
        buttonIncrement()
        buttonDecrement()
        print(count)
        sleep (.1)


if __name__ == '__main__':
    print('Program is starting...')
    try:
        print(count)
        print (buttonIncrement)
        loop()
    except KeyboardInterrupt:
        count = 100