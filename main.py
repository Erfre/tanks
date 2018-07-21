from controller import controller
import json
import socket
from os import system
import sys
import select

tank_thread = None

s = socket.socket()

host = '192.168.0.101'  # ip of server
port = 10000
s.connect((host, port))
s.setblocking(0)
#input = [s]

def init():
    tank = controller(17,27,22, None, None)
    tank.start(3)
    msg = "start"
    s.send(msg.encode())
    return tank

def update(message):
    print(message)
    tank.dir_listener(message)

def fix_data(data):
    """
    When recieving queued up data it splits it into a list.
    Splits the data after the newline and pops out the last data which is a
    empty string and returns it.
    
    :param message: 
    :return:
    """
    dict_list = data.split('\n')
    dict_list.pop()
    return dict_list


tank = init()

while True:
    try:
        ready = select.select([s], [], [], 0)
        if ready[0]:
            message = s.recvfrom(1024) # recieve data
            data = (message[0].decode("utf-8"))
            clean_data = fix_data(data)
            if len(clean_data) > 1:
                for direction in clean_data:
                    inputs = json.loads(direction) #convert to dict
                    tank.dir_listener(inputs) #TODO loop the dir_listener

            else:
                inputs = json.loads(clean_data[0])
                tank.dir_listener(inputs)

    except (KeyboardInterrupt):
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()


    except:
        system("sudo killall pigpiod")
        system("sudo pkill pigpiod")
        sys.exit()


