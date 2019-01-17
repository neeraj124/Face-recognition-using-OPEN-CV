import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.LBPHFaceRecogniser();
rec.load('/home/pi/Desktop/Raspberry-Face-Recognition-master/trainer/trainer.yml') 
id=0;
font=cv2.FONT_HERSHEY_SIMPLEX
while (TRUE):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            print('neeraj')
        elif(id==2):
            cv2.puttext(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
    cv2.imshow('Face',img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
             
