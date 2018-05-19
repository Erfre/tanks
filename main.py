from controller import controller
import socket
import sys
from os import system

tank_thread = None

s = socket.socket()
host = '192.168.0.103'
port = 10000
s.connect((host, port))
input = [s]
def init():
    tank = controller(2, 3, None, None, None)
    tank.start(3)
    return tank

def update(message):
   tank.dir_listener(message)

tank = init()

while True:
    try:
        message = s.recvfrom(2048)
        print(message)
        direction = message[0].decode("utf-8")
        print(direction)
        tank.update()
        if(direction):
            tank.dir_listener(direction)
    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        s.close()
        sys.exit()