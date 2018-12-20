# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 22:42:33 2018

@author: satya
"""

import RPi.GPIO as GPIO
import time
import math
import random
from Lane1 import calc_white1
from Lane2 import calc_white2
from Lane3 import calc_white3
from Lane4 import calc_white4
#from  main import white array --- yet to be created
'''
white1 = calc_white1() / 50000
white2 = random.random()
white3 = random.random()
white4 = random.random()
'''
GREEN1 = 31
GREEN2 = 33
GREEN3 = 35
GREEN4 = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(GREEN1,GPIO.OUT)
GPIO.setup(GREEN2,GPIO.OUT)
GPIO.setup(GREEN3,GPIO.OUT)
GPIO.setup(GREEN4,GPIO.OUT)

greenList = [GREEN1,GREEN2,GREEN3,GREEN4]

try:
    i = 0
    while True:
        white1 = calc_white1() / 50000
        white2 = calc_white2() / 50000
        white3 = calc_white3() / 50000
        white4 = calc_white4() / 50000
        '''lane1 = (1*ir1 + 0.5*ir2 + 0.25*ir3 + 0.125*ir4)
        lane2 = (1*ir5 + 0.5*ir6 + 0.25*ir7)
        lane3 = (1*ir8 + 0.5*ir9 + 0.25*ir10)
        lane4 = (1*ir11 + 0.5*ir12 + 0.25*ir13)'''
        
        #print(lane1)
        #print(lane2)
        
        #laneList = [lane1, lane2, lane3, lane4]
        laneList = [white1, white2, white3, white4]
        duration = 5*laneList[i%4] + 15
        print("Duration of GREEN of lane ",(i%4)+1,"is ",duration)
        #totalDuration = (lane1 + lane2 + lane3 + lane4)*5 + 5
        totalDuration = (white1 + white2 + white3 + white4)*5 + 15
        speed = 135*18/(5*duration) + 20
        print("Recommended Speed: ",math.ceil(speed),"km/hr")
        GPIO.output(greenList[i%4],GPIO.HIGH)
        GPIO.output(greenList[(i+1)%4],GPIO.LOW)
        GPIO.output(greenList[(i+2)%4],GPIO.LOW)
        GPIO.output(greenList[(i+3)%4],GPIO.LOW)
        
        i = i + 1
        time.sleep(duration)
        GPIO.output(greenList[(i-1)%4],GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.cleanup()
