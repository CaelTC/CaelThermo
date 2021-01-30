from gpiozero import LED
from time import sleep


led = LED(25)
while True:
    led.blink()
   