from controller import controller
import socket

s  = socket.socket()
host = '192.168.1.239'
port = 10000
s.connect((host, port))

def init():
    tank = controller(2, 3, None, None, None)
    tank.start(3)
    return tank

def update(message):
    tank.dir_listener(message)

tank = init()

while True:
    message = s.recvfrom(1024)
    direction = message[0].decode("utf-8")
    print(direction)
    if direction:
        update(direction)