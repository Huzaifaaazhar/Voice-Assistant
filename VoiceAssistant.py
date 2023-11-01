from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning!")       
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon!")     
    else:
        speak("Good Evening!")
    speak("How may I help you?")

def takeCommand():
    #Takes input from user in voice and output string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1 #Assistant waits to check if the input is complete.
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again, please!")
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('azharhuzaifa123@gmail.com', '#1imagination')
    server.sendmail('azharhuzaifa123@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    #if 1:
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query:
            songs = 'E:\\Data Material\\Audio'
            music = os.listdir(songs)
            print(songs)
            os.startfile(os.path.join(songs, music[0]))
        
        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {strTime}")
            
        elif 'open code' in query:
            path = "E:\\Data Material\\Microsoft VS Code"
            os.startfile(path)
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'azharhuzaifa123@gmail.com'
                sendEmail(to, content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("Not abel to send!!!!!!")
