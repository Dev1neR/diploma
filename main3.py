#https://www.raspberrypi.org/forums/viewtopic.php?t=253184
import time
import pygame

from adafruit_servokit import ServoKit
#from mpu6050 import mpu6050
#sensor = mpu6050(0x68,bus=3)
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
    kit.servo[2].angle = 90
    kit.servo[3].angle = 65
    kit.servo[0].angle = 45
    kit.servo[1].angle = 150
    kit.servo[6].angle = 0
    kit.servo[7].angle = 180
  elif x == "s":
    print("backwards")
    kit.servo[2].angle = 90
    kit.servo[3].angle = 65
    kit.servo[0].angle = 150
    kit.servo[1].angle = 45
    kit.servo[6].angle = 180
    kit.servo[7].angle = 0
  elif x == "r":
    print("reset")
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 65
    kit.servo[4].angle = 80
    kit.servo[5].angle = 110
    kit.servo[6].angle = 0
    kit.servo[7].angle = 0
  elif x == "f":
    print("wall")
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 65
    kit.servo[4].angle = 80
    kit.servo[5].angle = 110
    #kit.servo[6].angle = 90
    #kit.servo[7].angle = 90
  else:
    return -1

kit.servo[3].angle = 65
kit.servo[4].angle = 80
kit.servo[5].angle = 110

#accelerometer_data = sensor.get_accel_data()
#print(accelerometer_data)
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
            if event.key == pygame.K_f:
                menu("f")