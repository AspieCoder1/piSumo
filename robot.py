import RPi.GPIO as GPIO
import time
from bluedot import BlueDot, BlueDotPosition

bd = BlueDot()
pos = BlueDotPosition(0, 0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

def stopmotors():
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)

def forward():
    GPIO.output(9, 0)
    GPIO.output(10, 1)
    GPIO.output(7, 0)
    GPIO.output(8, 1)

def backward():
    GPIO.output(9, 1)
    GPIO.output(10, 0)
    GPIO.output(7, 1)
    GPIO.output(8, 0)

def left():
    GPIO.output(9, 0)
    GPIO.output(10, 1)
    GPIO.output(7, 1)
    GPIO.output(8, 0)

def right():
    GPIO.output(9, 1)
    GPIO.output(10, 0)
    GPIO.output(7, 0)
    GPIO.output(8, 1)

def handler(pos):
    if pos.left:
        left()
    if pos.right:
        right()
    if pos.top:
        forward()
    if pos.bottom:
        backward()

def lightUp():
    GPIO.output(24, 1)

def outOfBounds():
    if GPIO.input(25) == 0:
        stopmotors()
        lightUp()
        

stopmotors()
while True:
    bd.when_pressed = handler
    bd.when_released = stopmotors
    outOfBounds()
