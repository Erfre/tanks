import pigpio
from os import system
from time import sleep

class controller:
    """The tank class"""
    def __init__(self, right_servo, left_servo, tower_servo, cannon_servo, laser):
        """

        :param right_servo: GPIO pin connector on PI
        :param left_servo: GPIO pin connector on PI
        :param tower_servo: GPIO pin connector on PI
        :param cannon_servo: GPIO pin connector on PI
        :param laser: GPIO pin connector on PI
        """
        self.r_servo = right_servo
        self.l_servo = left_servo
        self.t_servo = tower_servo
        self.c_servo = cannon_servo
        self.laser = laser
        self.pi = None
        self.hp = 0
        self.servos = []

    def start(self, hp):
        """

        :param hp: integer value for HP of tank
        :return:
        """
        system("sudo pigpiod")
        self.hp = hp
        self.pi = pigpio.pi()
        return print("started")

    def move(self, servo, pulse):
        """
        Runs the servo for 1 second and then turn it off.
        :param servo:
        :param pulse:
        :return:
        """
        """TODO see what works best when tower servo is in place
        (move each with function or move all servos in a dict/array
        
        """
        self.pi.set_servo_pulsewidth(servo, pulse)
        self.servos.append(servo)
        # maybe I could add multiple servos??
        return

    def stop_servos(self):
        """

        :param servo:
        :return:
        """
        # this should stop all servos which have been moved
        for servo in self.servos:
            self.pi.set_servo_pulsewidth(servo)
        return

    def dir_listener(self, direction):
        """

        :param direction:
        :return:
        """
        if '_' not in direction:
            if direction == 'up':
                self.move(self.r_servo, 500)
                self.move(self.l_servo, 2500)
            elif direction == 'down':
                self.move(self.r_servo, 2500)
                self.move(self.l_servo, 500)
            elif direction == 'left':
                self.move(self.l_servo, 500)
            elif direction == 'right':
                self.move(self.r_servo, 500)
        else:
            if direction == 't_right':
                pass
            elif direction == 't_left':
                pass
            elif direction == 't_up':
                pass
            elif direction == 't_down':
                pass

    def fire(self, fire):
        """

        :param fire:
        :return:
        """
        if fire:
            pass  #  activate laser

    def tower_move(self, direction):
        """

        :param direction:
        :return:
        """