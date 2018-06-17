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
        self.servo_timer = None
        self.servo_timer_tower = None
        self.servo_direction = None
        self.t_servo_angle = 1500

        #self.move(self.t_servo, self.t_servo_angle)


    def start(self, hp):
        """

        :param hp: integer value for HP of tank
        :return:
        """
        system("sudo pigpiod")
        print("tank started")
        self.hp = hp
        self.pi = pigpio.pi()
    
    def update(self):
        self.stop_servos()

       # if self.servo_timer:
       #     if(time.time() - self.servo_timer) > 0.5:
       #         self.stop_servos()
       #         self.servo_timer = None

    def move(self, servo, pulse, dir):
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
        self.servos.append(dir)
        self.servo_time = time.time()
        return

    def move_tower(self, servo, pulse):

        self.pi.set_servo_pulsewidth(servo, pulse)
    
    def stop_servos(self):
        """
        Stops all servos which have been activated
        :param servo:
        :return:
        """
        self.pi.set_servo_pulsewidth(self.r_servo, 0)
        self.pi.set_servo_pulsewidth(self.l_servo, 0)
        self.servos = []
        return

    def dir_listener(self, direction):
        """

        :param direction:
        :return:
        """
        if '_' not in direction:
            if direction == 'down':
                self.move(self.r_servo, 900, direction)
                self.move(self.l_servo, 2000, direction)

            elif direction == 'up':
                if 'right' or 'left' not in self.servos:
                    self.move(self.r_servo, 2000, direction)
                    self.move(self.l_servo, 900, direction)
                elif 'right' in self.servos:
                    self.move(self.l_servo, 2000, direction)
                elif 'left' in self.servos:
                    self.move(self.r_servo, 900, direction)

            elif direction == 'left':
                self.move(self.l_servo, 500, direction)
            elif direction == 'right':
                self.move(self.r_servo, 2500, direction)
        else:
            if direction == 'tower_right':
                
                if self.t_servo_angle > 550:
                    self.t_servo_angle -= 50
                    self.move_tower(self.t_servo, self.t_servo_angle) 

            elif direction == 'tower_left':
                

                if self.t_servo_angle < 2450:
                    self.t_servo_angle += 50
                    self.move_tower(self.t_servo, self.t_servo_angle)

            elif direction == 't_up':
                pass
            elif direction == 't_down':
                pass
        
        self.servo_timer = time.time()
