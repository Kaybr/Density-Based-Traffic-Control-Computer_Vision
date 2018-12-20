import cv2
import time

def calc_white4():
    cap4 = cv2.VideoCapture("Lane4-p1-comp.mp4")

    if(cap4.isOpened() == False):
        print("Error opening cap4")
        
    if(cap4.isOpened()):    
        fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 100, detectShadows = True)
        fgbg2 = cv2.createBackgroundSubtractorKNN()
        count = 0
        start = time.time()
    while(count <= 50):
        ret4, frame4 = cap4.read()
        count = count + 1
        fgmask = fgbg.apply(frame4)
        cv2.namedWindow('frame4', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame4', 640, 800)
        cv2.imshow('frame4', fgmask)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    end = time.time()

    fps = count/(end - start)
    print("FPS Value: ", fps)

    white = cv2.countNonZero(fgmask)
    print(white, " in frame - ", count)
    
    cap4.release()

    cv2.destroyAllWindows()

    return white
