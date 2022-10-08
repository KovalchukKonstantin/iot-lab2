import picar_4wd as fc
import bluetooth
import sys
import tty
import termios
import asyncio

power_val = 50

hostMACAddress = "E4:5F:01:CE:D1:9D" #"DC:A6:32:80:7D:87" # The address of Raspberry PI Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
backlog = 1
size = 1024



def Keyboard_control():
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.bind((hostMACAddress, port))
    s.listen(backlog)
    print("listening on port ", port)   
    try:
        client, clientInfo = s.accept()
        while True:
            print("server recv from: ", clientInfo)
            global power_val
            key = client.recv(size).decode('utf-8')
            if not key:
                continue
            print(key)
            if key=='6':
                if power_val <=90:
                    power_val += 10
                    print("power_val:",power_val)
            elif key=='4':
                if power_val >=10:
                    power_val -= 10
                    print("power_val:",power_val)
            if key=='w':
                fc.forward(power_val)
            elif key=='a':
                fc.turn_left(power_val)
            elif key=='s':
                fc.backward(power_val)
            elif key=='d':
                fc.turn_right(power_val)
            else:
                fc.stop()
            if key=='q':
                print("quit")  
                break  
    except: 
        print("Closing socket")
        client.close()
        s.close()

if __name__ == '__main__':
    Keyboard_control()






