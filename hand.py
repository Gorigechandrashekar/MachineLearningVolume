import cv2 as cv
import mediapipe as mp
import time

class HandDetector():
    def __init__(self, mode = False, maxHands = 2 , detection = 0.5 , trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detection = detection
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.Hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.Hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)
    def getposition(self,img,draw=True):
        li=[]
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                for id,lm in enumerate(handlms.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    li.append([id,cx,cy])
        return li
    
cap=cv.VideoCapture(0)
ptime=0

# while True:
#     success,img=cap.read()
#     detector=HandDetector()
#     detector.findHands(img,draw=True)
#     li=detector.getposition(img,draw=True)
#     print(li)
#     cTime=time.time()
#     fps=1/(cTime-ptime)
#     ptime=cTime
#     cv.putText(img,str(int(fps)),(50,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
#     cv.imshow("reading hand",img)


#     if cv.waitKey(20) & 0xFF==ord('q'):
#         cv.destroyAllWindows()
#         break
