import cv2
import numpy as np
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)
'''while True:
    ret,frame= cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #hue set value
    lowvalue=np.array([100,30,150])
    upvalue=np.array([255,255,255])
    mask=cv2.inRange(hsv,lowvalue,upvalue)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    result=cv2.resize(result,(800,800))
    cv2.imshow('original',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    k=cv2.waitKey(27)&0xFF
    if k== 27:
        break
cv2.destroyAllWindows()
cap.release()'''
if cap.isOpened():
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    plt.imshow(hsv)
    plt.show()
    
