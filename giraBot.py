import serial
import time
import pip._vendor.urllib3
import json
import urllib3
arduino = serial.Serial('COM3',9600)

oldAngolo = 1
angolo = 1
url = "https://api.jsonbin.io/b/5ffc4163f98f6e35d5fb17a8"
http = urllib3.PoolManager()
while 1:
    richiesta = http.request('GET',url)
    numero = json.loads(richiesta.data)['angolo']
    print(numero)
    if(numero>0 and numero<150):
        angolo = str(numero)
    if(angolo != oldAngolo):
        arduino.write(angolo.encode())
        oldAngolo = angolo
    time.sleep(1)
