
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
        system("""uv4l -nopreview --auto-video_nr --driver raspicam --encoding
        mjpeg --width 640 --height 480 --framerate 20 --hflip=yes --vflip=yes
        --bitrate=2000000 --server-option '--port=8080' --server-option
        '--max-queued-connections=30' --server-option '--max-streams=25'
        --server-option '--max-threads=29'""")
        print("Livestream and pigpiod started.")
        self.hp = hp
        self.pi = pigpio.pi()
    
    def update(self):
       

        if self.servo_timer:
            if(time.time() - self.servo_timer) > 0.5:
                self.stop_servos()
                self.servo_timer = None

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
        self.servo_time = time.time()
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
                self.move(self.r_servo, 500)
            elif direction == 'right':
                self.move(self.r_servo, 2500)
                self.move(self.l_servo, 2500)
        else:
            if direction == 'tower_right':
                if self.t_servo_angle > 550:
                    self.t_servo_angle -= 50
                    self.move(self.t_servo, self.t_servo_angle) 
            elif direction == 'tower_left':
                if self.t_servo_angle < 2450:
                    self.t_servo_angle += 50  
                    self.mover(self.t_servo, self.t_servo_angle)
            elif direction == 't_up':
                pass
            elif direction == 't_down':
                pass
        
        self.servo_timer = time.time()
