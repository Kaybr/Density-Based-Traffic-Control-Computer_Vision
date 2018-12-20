import cv2
import urllib2
import numpy as np
import sys
from process_img import process_img

host = "192.168.0.101:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
print 'Streaming ' + hoststr

stream=urllib2.urlopen(hoststr)
fgbg = cv2.BackgroundSubtractorMOG()
#fgbg2 = cv2.BackgroundSubtractorMOG(history = 500, nmixtures = 6, backgroundRatio = 0.9, noiseSigma = 1)

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        screen = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        fgmask = fgbg.apply(screen)
                
        #new_screen = process_img(screen)
        
        cv2.imshow('frame', fgmask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)
            break
