import serial
import time
arduino = serial.Serial('COM3',9600)

print("Inserisci angolo di rotazione")
oldAngolo = 1
while 1:
    angolo = input()
    if(angolo != oldAngolo):
        arduino.write(angolo.encode())
        oldAngolo = angolo