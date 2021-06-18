#https://www.raspberrypi.org/forums/viewtopic.php?t=253184
import time
import math

from adafruit_servokit import ServoKit
from mpu6050 import mpu6050

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

sensor = mpu6050(0x68,bus=3)
kit = ServoKit(channels=16)

kit.servo[0].angle = 90;
kit.servo[1].angle = 100;
kit.servo[2].angle = 87;
kit.servo[3].angle = 70;
kit.servo[4].angle = 80;
kit.servo[5].angle = 110;
kit.servo[6].angle = 0;
kit.servo[7].angle = 0;


while(True):
    gyro_data = sensor.get_accel_data()
    xaxis = get_x_rotation(gyro_data['x'], gyro_data['y'], gyro_data['z'])
    yaxis = get_y_rotation(gyro_data['x'], gyro_data['y'], gyro_data['z'])
    print("X Rotation: ", xaxis)
    print("Y Rotation: ", yaxis)
    if (xaxis > 5):
        kit.servo[0].angle = 30;
        kit.servo[1].angle = 60;
    elif (xaxis < -5):
        kit.servo[0].angle = 150;
        kit.servo[1].angle = 180;
    elif (yaxis > 5):
        kit.servo[2].angle = 30;
        kit.servo[3].angle = 10;
    elif (yaxis < -5):
        kit.servo[2].angle = 150;
        kit.servo[2].angle = 150;
    if (xaxis > 0 and xaxis < 3):
        kit.servo[0].angle = 30;
        kit.servo[1].angle = 60;
    if (yaxis > -2 and yaxis < 0):
        kit.servo[2].angle = 87;
        kit.servo[2].angle = 70;
