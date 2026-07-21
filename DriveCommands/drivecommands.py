from motor import MotorController
import time

drive = MotorController()

drive.set_motor_direction(front_left =1, front_right =1, rear_right =1, rear_left = 1)

def drive_forward():
    drive.set_motors(front_left=1000, rear_left = 1000, front_right = 1000, rear_right =1000)

def drive_backward():
    drive.set_motors(front_left=-1000, rear_left = -1000, front_right = -1000, rear_right = 1000)

def slide_left():
    drive.set_motors(front_left=1000, rear_left = -1000, front_right = -1000, rear_right = 1000)

def slide_right():
    drive.set_motors(front_left=-1000, rear_left = 1000, front_right = 1000, rear_right = -1000)

def turn_left():
    drive.set_motors(front_left= -1000, rear_left = -1000, front_right = 1000, rear_right = 1000)

def turn_right():
    drive.set_motors(front_left= 1000, rear_left = 1000, front_right = -1000, rear_right = -1000)

