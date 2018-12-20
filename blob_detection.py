# -*- coding: utf-8 -*-

import cv2
import numpy as np
from regionOfInterest import roi

def detect_blob(image):
    '''satyanrayan pande-
    THRESHOLD_SENSITIVITY = 50
    hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    (_, _, grayFrame) = cv2.split(hsvFrame)
    grayFrame = cv2.GaussianBlur(grayFrame, (21, 21), 0)
    
    retval, thresholdImage = cv2.threshold(grayFrame, THRESHOLD_SENSITIVITY, 255, cv2.THRESH_BINARY)
    #thresholdImage = cv2.dilate(thresholdImage, None, iterations=2)
    cv2.imshow("threshold", thresholdImage)
    
    contours, hierarchy = cv2.findContours(thresholdImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours
    --end'''
    '''by sameer mandaogade'''
    hue ,saturation ,value = cv2.split(image)
    retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    medianFiltered = cv2.medianBlur(thresholded,5)
    #_, contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    return medianFiltered
    