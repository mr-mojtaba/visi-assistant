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
engine.setProperty('rate', 125)

# Creating a Variable for adjusting the engine sound gender.
voices = engine.getProperty('voices')

# Adjusting the engine sound gender.
engine.setProperty('voice', voices[1].id)

NAME = "none"

# If needed, this command can be used to display the list of connected microphones.
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))


# ---------- Functions ----------

# Text-to-speech function.
def speak(text):
    # saying the texts
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Function to listen and execute commands.
def take_command():
    r = sr.Recognizer()

    # Activating the microphone.
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            # Listening to commands.
            # For persian language -> ( fa-IR )
            # For more language -> ( https://cloud.google.com/speech-to-text/docs/languages )
            cm = r.recognize_google(audio, language="en-US")
            print(f"You said: {cm}\n")
        except:
            print("Sorry, I didn't understand, Please say it again.\n")
            speak("Sorry, I didn't understand, Please say it again.")
            return "None"
    return cm


# Function for Welcoming and getting the user's name.
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
        if NAME != "none":
            break
    print(f"Wellcome {NAME}. Lets start!\n")
    speak(f"Wellcome {NAME}. Lets start!")


welcome()


# ---------- Loop and conditions ----------

while True:
    print("How can i help you?\n")
    speak("How can i help you?")

    command = take_command().lower()

    if "by" in command or "stop" in command:
        print(f"Goodbye {NAME}")
        speak(f"Goodbye {NAME}")
        break

    if "wikipedia" in command:
        print("Searching wikipedia,,,\n")
        speak("Searching wikipedia,,,")
        command = command.replace("wikipedia", "")
        print("How many sentences of the result would you like to read to you?\n")
        speak("How many sentences of the result would you like to read to you?")
        try:
            sentences = int(take_command())
        except:
            sentences = 3
            result = wikipedia.summary(command, sentences=sentences)
            print(f"{sentences} sentences of your search result in wikipedia.\n")
            speak(f"{sentences} sentences of your search result in wikipedia.")
            pprint(result + "\n")
            speak(result)

    elif "youtube" in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        print("Opening Youtube!\n")
        speak("Opening Youtube!")
        time.sleep(5)

    elif "google" in command:
        webbrowser.open_new_tab("https://www.google.com")
        print("Opening Google!\n")
        speak("Opening Google!")
        time.sleep(5)

    elif "gmail" in command:
        webbrowser.open_new_tab("https://www.gmail.com")
        print("Opening Gmail!\n")
        speak("Opening Gmail!")
        time.sleep(5)

    elif "news" in command:
        webbrowser.open_new_tab("https://www.news.google.com")
        print("Opening News!\n")
        speak("Opening News!")
        time.sleep(5)

    elif "time" in command:
        str_time = datetime.datetime.now().strftime("%H:%M")
        print(f"The time is: {str_time}\n")
        speak(f"The time is: {str_time}")

    elif "date" in command:
        str_date = datetime.datetime.now().strftime("%d %b %Y")
        print(f"The date is: {str_date}\n")
        speak(f"The date is: {str_date}")
