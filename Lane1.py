import cv2
import time

def calc_white1(): 
    cap1 = cv2.VideoCapture("Lane1-p1-comp.mp4")

    if(cap1.isOpened() == False):
        print("Error opening cap 1")
        
    if(cap1.isOpened()):    
        fgbg = cv2.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 100, detectShadows = True)
        fgbg2 = cv2.createBackgroundSubtractorKNN()
        count = 0
        start = time.time()
    while(count <= 50):
        ret1, frame1 = cap1.read()
        count = count + 1    
        fgmask1 = fgbg.apply(frame1)
        cv2.namedWindow('frame1', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame1', 640, 800)
        cv2.imshow('frame1', fgmask1)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    end = time.time()

    fps = count/(end - start)
    print("FPS Value: ", fps)

    white = cv2.countNonZero(fgmask1)
    print(white, " in frame - ", count)

    cap1.release()

    cv2.destroyAllWindows()

    return white
