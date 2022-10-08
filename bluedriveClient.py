import bluetooth
import sys
import msvcrt
import asyncio


host = "E4:5F:01:CE:D1:9D" # The address of Raspberry PI Bluetooth adapter on the server.
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

power_val = 50
key = 'status'
print("If you want to quit.Please press q")


def readkey():
    while True:
        if msvcrt.kbhit():
            k = msvcrt.getch().decode('utf-8')
            print("Key Pressed", k)
            return k

while 1:
    text = readkey() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    sock.send(text)

    #data = sock.recv(1024)
    #print("from server: ", data)

sock.close()
