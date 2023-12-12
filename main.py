# Need to install ( pip install pipwin )
# Need to install ( pipwin install pyaudio )

# Need to install ( pip install SpeechRecognition )
import speech_recognition as sr

#  Need to install ( pip install pyttsx3 )
import pyttsx3

#  Need to install ( pip install wikipedia )
import wikipedia

#  Need to install ( pip install wolframalpha )
import wolframalpha

#  Need to install ( pip install requests )
import requests

#  Need to install ( pip install opencv-python )
import cv2

#  Need to install ( pip install pyautogui )
import pyautogui

# Standard python libraries
import datetime
import webbrowser
import os
import time
import subprocess
from pprint import pprint

# Creating an object for the text-to-speech engine.
engine = pyttsx3.init()

# Adjusting the engine speech speed.
engine.setProperty('rate', 110)

# Creating a Variable for adjusting the engine sound gender.
voices = engine.getProperty('voices')

# Adjusting the engine sound gender.
engine.setProperty('voice', voices[0].id)


# ---------- Functions ----------

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            cm = r.recognize_google(audio, language="en-US")
            print(f"You said: {cm}\n")
        except:
            print("Sorry, I didn't understand, Please say it again.\n")
            speak("Sorry, I didn't understand, Please say it again.")
            return "None"
    return cm


NAME = "none"


def welcome():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        print("Hello, Good Morning.\n")
        speak("Hello, Good Morning.")
    elif 12 <= hour <= 18:
        print("Hello, Good Afternoon.\n")
        speak("Hello, Good Afternoon.")
    else:
        print("Hello, Good Evening.\n")
        speak("Hello, Good Evening.")

    print("What is your name?\n")
    speak("What is your name?")
    global NAME

    while True:
        NAME = take_command().lower()
        if None != "none":
            break


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))
