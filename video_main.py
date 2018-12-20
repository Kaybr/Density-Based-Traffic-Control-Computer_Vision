# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""

#import numpy as np
import cv2
   
cap1 = cv2.VideoCapture("Lane1-p1-comp.mp4")
cap2 = cv2.VideoCapture("Lane2-p1-comp.mp4")
'''cap3 = cv2.VideoCapture("Lane3-p1-comp.mp4")
cap4 = cv2.VideoCapture("Lane4-p1-comp.mp4")
'''
if(cap1.isOpened() == False):
    print("Error opening cap 1")
    
if(cap2.isOpened() == False):
    print("Error opening cap 2")
'''    
if(cap3.isOpened() == False):
    print("Error opening cap 3")
    
if(cap4.isOpened() == False):
    print("Error opening cap 4")
'''    
while(cap1.isOpened() & cap2.isOpened()):    
    fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 16, detectShadows = True)
    fgbg2 = cv2.createBackgroundSubtractorKNN()
    while(True):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        '''ret3, frame3 = cap3.read()
        ret4, frame4 = cap4.read()
        '''
        if ret1 & ret2 == True:
            
            fgmask1 = fgbg2.apply(frame1)
            fgmask2 = fgbg2.apply(frame2)
            '''fgmask3 = fgbg2.apply(frame3)
            fgmask4 = fgbg2.apply(frame4)
            '''
            cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('frame1', 640, 800)
            cv2.imshow('frame1', fgmask1)
            cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('frame2', 640, 800)
            cv2.imshow('frame2', fgmask2)
            '''cv2.namedWindow('frame3', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('frame3', 640, 800)
            cv2.imshow('frame3', fgmask3)
            cv2.imshow('frame3', fgmask3)
            cv2.imshow('frame4', fgmask4)
            '''
            if cv2.waitKey(25) & 0xff == ord('q'):
                break
            
        else:
            break
    
cap1.release()
cap2.release()
'''cap3.release()
cap4.release()
'''
cv2.destroyAllWindows() 