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

def fix_data(msg_dcode):
    """
    Recives a string and checks the string for duplicates.
    And removes them
    :param message:
    :return:
    """
    unique = list(set(msg_dcode.split()))
    clean_data = ''
    for word in unique:
        if word is not 'stop':
            clean_data += word

    return clean_data


tank = init()

while True:
    try:
        ready = select.select([s], [], [], 0)
        if ready[0]:
            message = s.recvfrom(1024) # recieve data
            #print(message[0])
            direction = fix_data(message[0].decode("utf-8"))
            if(direction):
                #print(direction)
                if 'stop'in direction:
                    tank.stop_servos()
                    
                tank.dir_listener(direction)
       # tank.update()

    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()
    
    #direction = input()
    #if direction:
    #update(direction)
    #tank.stop_servos()
