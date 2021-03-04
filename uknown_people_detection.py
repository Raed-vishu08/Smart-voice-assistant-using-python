#noimport taking_sample
import pyttsx3
import os
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# engine command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#taking new samples
speak("DO YOU WANT TO TAKE NEW SAMPLES!! TYPE YES! OR  NO")
user_input=str(input("DO YOU WANT TO TAKE NEW SAMPLES :")).lower()
if user_input=='yes':
    import taking_sample
    os.system('taking_sample.py')
elif user_input=='no':
    print("Continuing with the previous data samples!!")
else:
    pass
 


data_path='C:/Users/visha/Desktop/Surveillence/faces/'
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels =[], []

for i, files in enumerate(onlyfiles):
    image_path=data_path+onlyfiles[i]
    images=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
    
Labels=np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!")


# In[12]:


import smtplib
import threading
import imutils

Email_Status = False


    
def send_mail_function():
    
    
    recipientEmail = ('ashu.bachi01@gmail.com')
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("rishu.0thakur@gmail.com", 'maygodblessu')
        server.sendmail("rishu.0thakur@gmail.com", recipientEmail, "Warning An unknown person as been reported at Home")
        print("sent to {}".format(recipientEmail))
        server.close()
    except Exception as e:
        print(e)

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    
    if faces is():
        return img, []
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h,x:x+w]
        roi=cv2.resize(roi, (200,200))
        
    return img, roi
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    
    image, face=face_detector(frame)
    
    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result=model.predict(face)
        
        if result[1]<500:
            confidence=int(100*(1-(result[1])/300))
            display_string=str(confidence)+'% Confidence it is user'
        cv2.putText(image, display_string, (100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
    
        if confidence>75:
            cv2.putText(image, "Known", (250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow("Face Cropper",image)
                       
        else:
            cv2.putText(image, "Unknown", (250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            cv2.imshow("Face Cropper",image) 
                        
            # go for weapon detection
            print("An unknown person entered!!!")             
            speak('An unknown person has been detected')           
            if Email_Status == False:
               threading.Thread(target=send_mail_function).start()
               Email_Status = True
               print("\n\n*************  EMAIL SENT TO THE OWNER  *************")
               speak('EMAIL HAS BEEN SENT TO THE OWNER')
                        
    except:
        cv2.putText(image, "Face not found", (250,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.putText(image, "Unknown", (250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow("Face Cropper",image)
        pass
    
    if cv2.waitKey(1)==13:
        break
                    
cap.release()
cv2.destroyAllWindows()

