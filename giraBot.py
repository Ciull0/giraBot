import serial
import time
import pip._vendor.urllib3
import json
import urllib3
arduino = serial.Serial('COM3',9600)

oldAngolo = 1
angolo = 1
url = "https://raw.githubusercontent.com/Ciull0/giraBot/master/status.json"
http = urllib3.PoolManager()
while 1:
    richiesta = http.request('GET',
                             url,
                             headers={
                                 'Cache-Control': 'no-cache',
                                 'Pragma': 'no-cache',
                                 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT'
                                 }
                            )
    numero = 90
    print(json.loads(richiesta.data))
    print(numero)
    if(numero>0 and numero<150):
        angolo = str(numero)
    if(angolo != oldAngolo):
        arduino.write(angolo.encode())
        oldAngolo = angolo
    time.sleep(1)
