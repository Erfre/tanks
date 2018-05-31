from controller import controller
import socket
from time import sleep
import select
from os import system
import threading
import sys
import select
import time
tank_thread = None


s  = socket.socket()

#host = '192.168.0.103' #Eriks network
#host = '192.168.1.137'
host = '192.168.0.121' # OG laptop at erik
port = 10000
s.connect((host, port))
s.setblocking(0)
input = [s]
def init():
    tank = controller(17,27,22, None, None)
    tank.start(3)
    return tank

def update(message):
    print(message)
    tank.dir_listener(message)

tank = init()

while True:
    try:
        ready = select.select([s], [], [], 0)
        if ready[0]:
            message = s.recvfrom(1024)

            direction = message[0].decode("utf-8")
            print(direction)
        
            if(direction):
                print(direction)
                tank.dir_listener(direction)
            
        tank.update()

    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()
    
    #direction = input()
    #if direction:
    #update(direction)
    #tank.stop_servos()
