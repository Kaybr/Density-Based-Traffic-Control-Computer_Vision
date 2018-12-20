# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyscreenshot as ImageGrab
import cv2
import numpy as np

while(True):
    image = np.array(ImageGrab.grab(bbox = (35, 200, 888, 675)))
    cv2.imshow('window', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.imwrite('stored image.png', image)
        cv2.destroyAllWindows()
        break

