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

    if "by" in command or "stop" in command or "exit" in command:
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

    elif "visi" in command or "hi" in command:
        print(f"Hi {NAME}, How can i help you?\n")
        speak(f"Hi {NAME}, How can i help you?")
        command = take_command()

    elif "who are you" in command:
        print("My name is Visi, I am version 1 of the voice assistant and, I was programmed by Mojtaba.\n")
        speak("My name is Visi, I am version 1 of the voice assistant and, I was programmed by Mojtaba.")

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

    elif "camera" in command or "photo" in command:
        # Specifying the camera
        camera = cv2.VideoCapture(0)

        ret, frame = camera.read()
        if ret:
            cv2.imwrite("your_photo.png", frame)
        camera.release()
        cv2.destroyAllWindows()
        print("Your photo was taken.\n")
        speak("Your photo was taken.")

    elif "screenshot" in command:
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save("screenshot.png")
        print("Screenshot was taken.\n")
        speak("Screenshot was taken.")

    elif "search" in command:
        command = command.replace("search", "")
        print(f"Searching {command}\n")
        speak(f"Searching {command}")
        webbrowser.open_new_tab(command)
        time.sleep(5)

    elif "question" in command:
        print("Now i can answer your calculation and geography questions.\n")
        speak("Now i can answer your calculation and geography questions.")

        # Create an object from take_command() to ask the question.
        question = take_command()

        # Wolframalpha API
        app_id = "P53EKT-QH6K4E499J"

        # Create the client
        client = wolframalpha.Client(app_id)

        # Asking questions
        res = client.query(question)

        # The answer receiving and converting it to text.
        answer = next(res.results).text

        print(answer + "\n")
        speak(answer)

    elif "write note" in command:
        print(f"What should i write {NAME}?\n")
        speak(f"What should i write {NAME}?")

        # Create an object from take_command() to ask the note text.
        note = take_command()

        print(f"{NAME}, Should I include date and time?\n")
        speak(f"{NAME}, Should I include date and time?")

        # Create an object from take_command() to ask for append the date and time.
        ans = take_command()

        if "y" in ans:
            date_and_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
            with open("note.txt", "w") as file:
                file.write(date_and_time + "\n")
                file.write("-" * 40 + "\n")
                file.write(note)
        else:
            with open("note.txt", "w") as file:
                file.write(note)

    elif "show note" in command:
        print("Showing the notes.\n")
        speak("Showing the notes.")

        with open("note.txt", "r") as file:
            nt = file.read()
            print(nt + "\n")
            speak(nt)

    elif "telegram" in command:
        print("Opening Telegram!\n")
        speak("Opening Telegram!")

        os.startfile(r"C:\Program Files\WindowsApps"
                     r"\TelegramMessengerLLP.TelegramDesktop_4.11.8.0_x64__t4vj0pshhgkwm\Telegram.exe")
        time.sleep(5)

    elif "whatsapp" in command:
        print("Opening WhatsApp!\n")
        speak("Opening WhatsApp!")

        os.startfile(
            r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2348.4.0_x64__cv1g1gvanyjgm\WhatsApp.exe")
        time.sleep(5)

    elif "logout" in command:
        print("Your system will log out after 5 seconds!\n")
        speak("Your system will log out after 5 seconds!")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "shutdown " in command:
        print("Your system will shutdown after 5 seconds!\n")
        speak("Your system will shutdown after 5 seconds!")
        time.sleep(5)
        subprocess.call(["shutdown", "/s"])

    elif "restart" in command:
        print("Your system will restart after 5 seconds!\n")
        speak("Your system will restart after 5 seconds!")
        time.sleep(5)
        subprocess.call(["shutdown", "/r"])

    elif "weather" in command:
        api_key = "e48a2b3409d7d2fae60f4a279ca8556e"
        base_url = "https://www.api..openweathermap.org/data/2.5/weather?"

        print("What is the city name?\n")
        speak("What is the city name?")

        city_name = take_command()

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)
        res = response.json()
        if res["code"] != "404":
            main = res["main"]
            temperature = main["temp"]
            humidity = main["humidity"]
            weather = res["weather"]
            weather_description = weather[0]["description"]

            print(f"Temperature in kelvin unit = {temperature}\n")
            speak(f"Temperature in kelvin unit = {temperature}")

            print(f"Humidity = {humidity}\n")
            speak(f"Humidity = {humidity}")

            print(f"Weather description = {weather_description}\n")
            speak(f"Weather description = {weather_description}")
