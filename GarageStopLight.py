# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:16:09 2019
@author: Shashwat Kathuria
"""

# GARAGE STOPLIGHT PROJECT - USING RASPBERRY PI MODEL 3 B

import RPi.GPIO as GPIO
import time

# Initializing constants(GPIO pin numbers) from which trigger and echo for distance measurement takes place
TRIG = 4
ECHO = 18
    
# Initializing constants(GPIO pin numbers) for all the lights
GREEN = 17
YELLOW = 27
RED = 22

def main(): 
    # Setting warnings to flase
    GPIO.setwarnings(False)
    
    # Cleaning up the previous settings of GPIO
    GPIO.cleanup()
    
    # Setting naming convention to be BCM
    GPIO.setmode(GPIO.BCM)
    

    
    # Setting up the GPIO pins for trigger and echo
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    

    
    # Setting up the GPIO pins to output high voltages when required
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(YELLOW, GPIO.OUT)
    GPIO.setup(RED, GPIO.OUT)
    while True:
        # Getting the distance
        distance = getDistance()
        time.sleep(0.05)
        
        # Printing the distance 
        print("The distance is : " + str(distance) + " Centimeters")
        
        # Setting the appropriate light according to the distance in centimeters
        if distance >= 50:
            greenLight()
        elif distance > 20 and distance < 50:
            yellowLight()
        elif distance <= 20:
            redLight()

def getDistance():
    """Function to return the distance claculated"""
    
    # Giving output with appropriate time gap
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    # When there is no input keep initializing start time to latest 
    while GPIO.input(ECHO) == False:
        start = time.time()
    # When the input is received from trigger, get the end time
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    # Calculating the time taken 
    signalTime = end - start
    
    # Calculating the distance in centimeters
    distanceInCM = signalTime / 0.000058
    
    return distanceInCM

def greenLight():
    """Function to send high signal only for the green light"""
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)
    
def yellowLight():
    """Function to send high signal only for the yellow light"""
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    
def redLight():
    """Function to send high signal only for the red light"""
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)

if __name__ == "__main__":
    main()