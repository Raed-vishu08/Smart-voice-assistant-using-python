


import os
import cv2
import numpy as np
import smtplib
import playsound 
#import winsound
import threading
import pyttsx3

# engine command
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



Email_Status = False
Fire_Reported = 0

# def play_alarm_sound_function(): 
#   while True:
#        playsound.playsound('Alarm Sound.wav',True)
#       # # sound.play_effect(Alarm Sound[, volume, pitch=1.0, pan=0.0, looping=False])
#       # wave_obj = sa.WaveObject.from_wave_file('Alarm Sound.wav')
#       # play_obj = wave_obj.play()
#       # play_obj.stop()
def send_mail_function():

  recipientEmail = "vishufeb786@gmail.com"
  recipientEmail = recipientEmail.lower()

  try:
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login("rishu.0thakur@gmail.com", 'maygodblessu')
      server.sendmail('rishu.0thakur@gmail.com', recipientEmail, "Warning A Fire Accident has been reported at Home")
      print("sent to {}".format(recipientEmail))
      server.close()
  except Exception as e:
      print(e)


#video = cv2.VideoCapture('fire_video.mp4') # If you want to use webcam use Index like 0,1.
video = cv2.VideoCapture(0) # If you want to use webcam use Index like 0,1.
 
#while True:
while video.isOpened():
  grabbed, frame = video.read()
  if not grabbed:
      print("no frame:")
      break

  frame = cv2.resize(frame, (960, 540)) 
 
  blur = cv2.GaussianBlur(frame, (21, 21), 0)
  hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
  lower = [18, 50, 50]
  upper = [35, 255, 255]
  lower = np.array(lower, dtype="uint8")
  upper = np.array(upper, dtype="uint8")

  mask = cv2.inRange(hsv, lower, upper)
 
  output = cv2.bitwise_and(frame, hsv, mask=mask)
  
  no_red = cv2.countNonZero(mask)
  
  if int(no_red) > 15000:
      Fire_Reported = Fire_Reported + 1

  cv2.imshow("output", output)

  if Fire_Reported >= 1:
  
      # if Alarm_Status == False:
      #     threading.Thread(target=play_alarm_sound_function).start()
      #     Alarm_Status = True
      #     print("*************  ALARM ON  *************")

      if Email_Status == False:
          threading.Thread(target=send_mail_function).start()
          Email_Status = True
          print("\n\n*************  EMAIL SENT  *************")
          speak("Warning!!! Fire detected. Email has been sent to the, owner")
          speak('Fire alarm ON!!')
          mlist='C:/Users/visha/Desktop/1234/Face-Mask-Detection-master/alarm sound'
          alarm = os.listdir(mlist)
          random = os.startfile(os.path.join(mlist, alarm[0]))

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
   
#playsound.playsound('Alarm Sound.wav',False)
cv2.destroyAllWindows()
video.release()

