import csv
from os import truncate
from time import time, sleep, timezone
import logging

counter = 0
lgr = logging.getLogger()
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG# add a file handler
fh = logging.FileHandler('/home/cael/CaelThermo/test.csv')
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
timE = time()
# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s, %(message)s, ')
fh.setFormatter(frmt)

# add the Handler to the logger
lgr.addHandler(fh)
        
def add():
    global counter
    counter += 1
    print("+1")
def write():
    global counter
    lgr.debug('counter'+''+'%s', counter)
def loop():
    write()
    add()
    sleep (5)

if __name__ == '__main__':
    while True:
        loop()
        
    