import serial
import time
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1) 

def read():
    data = arduino.readline() 
    return data

print("Estamos trabajando para usted")

time.sleep(4) ## Los 4 primeros valores son blancos


while True:
    value = read()
    value = int(value)
        
    print(value) # printing the value
    time.sleep(0.5)