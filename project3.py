import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#used haar cascade model to detect face
face = cv2.CascadeClassifier('D:\pro1\\openCV projects\\haarcascade_frontalface_default.xml')

while (1):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gra = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gra,1.3,5)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(15,0,255),2)   #drawing rectangle around the face
        face_area = frame[y:y+h,x:x+w]  #calculated the face area
        blor = cv2.GaussianBlur(face_area,(31,31),0)    #blurring only that area that is having the face
        frame[y:y+h,x:x+w] = blor   #update the face region pixels from our video with the blurred pixels
    cv2.imshow('hehehe',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
