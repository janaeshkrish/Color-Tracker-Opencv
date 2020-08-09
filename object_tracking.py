import cv2 
import numpy as np


def nothing(x):
    pass

cv2.namedWindow('tracker')
cv2.createTrackbar('LH','tracker',0,255,nothing)
cv2.createTrackbar('LS','tracker',0,255,nothing)
cv2.createTrackbar('LV','tracker',0,255,nothing)
cv2.createTrackbar('UH','tracker',255,255,nothing)
cv2.createTrackbar('US','tracker',255,255,nothing)
cv2.createTrackbar('UV','tracker',255,255,nothing)



#cap = cv2.VideoCapture(0)
while(True):
    frame = cv2.imread(r'C:\Users\Asus\Desktop\download.jpg')
    #ret,frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos('LH','tracker')
    l_s = cv2.getTrackbarPos('LS','tracker')
    l_v = cv2.getTrackbarPos('LV','tracker')
    
    u_h = cv2.getTrackbarPos('UH','tracker')
    u_s = cv2.getTrackbarPos('US','tracker')
    u_v = cv2.getTrackbarPos('UV','tracker')
    
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv,l_b,u_b)
    
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    
    
    cv2.imshow('original',frame)
    cv2.imshow('result',res)
    cv2.imshow('mask',mask)
    k=cv2.waitKey(1) & 0xFF 
    if k == ord('q'):
        break
#cap.release()
cv2.destroyAllWindows()