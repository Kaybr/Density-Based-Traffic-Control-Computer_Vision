# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
import cv2
import numpy as np
from regionOfInterest import roi
from modified_canny import mod_canny
#from linesCorrection import draw_lines

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 0)
    processed_img = mod_canny(processed_img, sigma = 0.75)
    vertices = np.array([[0,327], [265,58], [312,58], [474,327]], np.int32)
    processed_img = roi(processed_img, [vertices])
    
    #lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    #draw_lines(processed_img, lines)
    return processed_img
