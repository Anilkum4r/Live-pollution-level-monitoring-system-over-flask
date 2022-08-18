from serial import Serial
import requests

com =Serial("COM1" ,9600)
d ={}
while True:
    if com.inWaiting() > 0:
        rx =com.readline().decode()
        print(rx)

        d['ldr'] =rx[0]
        print(d)

        resp =requests.post("http://127.0.0.1:5000/",data=d)
        print(resp.text)
