from controller import controller
import json
import socket
from os import system
import sys
import select

tank_thread = None


s  = socket.socket()

host = '192.168.1.230' #Eriks network
#host = '192.168.1.137'
#host = '192.168.0.121' # OG laptop at erik
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

def fix_data(dir):
    """
    Recives a string and checks the string for duplicates.
    And removes them
    :param message:
    :return:
    """
    #for key in dir:
       # if dir[]


tank = init()

while True:
    try:
        ready = select.select([s], [], [], 0)
        if ready[0]:
            message = s.recvfrom(1024) # recieve data
            print(message[0])
            inputs = json.loads(message[0].decode("utf-8"))
            tank.dir_listener(inputs)

    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()
    
    #direction = input()
    #if direction:
    #update(direction)
    #tank.stop_servos()
