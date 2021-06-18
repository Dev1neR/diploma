#https://www.raspberrypi.org/forums/viewtopic.php?t=253184
import time
import pygame

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

kit.servo[6].set_pulse_width_range(800, 2300)
kit.servo[7].set_pulse_width_range(800, 2300)
        
def menu(x):
  if x == "a":
    print("left")  
    kit.servo[4].angle = 50
    kit.servo[5].angle = 30
    kit.servo[8].angle = 50
    kit.servo[9].angle = 50
  elif x == "d":
    print("right")
    kit.servo[4].angle = 160
    kit.servo[5].angle = 140
    kit.servo[8].angle = 110
    kit.servo[9].angle = 110
  elif x == "w":
    print("forward")   
    kit.servo[2].angle = 87
    kit.servo[3].angle = 70
    if (xaxis > 3):
        kit.servo[0].angle = 180
        kit.servo[1].angle = 170
        kit.servo[6].angle = 170
        kit.servo[7].angle = 170
    else:
        kit.servo[0].angle = 140
        kit.servo[1].angle = 140
        kit.servo[6].angle = 130
        kit.servo[7].angle = 130
  elif x == "s":
    print("backwards")
    kit.servo[2].angle = 87
    kit.servo[3].angle = 70
    kit.servo[0].angle = 45
    kit.servo[1].angle = 45
    kit.servo[6].angle = 170
    kit.servo[7].angle = 170
  elif x == "r":
    print("reset")
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[2].angle = 87
    kit.servo[3].angle = 70
    kit.servo[4].angle = 80
    kit.servo[5].angle = 110
    kit.servo[6].angle = 0
    kit.servo[7].angle = 0
  else:
    return -1
kit.servo[2].angle = 87
kit.servo[3].angle = 70
kit.servo[4].angle = 80
kit.servo[5].angle = 110

kit.servo[6].angle = 180
time.sleep(0.3)
kit.servo[7].angle = 180
time.sleep(0.5)
kit.servo[6].angle = 0
kit.servo[7].angle = 0

pygame.init()
screen = pygame.display.set_mode((400,400))

done = False
while not done:
    gyro_data = sensor.get_accel_data()
    xaxis = get_x_rotation(gyro_data['x'], gyro_data['y'], gyro_data['z'])
    yaxis = get_y_rotation(gyro_data['x'], gyro_data['y'], gyro_data['z'])
    print("X Rotation: ", xaxis)
    print("Y Rotation: ", yaxis)
    time.sleep(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                menu("w")
            if event.key == pygame.K_s:
                menu("s")
            if event.key == pygame.K_a:
                menu("a")
            if event.key == pygame.K_d:
                menu("d")
            if event.key == pygame.K_r:
                menu("r")
