

import pyttsx3
import numpy as np 
import cv2 
import imutils 
import datetime 
import smtplib
import playsound
import threading
import os 

# engine command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

gun_cascade = cv2.CascadeClassifier('cascade.xml') 
camera = cv2.VideoCapture('robbery.mp4') 



Email_Status = False

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def send_mail_function():
        securityEmail = "sreyasreedokala@gmail.com"
        securityEmail = securityEmail.lower()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("rishu.0thakur@gmail.com", 'maygodblessu')
            server.sendmail('rishu.0thakur@gmail.com', securityEmail, "Warning An unknown person with gun as been reported at Home")
            print("sent to {}".format(securityEmail))
            server.close()
        except Exception as e:
            print(e)

firstFrame = None
gun_exist = False
   
while True: 
      
    ret, frame = camera.read() 
   
    frame = imutils.resize(frame, width = 500) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
       
    gun = gun_cascade.detectMultiScale(gray, 
                                       1.3, 5, 
                                       minSize = (100, 100)) 
       
    if len(gun) > 0: 
        gun_exist = True
           
    for (x, y, w, h) in gun: 
          
        frame = cv2.rectangle(frame, 
                              (x, y), 
                              (x + w, y + h), 
                              (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w]     
   
    if firstFrame is None: 
        firstFrame = gray 
        continue
   
   
    cv2.imshow("Security Feed", frame) 
    
    if gun_exist: 
            
            #print("guns detected")
           
            if Email_Status == False:
                threading.Thread(target=send_mail_function).start()
                Email_Status = True
                print("\n\n*************  EMAIL SENT TO THE SECURITY *************")
                speak("Warning!!! gun has been detected")
                speak("email has been sent to the security")
                print("guns detected")
    else: 
         pass 
         
   
    key = cv2.waitKey(1) & 0xFF
      
    if key == ord('q'): 
        break
     

camera.release() 
cv2.destroyAllWindows()
