import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import random
import pyjokes  
import requests 

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
    engine.setProperty('voice', voices[0].id) 
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    
    if day in Day_dict:
        speak("Today is " + Day_dict[day])

def tellTime():
    time = datetime.datetime.now().strftime("%I:%M %p") 
    speak("The time is " + time)

def Hello():
    speak("Hello! How can I assist you?")

def open_application(app_name):
    try:
        os.system(f"start {app_name}") 
        speak(f"Opening {app_name}")
    except Exception as e:
        speak("Sorry, I couldn't open the application.")

def get_weather():
    api_key = "your_openweathermap_api_key" 
    city = "Delhi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
    except:
        speak("Sorry, I couldn't fetch the weather details.")

def calculator():
    speak("Tell me the calculation")
    query = takeCommand()
    try:
        result = eval(query)  
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I couldn't calculate that.")

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

        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com")

        elif "open facebook" in query:
            speak("Opening facebook")
            webbrowser.open("https://www.facebook.com/share/18XwUte8p9/?mibextid=qi2Omg")

        elif "open instagram" in query:
            speak("Opening instagram")
            webbrowser.open("https://www.instagram.com/dhirajsingh_7541?igsh=ajdvOGo3MWpoOTRy")
            
        elif "open github" in query:
            speak("Opening github")
            webbrowser.open("https://github.com/Dhirajsingh12")
            
        elif "open linkedin" in query:
            speak("Opening linkedin")
            webbrowser.open("https://www.linkedin.com/in/dhiraj-kumar-4525b81b7")


        elif "open stack overflow" in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

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

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "calculate" in query or "math" in query:
            calculator()

        elif "weather" in query:
            get_weather()

        elif "play music" in query:
           os.system("start wmplayer")  


        elif "shutdown the system" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")

        elif "log out" in query:
            speak("Logging out")
            os.system("shutdown -l")

        elif "exit" in query:
            speak("Bye! Have a great day.")
            break

if __name__ == '__main__':
    Take_query()
