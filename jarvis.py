import operator
import time
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser,os
import wikipedia
import pywhatkit as kit
import tracemalloc,speedtest,subprocess,pyjokes,pyautogui,random
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pyautogui
import speedtest


List = []


# text to speech
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


# speech to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        try:
            print("Recognizing....")
            Query = r.recognize_google(audio, language='en-in')
            print("The Command is = ", Query)
        except Exception as e:
            print(e)
            speak("Say that again sir")
            return "None"
        return Query


# wish me
def wish():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<=12:
        speak("Good morning")
    elif time>12 and time<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello there, I am Jarvis sir, please tell me how can i help you?")


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    mint = time[14:16]
    speak( "The time is sir" + hour + "Hours and" + mint + "Minutes")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def history():
    List.reverse()
    speak("the last five commands were")
    for i in range(0,5):
        speak(List[i])
        print(List[i])


# news
def news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=7cb4d2969e0b46fabe84418b5a17eb51"
    news_page = requests.get(url).json()
    articles = news_page["articles"]
    headlines = []
    days = ["First","Second","Third","Fourth","Fifth"]
    for ar in articles:
        headlines.append(ar["title"])
    for i in range(len(days)):
        speak(f"today's {days[i]} news is: {headlines[i]}")
        print(f"today's {days[i]} news is: {headlines[i]}")


# queries to do
def Take_query():
    wish()
    while (True):

        query = takeCommand().lower()
        if "open youtube" in query:
            List.append(query)
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "what\'s up" in query or 'how are you' in query:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power']
            speak(random.choice(setReplies))
            continue

        elif "who are you" in query or 'what are you' in query:
            setReplies = [' I am KryptoKnite', 'In your system', 'I am an example of AI']
            speak(random.choice(setReplies))

        elif "open notepad" in query:
            List.append(query)
            speak("Opening notepad ")
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            continue

        elif "open calculator" in query:
            List.append(query)
            speak("Opening calc ")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            continue

        elif "open command prompt" in query:
            List.append(query)
            speak("Opening cmd ")
            os.system("start cmd")
            continue

        elif "play music" in query:
            List.append(query)
            speak("playing music ")
            npath='C:\\Users\\mohit\\Music'
            songs = os.listdir(npath)
            os.startfile(os.path.join(npath,songs[1]))
            continue

        elif "open google" in query:
            List.append(query)
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "tell me a joke" in query:
            List.append(query)
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
            continue

        elif "search google" in query:
            List.append(query)
            speak("Sir, what should i search ")
            res = takeCommand().lower()
            webbrowser.open(f"{res}")
            continue

        elif "play songs on youtube" in query:
            List.append(query)
            speak("playing songs on youtube ")
            kit.playonyt("mere nishan")
            continue

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            continue

        elif "tell me news" in query:
            List.append(query)
            speak("Please wait sir, fetching the latest news")
            news()
            continue

        elif "tell me our current location" in query or "tell me your current location" in query or "where are we now" in query:
            List.append(query)
            speak("Sir wait, let me check")
            try:
                add = requests.get('https//api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+add+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_requests['country']
                speak(f"sir we are in {city} city of country {country}")
            except Exception as e:
                speak("Sorry sir , due to network issues, iam not able to find")
            continue

        # this will exit and terminate the program
        elif "bye" in query or "no thanks" in query or 'nothing' in query or 'abort' in query or 'stop' in query:
            speak("okay, Bye Sir")
            tracemalloc.stop()
            exit()

        elif "thank you" in query or "thanks" in query:
            speak("happy to help you Sir")
            continue

        elif "which day it is" in query:
            List.append(query)
            tellDay()
            continue

        elif "tell me the time" in query:
            List.append(query)
            tellTime()
            continue

        elif "tell me your memory consumption" in query:
            List.append(query)
            current, peak = tracemalloc.get_traced_memory()
            speak(f"Current memory usage is {current / 10 * 6}MB; Peak was {peak / 10 * 6}MB")
            print(f"Current memory usage is {current / 10 * 6}MB; Peak was {peak / 10 * 6}MB")
            continue

        elif "wikipedia" in query:
            List.append(query)
            speak("Searching the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            continue

        elif "tell me my history" in query:
            List.append(query)
            speak("fetching history, please wait sir")
            history()
            continue

        elif "tell me what can you do" in query or "tell me your skills" in query:
            List.append(query)
            speak("Here are some things I can help you do")
            print("Here are some things I can help you do")
            speak("Check the wheather anywhere")
            print("Check the wheather anywhere")
            speak("Check daily news")
            print("Check Daily News")
            speak("play some musics")
            print("Play some musics")
            speak("search wikipedia")
            print("search wikipedia")
            speak("play some musics on youtube")
            print("Play some musics on youtube")
            speak("set an alarm")
            print("set an alarm")
            speak("search google")
            print("Search the google")
            continue

        elif "tell me your name" in query:
            List.append(query)
            speak("I am Jarvis. Your deskstop Assistant")
            continue

        elif "can you calculate" in query or "do some calculations" in query:
            # r = sr.Recognizer()
            # with sr.Microphone as source:
            #     speak("Say what you want to calculate, example 2 plus 5")
            #     print("listening....")
            #     r.adjust_for_ambient_noise(source)
            #     audio = r.listen(source)
            statement = takeCommand().lower()
            print(statement)
            def find_operator(op,op1,op2):
                return  {
                    '+' : operator.add(op1,op2),
                    '-' : operator.sub(op1,op2),
                    'x' : operator.mul(op1,op2),
                    'divided' : operator.__truediv__(op1,op2),
                }
            def eval_expression(op1,oper,op2):
                op1,op2 = int(op1),int(op2)
                return find_operator(oper,op1,op2)
            speak("your result is")
            speak(eval_expression(*(statement.split())))
            continue

        elif "how to" in query:
            max_results = 1
            how_to = search_wikihow(query,max_results)
            assert  len(how_to) ==1
            how_to[0].print()
            speak(how_to[0].summary)
            continue

        elif "weather in" in query:
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"weather is {temp}")
            continue

        elif "volume up" in query:
            pyautogui.press("volumeup")
            continue

        elif "volume down" in query:
            pyautogui.press("volumedown")
            continue

        elif "volume mute" in query or "mute" in query:
            pyautogui.press("volumemute")
            continue


if __name__ == '__main__':
    tracemalloc.start()
    Take_query()
    tracemalloc.stop()