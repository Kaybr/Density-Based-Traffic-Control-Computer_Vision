# -*- coding: utf-8 -*-
import cv2

frame = cv2.imread("Lane1-p1-ref.png")
fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 16, detectShadows = True)
fgmask = fgbg.apply(frame)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 640, 800)
cv2.imshow('frame', fgmask)
cv2.waitKey(0)