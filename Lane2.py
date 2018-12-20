import cv2
import time

def calc_white2():
    cap2 = cv2.VideoCapture("Lane1-p1-comp.mp4")

    if(cap2.isOpened() == False):
        print("Error opening cap2")
        
    if(cap2.isOpened()):    
        fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 100, detectShadows = True)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        fgbg2 = cv2.bgsegm.createBackgroundSubtractorGMG()
        count = 0
        start = time.time()
    while(True):
        ret2, frame2 = cap2.read()
        count = count + 1
        fgmask = fgbg2.apply(frame2)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.namedWindow('frame2', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame2', 640, 800)
        cv2.imshow('frame2', fgmask)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    end = time.time()

    fps = count/(end - start)
    print("FPS Value: ", fps)

    white = cv2.countNonZero(fgmask)
    print(white, " in frame - ", count)
    
    cap2.release()

    cv2.destroyAllWindows()

    return white

calc_white2()