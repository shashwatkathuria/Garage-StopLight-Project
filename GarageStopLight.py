import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def getDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    signalTime = end - start
    
    distanceInCM = signalTime / 0.000058
    
    return distanceInCM


GREEN = 17
YELLOW = 27
RED = 22

GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

def greenLight():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)
    
def yellowLight():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    
def redLight():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)

while True:
    
    distance = getDistance()
    time.sleep(0.05)
    print("The distance is : " + str(distance) + " Centimeters")
    
    if distance >= 50:
        greenLight()
    elif distance > 20 and distance < 50:
        yellowLight()
    elif distance <= 20:
        redLight()
        
    