from time import time, sleep

timeOn = 0
counter = 0

def counterAdd ():
    global counter
    counter = counter + 1 
    sleep (1)

def now():
    return str(time())

while True:
    counterAdd()
    if (counter %10) == 0 :
        print ("Dizaine")
        timeOn = time()
    elif time() >= timeOn + 3 :
        print ("off")

