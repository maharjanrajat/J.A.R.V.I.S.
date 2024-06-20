import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio,language = 'en-np')
        print(f"Showing result for: {query}\n")
    except Exception as e:
        print("Please say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greeting import greetMe 
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime!")
                    break
                
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                
                elif "i am fine" in query:
                    speak("that's great sir")
                
                elif "how are you" in query:
                    speak("Perfect sir")
                
                elif "thank you" in query:
                    speak("You're welcome, sir")
                    
                elif "open" in query:
                    from dictApp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictApp import closeappweb
                    closeappweb(query)
                    
                
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                    
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                     
                elif "temperature" in query:
                    search = "temperature today..."
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"curresnt{search} is {temp}")
                    
                elif "weather" in query:
                    search = "weather today..."
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"curresnt{search} is {temp}")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the current time is {strTime}")
                    
                elif "set an alarm" in query:
                    print("input time example: 10 and 10 and 10")
                    speak("Set an alarm")
                    a = input("Please tell the time:")
                    alarm(a)
                    speak("Alarm set successfully, sir")
                    
                elif "finally sleep" in query:
                    speak("Okay sir, going to sleep!")
                    exit()
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to.." + rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()
                    
                elif "what do you remember jarvis?" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to.." + remember.read())                 