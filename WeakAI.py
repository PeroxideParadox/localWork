# System Requirements

# Windows 7 and above ,Python 3.6 and above
# The following Modules must be Imported
# pyttsx3,datetime,wolframalpha,wikipedia,speech_recognition,webbrowser
# Usage of good Microphone is Recommended

import pyttsx3
import datetime
import wolframalpha
import speech_recognition as sr
import wikipedia
import webbrowser as wb

machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[0].id)


def speak(audio):
    machine.say(audio)
    machine.runAndWait()


def Greet():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Dear")
    elif hour >= 12 and hour < 18:
        speak("good Evening Master")
    else:
        speak("Good evening Master")
    speak("This is BSKG007 here How can I help you")


def Work():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if "youtube" in query.lower():
            print("Opening youtube")
            wb.open("www.youtube.com")
        elif "google" in query.lower():
            print("Opening google")
            wb.open("www.google.com")
        elif "search" or "Calculate " in query.lower():
            query = query.replace("search", "")
            question = query
            app_id = "U8YVH3-9K9PAHW9J7"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hello this is our beta version ")
    Greet()
    Work()
