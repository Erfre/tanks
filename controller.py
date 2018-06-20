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
        #self.servos.append(dir)
        self.servos = list(set(self.servos))
        #self.servo_time = time.time()
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

        :param direction: Dictionary
        :return:
        """

        if direction['38']:
            #up
            self.move(self.l_servo, 1800)
            self.move(self.r_servo, 1200)
        if direction['40']:
            # down
            self.move(self.l_servo, 1200)
            self.move(self.r_servo, 1800)
        if direction['37']:
            # turn left
            self.move(self.l_servo, 500)

        if direction['39']:
            # right
            self.move(self.r_servo, 2500)

        if not any(direction.itervalues()):
            self.move(self.r_servo, 0)
            self.move(self.l_servo, 0)

        # if '_' not in direction:
        #     #print(self.servos)
        #     if 'up' in direction:
        #         if 'left' in direction:
        #             # lower speed on left side
        #
        #             self.move(self.l_servo, 1200, direction)
        #             self.move(self.r_servo, 2500, direction)
        #             #print(self.servos)
        #         elif 'right' in direction:
        #             # lower speed on right side
        #             self.move(self.l_servo, 500, direction)
        #             self.move(self.r_servo, 1800, direction)
        #         else:
        #             self.move(self.r_servo, 1800, direction)
        #             self.move(self.l_servo, 1200, direction)
        #     elif 'down' in direction:
        #         if 'left' in direction:
        #             # lower speed on left side
        #             self.move(self.l_servo, 2500, direction)
        #             self.move(self.r_servo, 1200, direction)
        #         elif 'right' in direction:
        #             # lower speed on right side
        #             self.move(self.l_servo, 1800, direction)
        #             self.move(self.r_servo, 500, direction)
        #         else:
        #             self.move(self.r_servo, 1200, direction)
        #             self.move(self.l_servo, 1800, direction)
        #     elif 'left' in direction:
        #         if 'right' in self.servos:
        #             self.move(self.l_servo, 2500, direction)
        #             self.move(self.r_servo, 2500, direction)
        #         else:
        #             self.move(self.l_servo, 500, direction)
        #     elif 'right' in direction:
        #         if 'left' in self.servos:
        #             self.move(self.r_servo, 500, direction)
        #             self.move(self.l_servo, 500, direction)
        #         else:
        #             self.move(self.r_servo, 2500, direction)
        # else:
        #     if direction == 'tower_right':
        #
        #         if self.t_servo_angle > 550:
        #             self.t_servo_angle -= 50
        #             self.move_tower(self.t_servo, self.t_servo_angle)
        #
        #     elif direction == 'tower_left':
        #
        #
        #         if self.t_servo_angle < 2450:
        #             self.t_servo_angle += 50
        #             self.move_tower(self.t_servo, self.t_servo_angle)
        #
        #     elif direction == 't_up':
        #         pass
        #     elif direction == 't_down':
        #         pass
        #
        # self.servo_timer = time.time()
