# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
#import numpy as np
#from PIL import ImageGrab
import cv2
#from process_img import process_img
from blob_detection import detect_blob
from regionOfInterest import roi
import numpy as np

def main():
    #path = 'D:\\Study\\SEM VIII\\FYP\\Density Based Traffic Control using Image Processing\\output_images\\'
    screen = cv2.imread('sample2_img.jpg')
    #new_screen = process_img(screen)
    #cv2.imwrite(path + 'op6.jpg', new_screen)
    
    blob_detected = detect_blob(screen)
    
    #height, width =  blob_detectedaa.shape
    #print "Total Pixels = %d" % (height * width)
    vertices = np.array([[0,327], [265,58], [312,58], [474,327]], np.int32)
    image = roi(blob_detected, [vertices])
    image = cv2.bitwise_not(image)
    cv2.imshow('Blob-Detected', image)
    cv2.waitKey(0)
    white = cv2.countNonZero(blob_detected)
    print white
    cv2.destroyAllWindows()

main()