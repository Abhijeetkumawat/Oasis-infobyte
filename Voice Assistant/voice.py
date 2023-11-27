import pyttsx3 #convert text to speech
import speech_recognition as sr #takes microphone input & return string output
import datetime #current Date & Time
import wikipedia #wikipedia searches
import webbrowser
import os

engine = pyttsx3.init('sapi5') #it is a Microsoft developed speech API, helps in synthesis and recognition of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)# selecting voice
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

def speak(audio): #this function speak() will take audio as argumenta and then pronounce it
    engine.say(audio)
    engine.runAndWait() #through tthis speech will audible to the user

def wishMe(): #through this our Assistant will wish the user
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am your Personal voice Assistant. Please tell me how may I help you sir")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition
        print(f"User said: {query}\n") #User query will be printed.

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Sir, today's date is {strDate}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)