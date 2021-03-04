import requests 
import sys 
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import re
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !") 

    else:
        speak("Good Evening Sir !") 

    assname =('smart voice assistant')
    speak("welcome to the service of")
    speak(assname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome to the service of ", assname.center(columns))
    print("#####################".center(columns))
    
    
  
def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome .", uname.center(columns))
    print("#####################".center(columns))
    
    speak("How can i Help you")
    speak('i can provide you personal and other services.....')
    time.sleep(1)
    speak('which service would you like me to perform now')
    
    

def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) 
        print("Unable to Recognize your voice.") 
        return "None"
    
    return query



def corona_updates(audio):
    
    audio = audio   

    #url = 'https://www.worldometers.info/coronavirus/'
    url='https://www.worldometers.info/coronavirus/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'lxml')

    totalcases = soup.findAll('div', attrs =  {'class': 'maincounter-number'})
    total_cases = []
    
    for total in totalcases:
        total_cases.append(total.find('span').text)
    world_total = 'Total Coronavirus Cases: ' + total_cases[0]
    world_deaths = 'Total Deaths: ' + total_cases[1]
    world_recovered = 'Total Recovered: ' + total_cases[2]
    
    info = 'For more information visit: ' + 'https://www.worldometers.info/coronavirus/#countries'

    if 'world' in audio:
        print('World Updates: ')
        print(world_total)
        print(world_deaths)
        print(world_recovered)
        print(info)
        speak('Stay safe!!!..Stay healthy !!!...')
         
    elif "covid" in audio:
        speak('i cant get you, kindly be clear with your statement')
        speak('state either "covid world" or "covid" with any country name you want know')
    else:
        country = audio

        url = 'https://www.worldometers.info/coronavirus/country/' + country.lower() + '/'
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'lxml')

        totalcases = soup.findAll('div', attrs =  {'class': 'maincounter-number'})
        total_cases = []
        for total in totalcases:
            total_cases.append(total.find('span').text)    
        
        total = 'Total Coronavirus Cases: ' + total_cases[0]
        deaths = 'Total Deaths: ' + total_cases[1]
        recovered = 'Total Recovered: ' + total_cases[2]

        info = 'For more information visit: ' + url

        updates = country + ' Updates: '

        print(updates)
        print(total)
        print(deaths)
        print(recovered)
        print(info)
        
        engine.say(updates)
        engine.say(total)
        engine.say(deaths)
        engine.say(recovered)
        engine.say('For more information visit: worldometers.info')
        speak('Stay safe!!!..Stay healthy !!!...')
        engine.runAndWait()




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
    # Enable low security in gmail
    server.login("rishu.0thakur@gmail.com", 'maygodblessu')
    server.sendmail('vishufeb786@gmail.com', to, content)
    server.close()

def scrape_news():
    url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en '
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    news = soup.findAll('h3', attrs = {'class':'ipQwMb ekueJc RD0gLb'})
    for n in news:
        print(n.text)
        print('\n')
        engine.say(n.text)
    print('For more information visit: ', url)
    engine.say('For more information visit google news')
    engine.runAndWait()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()
    # u1=str(takeCommand())
    #u2=str(takeCommand())
