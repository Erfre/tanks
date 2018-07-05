import pigpio
import threading
from os import system
import time


class controller():
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
        self.servo_timer_tower = None
        self.servo_direction = None
        self.tower_thread = None
        self.t_servo_angle = 1500

        #self.move(self.t_servo, self.t_servo_angle)


    def start(self, hp):
        """

        :param hp: integer value for HP of tank
        :return:
        """
        system("sudo pigpiod")
        print("Livestream and pigpiod started.")
        self.hp = hp
        self.pi = pigpio.pi()
    

    def move(self, servo, pulse):
        """
        Runs the servo for 1 second and then turn it off.
        :param servo:
        :param pulse:
        :return:
        """

        self.pi.set_servo_pulsewidth(servo, pulse)
        #self.servos.append(dir)
        self.servos = list(set(self.servos))
        #self.servo_time = time.time()
        return

    def thread_tower(self, pulse):
        """
        Moves the tower in degrees which are converted from the servo pulse
        :return:
        """
        #servo_pulse = 11

        while True:
            self.t_servo_angle += pulse
            if self.t_servo_angle < 2500 or self.t_servo_angle > 500:
                self.move(self.t_servo, self.t_servo_angle)
            else:
                print('No more moves in this direction')
                return
            pulse += pulse

    def move_tower(self, pulse):
        """
        Moves the tower in degrees which are converted from the servo pulse
        :return:
        """
        #servo_pulse = 11
        self.t_servo_angle = self.t_servo_angle + pulse
        if self.t_servo_angle < 2500 or self.t_servo_angle > 500:
            self.move(self.t_servo, self.t_servo_angle)

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

    def fire(self):
        """
        moves the tank tank back and then forward
        :return:
        """
        # might want to check the timer for servos?
        self.move(self.l_servo, 2500)
        self.move(self.r_servo, 500)
        time.sleep(0.2)
        self.stop_servos()
        # maybe a delay here, try a sleep one
        self.move(self.l_servo, 500)
        self.move(self.r_servo, 2500)
        time.sleep(0.1)
        self.stop_servos()

    def dir_listener(self, direction):
        """

        :param direction: Dictionary
        :return:
        """
        if direction['32']:
            #if the tank shoots move it back
            self.fire()

        if direction['87']:
            #up
            self.move(self.l_servo, 2000)
            self.move(self.r_servo, 1000)
        elif direction['83']:
            # down
            self.move(self.l_servo, 1000)
            self.move(self.r_servo, 2000)
        else:
            self.stop_servos()
        if direction['65']:
            # turn left
            self.move(self.l_servo, 500)

        if direction['68']:
            # right
            self.move(self.r_servo, 2500)

        if direction['37']:
            #tower left increase
            #self.move(self.t_servo,)
            #self.tower_thread = threading.Thread(target=self.thread_tower, args=(11,)).start()
            self.move_tower(11)
        elif direction['37']:
            #self.tower_thread._stop()
            #stop thread
            pass
        if direction['39']:
            #tower right
            #self.move(self.t_servo,)
            self.move_tower(-11)
        elif direction['39']:
            #stop thread
            pass

        if all(value == 0 for value in direction.values()):
            self.move(self.r_servo, 0)
            self.move(self.l_servo, 0)
