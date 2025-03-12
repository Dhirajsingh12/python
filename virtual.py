import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')
            print("You said: ", Query)
        except Exception as e:
            print("Error:", e)
            print("Say that again please...")
            return "None"
        
        return Query.lower()

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # [1] for female, [0] for male
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    
    if day in Day_dict:
        speak("Today is " + Day_dict[day])

def tellTime():
    time = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
    speak("The time is " + time)

def Hello():
    speak("Hello! How can I assist you?")

def Take_query():
    Hello()

    while True:
        query = takeCommand()

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks")
            webbrowser.open("https://www.geeksforgeeks.org")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "which day it is" in query:
            tellDay()

        elif "tell me the time" in query:
            tellTime()

        elif "from wikipedia" in query:
            speak("Checking Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please specify.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, no results found on Wikipedia.")

        elif "tell me your name" in query:
            speak("I am Jarvis, your desktop assistant.")

        elif "bye" in query:
            speak("Bye! Have a great day.")
            break

if __name__ == '__main__':
    Take_query()
