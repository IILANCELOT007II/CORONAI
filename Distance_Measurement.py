#######################################
############||LANCELOT||###############
#######################################



import cv2
import numpy as np


img = cv2.imread(#image)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detect_face = face.detectMultiScale(gray, 1.2, 1)

for (x,y,w,h) in detect_face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    ROI = gray[x:x+w, y:y+h]
    length = ROI.shape[0]
    breadth = ROI.shape[1]
    Area = length * breadth
    Distance = 149 - 1.08*(10**(-3))*Area + 2.59*(10**(-9))*(Area**2)
    Distance = round(Distance,2)
    display = str(Distance)
    if Area > 0:
        cv2.putText(img, display, (x, y-10), font, 0.5, (255, 255, 0), 2, cv2.LINE_AA)
        
        
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