while True:
    u1=str(takeCommand())
    
    if u1=="personal services":
            speak(" In personal servies, I can perform the following :")
            print("\n\n**************************** PERSONAL SERVICES ****************************\n\n")
            print("1.  Youtube -----> say 'open youtube'\n")
            print("2.  Google -----> say 'open google'\n")
            print("3.  Music -----> say 'play music'\n")
            print("4.  Mail -----> say 'send a mail'\n")
            print("5.  Latest News -----> say 'latest news'\n")
            print("6.  Note -----> say 'write a note' or 'show a note\n")
            print("7.  Weather Forecast -----> say 'weather updates'\n")
            print("8.  Wikipedia -----> say 'wikipedia ______________'\n")
            print("9.  Stackoverflow -----> say 'open stackoverflow'\n")
            print("10. Current time -----> say 'time'\n")
            print("11. Random Questions -----> ask questions starting from 'what' or 'who','where'\n")
            print("12. Joke -----> say 'joke'\n")
            print("13. Covid updates-----> covid INDIA or covid WORLD")
            print("13. Computational and Geographical Questions -----> say 'ask' \n")
            print("14. Wallpaper -----> say 'change wallpaper'\n")
            print("15. System Shutdown -----> say 'shutdown system'\n")
            print("16. Recycle Bin -----> say 'empty recycle bin'\n")
            print("17. Capture Images -----> say 'camera' or 'take a photo'\n")
            print("18. System Restart -----> say 'restart'\n")
            print("19. System Shutdown -----> say 'log off' or 'sign out'\n")
            print("20. Exit -----> say 'exit'\n")
            #print("9.  Text Messages -----> say 'send message'\n")
            while True:
                query = takeCommand().lower()
        
            # All the commands said by user will be 
            # stored here in 'query' and will be
            # converted to lower case for easily 
            # recognition of command
                if 'wikipedia' in query:
                       speak('Searching Wikipedia...')
                       query = query.replace("wikipedia", "")
                       results = wikipedia.summary(query, sentences = 3)
                       speak("According to Wikipedia")
                       print(results)
                       speak(results)

                elif 'open youtube' in query:
                       speak("Here you go to Youtube\n")
                       webbrowser.open("youtube.com")

                elif 'open google' in query:
                     speak("Here you go to Google\n")
                     webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                     speak("Here you go to Stack Over flow.Happy coding")
                     webbrowser.open("stackoverflow.com") 

                elif 'play music' in query or "play song" in query:
                     speak("Here you go with music")
                     # music_dir = "G:\\Song"
                     music_dir = "C://Users//visha//Music//MP3-musics"
                     songs = os.listdir(music_dir)
                     print(songs) 
                     random = os.startfile(os.path.join(music_dir, songs[1]))
        
                elif 'time' in query:
                     strTime=datetime.datetime.now().strftime("%H:%M:%S")
                     speak(f"the time is {strTime}")
        
        
                elif 'send a mail' in query:
                       try:
                          speak("What should I say?")
                          content = takeCommand()
                          speak("whom should i send  can you please give recipient mail-id ")
                          to = input("give recipient mail-id :") 
                          sendEmail(to, content)
                          speak("Email has been sent !")
                       except Exception as e:
                          print(e)
                          speak("Sorry sir !!! I am unable to send this email")
        
                elif 'latest news' in query:
                      
                      print('..')
                      scrape_news()

                elif 'how are you' in query:
                     speak("I am fine, Thank you")
                     speak("How are you, Sir")

                elif 'fine' in query or "good" in query:
                     speak("It's good to know that your fine")

                elif "change my name to" in query:
                     query = query.replace("change my name to", "")
                     assname = query

                elif "change name" in query:
                     speak("What would you like to call me, Sir ")
                     assname = takeCommand()
                     speak("Thanks for naming me")

                elif "what's your name" in query or "What is your name" in query:
                     speak("My friends call me")
                     speak(assname)
                     print("My friends call me", assname)

                elif 'exit' in query:
                     speak("Thanks for giving me your time")
                     sys.exit()

                elif "who made you" in query or "who created you" in query: 
                     speak("I have been created by ashwini, sreya and vishal.")
            
                elif 'joke' in query:
                     speak(pyjokes.get_joke())
                     print(pyjokes.get_joke())
            
                elif 'ask' in  query:
                     speak('I can answer to computational and geographical questions and what question do you want to ask now')
                     question=takeCommand()
                     app_id="R2K75H-7ELALHR35X"
                     client = wolframalpha.Client('R2K75H-7ELALHR35X')
                     res = client.query(question)
                     answer = next(res.results).text
                     speak(answer)
                     print(answer)

                elif 'search' in query or 'play' in query:
                      try: 
                         from googlesearch import search 
                      except ImportError:  
                        print("No module named 'google' found") 
  
                      query = query.replace("search", "") 
                      query = query.replace("play", "")         
                     #webbrowser.open(query) 
                      for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                         print(j) 
                
                elif 'covid' in query:
                      print('..')
                      words = query.split(' ')
                      corona_updates(words[-1])
               
                elif "who i am" in query:
                      speak("If you talk then definately your human.")

                elif "why you came to world" in query:
                     speak("Thanks to. further It's a secret")

        

                elif 'is love' in query:
                      speak("It is 7th sense that destroy all other senses")

                elif "who are you" in query:
                      speak("I am your  smart virtual assistant")
                      print("I am your  smart virtual assistant")
        
       

                elif 'change wallpaper' in query:
                      ctypes.windll.user32.SystemParametersInfoW(20, 
                                                     0, 
                                                     "Location of wallpaper",
                                                     1)
                      speak("Background changed succesfully")

                

                # elif 'latest news' in query:
            
                #       try: 
                #           jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=in&apiKey=30034779380e4cb698b6c11cd6afdd9f')
                #           data = json.load(jsonObj)
                #           i = 1
                
                #           speak('here are some top news from the times of india')
                #           print('''=============== TIMES OF INDIA ============'''+ '\n')
                
                #           for item in data['articles']:
                    
                #                  print(str(i) + '. ' + item['title'] + '\n')
                #                  print(item['description'] + '\n')
                #                  speak(str(i) + '. ' + item['title'] + '\n')
                #                  i += 1
                #       except Exception as e:
                
                #            print(str(e))
  
        
                elif 'lock window' in query:
                     speak("locking the device")
                     ctypes.windll.user32.LockWorkStation()

                elif 'shutdown system' in query:
                     speak("Hold On a Sec ! Your system is on its way to shut down")
                     subprocess.call('shutdown / p /f')
                
                elif 'empty recycle bin' in query:
                      winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                      speak("Recycle Bin Recycled")

                elif "don't listen" in query or "stop listening" in query:
                     speak("for how much time you want to stop smart assistant from listening commands")
                     p =int(input('enter the time in second :'))
                     time.sleep(p)
                     speak('waiting time is over your smart assistant is again at your service')
                     

                elif 'where is' in query:
                    print('..')
                    words = query.split('where is')
                    print(words[-1])
                    link = str(words[-1])
                    link = re.sub(' ', '', link)
                    engine.say('Locating')
                    engine.say(link)
                    engine.runAndWait()
                    link = f'https://www.google.co.in/maps/place/{link}'
                    print(link)
                    webbrowser.open(link)
                    
                elif "camera" in query or "take a photo" in query:
                     ec.capture(0, "Smart voice Camera ", "img.jpg")

                elif "restart" in query:
                     subprocess.call(["shutdown", "/r"])
            
                
                elif "log off" in query or "sign out" in query:
                     speak("Make sure all the application are closed before sign-out")
                     time.sleep(5)
                     subprocess.call(["shutdown", "/l"])

                elif "write a note" in query:
                     speak("What should i write, sir")
                     note = takeCommand()
                     file = open('smart.txt', 'w')
                     speak("Sir, Should i include date and time")
                     snfm = takeCommand()
                     if 'yes' in snfm or 'sure' in snfm:
                         strTime=datetime.datetime.now().strftime("%H:%M:%S")
                         file.write(strTime)
                         file.write(" :- ")
                         file.write(note)
                     else:
                         file.write(note)
        
                elif "show note" in query:
                     speak("Showing Notes")
                     file = open("smart.txt", "r") 
                     print(file.read())
                     speak(file.read(6))

                elif "weather update" in query:
            
                     # Google Open weather website
                     # to get API of Open weather 
                     api_key="8ef61edcf1c576d65d836254e11ea420"
                     base_url="https://api.openweathermap.org/data/2.5/weather?"
                     speak("whats the city name")
                     city_name=takeCommand()
                     complete_url=base_url+"appid="+api_key+"&q="+city_name
                     response = requests.get(complete_url)
                     x=response.json()
                     if x["cod"]!="404":
                            y=x["main"]
                            current_temperature = y["temp"]
                            current_humidiy = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            speak(" Temperature in kelvin unit is " +
                                 str(current_temperature) +
                                 "\n humidity in percentage is " +
                                 str(current_humidiy) +
                                 "\n description  " +
                                 str(weather_description))
                            print(" Temperature in kelvin unit = " +
                                 str(current_temperature) +
                                 "\n humidity (in percentage) = " +
                                 str(current_humidiy) +
                                 "\n description = " +
                                 str(weather_description))

                     else:
                             speak(" City Not Found ")

            
                elif "send message " in query:
                     # You need to create an account on Twilio to use this service
                     account_sid = 'AC96896d3a83d7aee901839cf0c505a25c'
                     auth_token = 'cf51fc8b33dcdb5f6a06d30b4a2ef958'
                     client = Client(account_sid, auth_token)

                     message = client.messages                                      .create(
                                         body = takeCommand(),
                                         from_='+916350063760',
                                         to ='+919462817750'
                                     )

                     print(message.sid)

                
         
                    
    #other services Task                    
    elif u1=="other services":
    
              speak(" In other servies, I can perform the following :")
              print("\n\n**************************** OTHER SERVICES ****************************\n\n")
              print("1.  Mask Detection -----> say 'start mask detection'\n")
              print("2.  Face Recognition -----> say ''\n")
              print("3.  Unknown Person Detection\n")
              print("4.  Fire Detection\n")
              print("5.  Weapon Detection\n")
              print("6.  Monitoring at the Enterance -----> say 'start first camera'\n")
              print("7.  Realtime Monitoring at the Enterance -----> say 'start secondv camera'\n")
              print("8.  Human Emotion Recognition\n")
              print("9.  Age and Gender Detection\n")
              print(".  Exit -----> say 'exit'\n")
              while True:
             
                      query2 = takeCommand().lower()
             
                      
                      if'start mask detection' in query2:
                         speak("Hold On a Second ! face mask detection by facenet is opening")
                         import face_mask
                         speak('the task assigned is succlessfully completed')
                         os.system('face_mask.py')
             
                      elif "take the attendance" in query2:
                         speak("Hold On a Second !!")
                         import attendance
                         speak('the task assigned is succlessfully completed')
                         os.system('attendance.py')
              
                      elif "start first camera  " in query2:
                         speak('Hold on a second !! surveillance camera at entrance is on')
                         speak('the task assigned is succlessfully completed')
                         import people_counter
                         os.system('people_counter.py')
            
                      elif "start second camera " in query2:
                         speak('Hold on a second!! realtime surveillance camera at entrance is on')
                         speak('the task assigned is succlessfully completed')
                         import real_time_people_counter
                         os.system('real_time_people_counter.py')
                 
                      elif "start third camera" in query2:
                         speak('hold on a second!! system camera is on for detecting unkown person from taken sample')
                         import uknown_people_detection
                         speak('the task assigned is succlessfully completed')
                         os.system('uknown_people_detection.py')
            
                      elif "start weapon detection" in query2:
                         speak('hold on a second!!! system camera is on for detecting the weapon')
                         import weapon_detection
                         speak('the task assigned is succlessfully completed')
                         os.system('weapon_detection.py')
        
                      elif 'start fire detection' in query2:
                         speak('hold on second!! system is detecting for fire')
                         import Fire_detector
                         speak('the task assigned is succlessfully completed')
                         os.system('Fire_detector.py')
                   
                      elif 'exit' in query2:
                         speak("Thanks for giving me your time !!! hope you satisfied with my service")
                         sys.exit()
              
                      
              
    else:
            speak('choose correct service')          
     
          
          
          
          
          
          
          
          
          
          
          
          
          
          