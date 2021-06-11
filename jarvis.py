import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser,os
import wikipedia
import pywhatkit as kit


#text to speech
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()

#speech to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing....")
            Query = r.recognize_google(audio, language='en-in')
            print("The Command is = ", Query)
        except Exception as e:
            print(e)
            speak("Say that again sir")
            return "None"
        return Query

#wish me
def wish():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<=12:
        speak("Good morning")
    elif time>12 and time<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello there, I am Jarvis sir, please tell me how can i help you?")

#queries to do
def Take_query():
    wish()
    while (True):

        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open notepad" in query:
            speak("Opening notepad ")
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            continue

        elif "open command prompt" in query:
            speak("Opening cmd ")
            os.system("start cmd")
            continue

        elif "play music" in query:
            speak("playing music ")
            npath="C:\\Users\\mohit\\Music"
            songs = os.listdir(npath)
            os.startfile(os.path.join(npath,songs[1]))
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "search google" in query:
            speak("Sir, what should i search ")
            res = takeCommand().lower()
            webbrowser.open(f"{res}")
            continue

        elif "play songs on youtube" in query:
            speak("playing songs on youtube ")
            kit.playonyt("mere nishan")
            continue

        # this will exit and terminate the program
        elif "bye" in query or "no thanks" in query:
            speak("Bye Sir")
            exit()

        elif "thank you" in query or "thanks" in query:
            speak("happy to help you Sir")
            continue

        elif "wikipedia" in query:

            speak("Searching the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jarvis. Your deskstop Assistant")


if __name__ == '__main__':
    Take_query()