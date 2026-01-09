from urllib import request
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
# import Wikipedia
import ctypes
import subprocess
import random

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning BOSS")
    elif hour>=12 and hour<18:
        speak("Good Afternoon BOSS")
    else:
        speak("Good evening BOSS")
    speak("this is your captain speaking  how can i help you")
class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.CAPTAIN()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text
    
    def CAPTAIN(self):
        wish()
        while True:
            
            self.query = self.STT()
            if 'See you later' in self.query:
                sys.exit()
            elif 'open google' in self.query:
             webbrowser.open("google.com")
            
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            
            elif "my name" in self.query:
                speak("your name is Mr. Pawan kalyan J P K ")

            
            
            elif 'wikipedia' in self.query:
                speak('Searching wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'play music' in self.query or "play song" in self.query:
                speak("Here you go with music")
                
                music_dir = r"C:\Users\91837\OneDrive\Desktop\Spl project VA\music"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'what is the time' in self.query:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"the time is {strTime}")
               print(strTime)
        
            elif 'lock window' in self.query:
               speak("locking the device")
               ctypes.windll.user32.LockWorkStation()

            elif "restart" in self.query:
               subprocess.call(["shutdown", "/r"])
			
            
            elif "hibernate" in self.query or "sleep" in self.query:
               speak("Hibernating")
               subprocess.call("shutdown / h")
            
            elif "log off" in self.query or "sign out" in self.query:
             speak("Make sure all the application are closed before sign-out")
             time.sleep(5)
             subprocess.call(["shutdown", "/l"])
            
            elif "open chrome" in self.query:
             speak("Google Chrome")
             os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk')

            elif "best restaurant" in self.query:
                speak(" searching results")
                webbrowser.open("https://www.google.com/search?q=best+restaurants+near+me&rlz=1C1CHBF_enIN1025IN1025&oq=best+re&aqs=chrome.1.69i57j0i271l3.2874j0j7&sourceid=chrome&ie=UTF-8")
            
            elif "open youtube" in self.query:
                speak(" searching results")
                webbrowser.open("https://www.youtube.com/")

            elif "oepn movies website" in self.query:
                speak("opening ibomma")
                webbrowser.open("https://ww3.ibomma.cx/telugu-movies/")











FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/captain.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())