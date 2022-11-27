import cv2
from detect import VideoTracker
import numpy as np
import time
from utils.parser import get_config
import re
import os
import json

class Config:
    def __init__(self):
        #self.OUTPUTDIR="./output"
        self.YOLOWEIGHT="./weights/yolov5x.pt"
        self.CARSPEEDLIMIT=25
        self.TRAFFICJAMLIMIT=16
        self.SAVEVIDEO=True
        self.CARCLASSIFY=True
        self.forwardline=[]
        self.leftline=[]
        self.rightline=[]
        self.leftlight=[]
        self.forwardlight=[]
        self.rightlight=[]
        self.trafficline1=[]
        self.trafficline2=[]
        self.preflag=[]
        self.laneline=[]
    def initConfig(self):
        self.forwardline=[]
        self.leftline=[]
        self.rightline=[]
        self.leftlight=[]
        self.forwardlight=[]
        self.rightlight=[]
        self.trafficline1=[]
        self.trafficline2=[]
        self.laneline=[]
        #self.preflag=[]

def OnMouseAction(event,x,y,flags,param):
    if len(xyxy)==4 and id<8 and id>2:
        return
    if len(xyxy)==8 and id>=0 and id<=2:
        return
    if event==cv2.EVENT_LBUTTONDOWN:
        xyxy.append(x)
        xyxy.append(y)
        #imgTmp=self.img.copy()
        cv2.circle(imgTmp, (x, y), 2, (0,250,0), 2)
        cv2.imshow(str(id),imgTmp)

vdo = cv2.VideoCapture("./video.avi")
img = None
while vdo.grab():
    _, img = vdo.retrieve()

    # if img!=None:
    break
x, y = img.shape[0:2]
img = cv2.resize(img, (int(y / 2), int(x / 2)))
vdo.release()
config=Config()
config.preflag = [1,1,1,1,1,1,0,0,1]
for i in range(len(config.preflag)):
    xyxy = []
    id = i
    if config.preflag[i] == 1:
        cv2.namedWindow(str(i))
        imgTmp = img.copy()
        cv2.setMouseCallback(str(i), OnMouseAction)
        cv2.imshow(str(id), img)
        # k=cv2.waitKey(-1)

        flag = 0
        if cv2.waitKey(0) == ord('y'):
            if i == 0:
                for i in xyxy:
                    config.forwardline.append(i * 2)
            elif i == 1:
                for i in xyxy:
                    config.leftline.append(i * 2)
            elif i == 2:
                for i in xyxy:
                    config.rightline.append(i * 2)
            elif i == 3:
                for i in xyxy:
                    config.forwardlight.append(i * 2)
            elif i == 4:
                for i in xyxy:
                    config.leftlight.append(i * 2)
            elif i == 5:
                for i in xyxy:
                    config.rightlight.append(i * 2)
            elif i == 6:
                for i in xyxy:
                    config.trafficline1.append(i * 2)
            elif i == 7:
                for i in xyxy:
                    config.trafficline2.append(i * 2)
            elif i == 8:
                for i in xyxy:
                    config.laneline.append(i * 2)
            # print("ok")
            # xyxy=[]
            flag = 1
            cv2.destroyAllWindows()
            # break

print(config.preflag)
print(config.forwardline)
print(config.leftline)

cfg = get_config()
cfg.merge_from_file("./configs/deep_sort.yaml")
videoTracker=VideoTracker(cfg)
videoTracker.run("./video.avi",config)

