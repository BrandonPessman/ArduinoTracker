#! /usr/bin/env python
import serial
import time
ser = serial.Serial(port='/dev/ttyACM0',baudrate = 9600,parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
# Wait to read from Arduino
while 1:
   try:
       time.sleep(10)
       # send an R to the arduino
       ser.write(str.encode("R"))
       #read data from arduino
       myData = ser.readline()
       print(myData)
   except KeyboardInterrupt:
       exit()