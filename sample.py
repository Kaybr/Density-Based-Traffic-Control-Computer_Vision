# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 100, detectShadows = True)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
fgbg2 = cv2.bgsegm.createBackgroundSubtractorGMG()
 
if(cap.isOpened() == False):
    print("Error opening cap")
    
while(True):
        ret, frame = cap.read()
        fgmask1 = fgbg.apply(frame)
        #fgmask1 = fgbg2.apply(frame)
        #fgmask1 = cv2.morphologyEx(fgmask1, cv2.MORPH_OPEN, kernel)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', fgmask1)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()
        
