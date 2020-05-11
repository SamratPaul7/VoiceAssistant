import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import os
import xsmtplib
import webbrowser
import wikipedia
import urllib.request
import urllib.parse
import re
MASTER = " '''put your name here''' "

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#this function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#this function will greet the user
def wishme():
    speak("Initializing Micoo....")
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("I am Micoo. How may I help you?")

#this function will take command via user's voice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("I am waiting for your instructions. Say that again please")
        query = None

    return query
wishme()
while True:
    query = takeCommand()
    if query != None:
    #execution of tasks
        if 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif 'open youtube' in query.lower():
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query.lower():
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("google.com")

        elif 'play music' in query.lower():
            songs_dir = ""
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'go to' in query.lower():
            query = query.split()
            url = 'https://'+ str(query[2])
            print(url)
            values = {'s':'basics','submit':'search'}
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(url,data)
            resp = urllib.request.urlopen(req)
            respdata = resp.read()
            paragraphs = re.findall(r'<p>(.*?)</p>',str(respdata))
            for eachP in paragraphs:
                speak(eachP)
        elif 'who'or 'what' or 'wikipedia' in query.lower():
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences= 2)
            print(results)
            speak(results)
            speak('searching...')

        elif 'bye' or 'goodbye' in query.lower():
            speak("Goodbye" + MASTER)
            speak("Micoo signing off")
            exit()
