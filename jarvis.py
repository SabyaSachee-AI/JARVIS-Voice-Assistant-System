
#1. Importing the libraries

import speech_recognition as sr
import pyttsx3
import datetime
import logging
import wikipedia
import os
import webbrowser
import subprocess  #je kono app open korar jonno
import random


#2. Setting up the logging configuration:to creat folder and file and log formate (suitable for all project)

LOG_DIR = "logs"   #Folder Name
LOG_FILE_NAME = "application.log"     #file name

os.makedirs(LOG_DIR, exist_ok=True)            #Folder creation ,(exist_ok=True)_if alredy creaded continue/ignoor

log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)  #path creation ,we can do it manually(path ="logs/application.log")

#how log will be saved in file,log formate)
logging.basicConfig (
    filename=log_path, 
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


#3.functional Progamming: all necessary function

# a.Activating voice from our system

engine = pyttsx3.init("sapi5")  #initialise the librey
engine.setProperty('rate',170)  #speed/tempu up/down
voices = engine.getProperty("voices")
#voice =voices
#print(voice) #will show two voice one is mail and another is female
# print(voices [1].id)
# print(voices [0].id) #to show the name of the voice
engine.setProperty("voice",voices[1].id)  #we select index 1(femaile)


# THis is speak function
def speak(text):
    '''this function convert text to voice 
    args:
        text
    return:
        voice
    '''

    engine.say(text)
    engine.runAndWait()

# speak("hello i am Preontie")

#b.This function recognize the speech and convert it to text

def takecommand():
    '''
    This function takes the command and recognize 

    returns:
    text as querry

    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio =r.listen (source)
    try:
         print("Recognizing...")
         query=r.recognize_google(audio, language = 'en-in')
    except Exception as e:
         logging.info(e)
         print("Not Clear ,please Say that again")
         speak("Not Clear ,please Say that again")
         return "None"
    return query



#grettings funtion:

def greeting():
     hour =(datetime.datetime.now().hour)
     if hour>=0 and hour <=12:
          speak( "Good Morning Sir! , How are you doing?")
          
     elif hour>12 and hour <=18:
          speak( "Good Afternoon Sir! , How are you doing?")
     else:
          speak( "Good Evening Sir! , How are you doing?")

     #speak("I am preontie!!,Please tell me how may i help you today?")

def play_music():
     music_dir = "F:\\DS\Full-Stack-Data-Science-with-Generative-AI\\JARVIS-Voice-Assistant-System\\music"
     try:
         songs = os.list(music_dir)
         if songs:
              random_song = random.choice(songs)
              speak(f"playing a random song sir:{random_song}")
              os.startfile(os.path.join(music_dir,random_song))
         else:
              speak("no music found")

     except Exception as e:
          speak("no music folder not  found")

#program run from here:
greeting()
while True:     #bar bar sunbe
     query = takecommand().lower() #lower(): input voice je text a convert korbe segula sob chuto hater kore nibe
     print(query)                  #speak(query)           #AMI JABOLI TA REPEAT KORBE ...SOURCE THEKE JA SUNBE TA ABR BOLBE JA AMADER DORKAR NAI
     
     if "your name" in query:
          speak("my name is Preonty")
          logging.info("User asked for assistant's Name")
        
     elif "How are you" in query:
          speak("i am functioning at full capacity sir!!")
          logging.info("User asked for how are you")      
     
     elif "who made you" in query:
          speak("i am developed by S.S.D")
          logging.info("User asked for made by")

     elif "time" in query:                           #Current time:          
          time= datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir the time is {time}")
          logging.info("User asked for time")

     elif "google" in query:                  #webbrowser.open(link)___browser a kiso open kora:         
          webbrowser.open("google.com")
          speak("yes.. sure!!.opening....")
          print("Opening...!!")
          logging.info("User asked for open google")
    
     elif "facebook" in query:
          webbrowser.open("facebook.com")
          speak("yes.. sure!!.opening....")
          print("Opening...!!")
          logging.info("User asked for open facebook")
     
     elif "github" in query:
          webbrowser.open("github.com")
          speak("yes.. sure!!.opening....")
          print("Opening...!!")
          logging.info("User asked for open github")
     
     elif "Whatsapp" in query:
          webbrowser.open("web.whatsapp.com")
          speak("yes.. sure!!.opening....Whatsapp")
          print("Opening...!!")
          logging.info("User asked for open Whatsapp")


     elif "youtube" in query:                          #youtube search
          speak("yes.. sure!!.opening....youtube")
          query =query.replace("youtube","")
          webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
          logging.info("User requested to search in youtube")

     elif "calculator" in query:               #subprocess.Popen(soft) pc theke kono soft open kora 
          speak("yes.. sure!!.opening....Calculator")
          subprocess.Popen("calc.exe")
          logging.info("User asked for open Calculetor")
     
     elif "notepad" in query:
          speak("yes.. sure!!.opening....notepad")
          subprocess.Popen("notepad.exe")
          print("Opening...!!")
          logging.info("User asked for open Notepad")

     elif "joke" in query:
          speak("yes.. sure!!.i am trying..")
          jokes = ["heloo helooo helllooo joke"
                   "hi hi hih hi joke2"  
                   "joke3"    
                     ]   
          speak("random.choice(jokes)")
          logging.info("User asked for jokes")

     elif "wikipedia"in query:
          query = query.replace("wikipedia","")
          result =wikipedia.summary(query,sentences=2)
          speak(f"according to wikipidea..{result}")
          logging.info("User asked for wikipedia")

     elif "play music" in query:
          speak("ok wait a second..")
          play_music()



     elif "Thank you"in query or "thanks"in query : 
          speak("its my pleasure sir!!..always happy to help")
          logging.info("User asked for how are you")
     
     elif "exit" in query or "stop" in query:
          speak("thankyou for your time sir")
          exit()
          logging.info("User asked for Exit")
     else:
          speak("Sorry i cant help")
          logging.info("unknown to preonty")




