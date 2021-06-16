#https://www.raspberrypi.org/forums/viewtopic.php?t=253184
import time

from adafruit_servokit import ServoKit
from mpu6050 import mpu6050
sensor = mpu6050(0x68,bus=3)
kit = ServoKit(channels=16)

while(True):
    gyro_data = sensor.get_gyro_data()
    if (gyro_data['x'] > 3):
        kit.servo[].angle = ;
        kit.servo[].angle = ;
    elif (gyro_data['x'] < -3):
        kit.servo[].angle = ;
        kit.servo[].angle = ;
    elif (gyro_data['y'] > 3):
        kit.servo[].angle = ;
        kit.servo[].angle = ;
    elif (gyro_data['y'] < -3):
        kit.servo[].angle = ;
        kit.servo[].angle = ;
