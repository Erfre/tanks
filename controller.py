import pigpio
from os import system
from time import sleep

class controller:
    """The tank class"""
    def __init__(self, right_servo, left_servo, tower_servo, cannon_servo, laser):
        """

        :param right_servo:
        :param left_servo:
        :param tower_servo:
        :param cannon_servo:
        :param laser:
        """
        self.r_servo = right_servo
        self.l_servo = left_servo
        self.t_servo = tower_servo
        self.c_servo = cannon_servo
        self.laser = laser
        self.pi = None
        self.hp = 0

    def start(self, hp):
        """

        :param hp:
        :param server:
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

        self.pi.set_servo_pulsewidth(servo, pulse)
        # maybe I could add multiple servos??
        return

    def stop(self, servo):
        """

        :param servo:
        :return:
        """
        self.pi.set_servo_pulsewidth(servo, 0)
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
                sleep(1)
                self.stop(self.l_servo)
                self.stop(self.r_servo)
            elif direction == 'down':
                self.move(self.r_servo, 2500)
                self.move(self.l_servo, 500)
                sleep(1)
                self.stop(self.l_servo)
                self.stop(self.r_servo)
            elif direction == 'left':
                self.move(self.l_servo, 500)
                sleep(1)
                self.stop(self.l_servo)
            elif direction == 'right':
                print("now im right")
                self.move(self.r_servo, 1500)
                sleep(1)
                self.stop(self.r_servo)
        else:
            if  direction == 't_right':
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