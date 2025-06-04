import cv2 as cv 
import mediapipe as mp
import time
import numpy as np
import hand as hd
import math
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume = cast(interface,POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxvol = volRange[1]

cap = cv.VideoCapture(0)
detector = hd.HandDetector()
ptime = 0

while True:

    success , img = cap.read()
    detector.findHands(img , True)
    lm=detector.getposition(img , True)
    if(len(lm) != 0 ):
        # print(lm[8],lm[12])
        x1,y1 = lm[8][1],lm[8][2]
        x2,y2 = lm[12][1],lm[12][2]
        cv.circle(img,(x1,y1),10,(0,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),10,(0,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),thickness=10)
        length = math.hypot(x2-x1,y2-y1)
        vol = np.interp(length,[25,100],[minVol,maxvol])
        volume.SetMasterVolumeLevel(vol,None)

    cTime = time.time()
    fps = 1/(cTime-ptime)
    ptime = cTime

    cv.putText(img, f'FPS: {int(fps)}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0,0), 2)
    cv.imshow("volumecontrol",img)

    if cv.waitKey(1) & 0XFF==ord("q"):
        cv.destroyAllWindows()
        break




