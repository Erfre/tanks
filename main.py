from controller import controller
import json
import socket
from os import system
import sys
import select

tank_thread = None


s  = socket.socket()

host = '192.168.1.64' #Eriks network
#host = '192.168.1.137'
#host = '192.168.0.121' # OG laptop at erik
port = 10000
s.connect((host, port))
s.setblocking(0)
input = [s]
def init():
    tank = controller(17,27,22, None, None)
    tank.start(3)
    msg = "start"
    s.send(msg.encode())
    return tank

def update(message):
    print(message)
    tank.dir_listener(message)

def fix_data(dir):
    """
    Recives a dict and removes duplicates.
    
    :param message:
    :return:
    """
   # if dir

tank = init()

while True:
    try:
        ready = select.select([s], [], [], 0)
        if ready[0]:
            message = s.recvfrom(1024) # recieve data
            test = (message[0].decode("utf-8"))
            try:
                inputs = json.loads(test)
                print(inputs,type(inputs),len(inputs))
                tank.dir_listener(inputs)
            except json.decoder.JSONdecodeError:
                inputs, dump = json.loads(test)
                tank.dir_listener(inputs)

    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()
    
    #direction = input()
    #if direction:
    #update(direction)
    #tank.stop_servos()
