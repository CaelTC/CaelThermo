from time import time, sleep

timeOn = -3
counter = 0

def counterAdd ():
    global counter
    counter = counter + 1 
    sleep (1)

def now():
    return str(time())

def loop():
    while True:
        counterAdd()
        global timeOn
        if (counter %10) == 0 :
            print ("Dizaine")
            timeOn = time()
        elif time() >= timeOn + 3 :
            print ("off")

try: 
    loop()
except KeyboardInterrupt:
    counter = 0