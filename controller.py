
import pigpio
from os import system
import time
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
        self.servo_timer = None
        self.servo_direction = None

    def start(self, hp):
        """

        :param hp: integer value for HP of tank
        :return:
        """
        system("sudo pigpiod")
        self.hp = hp
        self.pi = pigpio.pi()
    
    def update(self):
        
        if self.servo_timer:
            if(time.time() - self.servo_timer) > 1:
                self.stop_servos()
                self.servo_timer = None

                print('stop')


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
        return

    def stop_servos(self):
        """
        Stops all servos which have been activated
        :param servo:
        :return:
        """
        for servo in self.servos:
            self.pi.set_servo_pulsewidth(servo, 0)
        self.servos = []
        return

    def dir_listener(self, direction):
        """

        :param direction:
        :return:
        """
        if '_' not in direction:
            if direction == 'down':
                self.move(self.r_servo, 500)
                self.move(self.l_servo, 2500)
            elif direction == 'up':
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
        
        self.servo_timer = time.time()

    def fire(self, fire):
        """

        :param fire:
        :return:
        """
        if fire:
            pass  #  activate laser
