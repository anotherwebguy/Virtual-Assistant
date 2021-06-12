import operator
import time
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser,os
import wikipedia
import pywhatkit as kit
import tracemalloc,subprocess,pyjokes,pyautogui,random
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import json
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
        print("please tell me how can i help you?")
        speak("please tell me how can i help you?")
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)
        try:
            print("Recognizing....")
            Query = r.recognize_google(audio, language='en-in')
            print("Your Command = ", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            speak("Say that again sir")
            return "none"
        return Query


# wish me
def wish():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<=12:
        print("Good morning")
        speak("Good morning")
    elif time>12 and time<18:
        print("Good afternoon")
        speak("Good afternoon")
    else:
        print("Good evening")
        speak("Good evening")
    print("Hello there, I am Jarvis sir")
    speak("Hello there, I am Jarvis sir")


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    mint = time[14:16]
    print( "The time is " + hour + "Hours and" + mint + "Minutes")
    speak("The time is sir" + hour + "Hours and" + mint + "Minutes")


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
    for i in range(1,6):
        print(List[i])
        speak(List[i])


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
        print(f"today's {days[i]} news is: {headlines[i]}")
        speak(f"today's {days[i]} news is: {headlines[i]}")


# queries to do
def Take_query():
    wish()
    while (True):
        print()
        time.sleep(2)
        query = takeCommand().lower()
        if "open youtube" in query:
            List.append(query)
            print("Opening Youtube ")
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "what\'s up" in query or 'how are you' in query:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power']
            print(random.choice(setReplies))
            speak(random.choice(setReplies))
            continue

        elif "who are you" in query or 'what are you' in query:
            setReplies = [' I am KryptoKnite', 'In your system', 'I am an example of AI']
            print(random.choice(setReplies))
            speak(random.choice(setReplies))

        elif "open notepad" in query:
            List.append(query)
            print("Opening notepad ")
            speak("Opening notepad ")
            npath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            continue

        elif "open calculator" in query:
            List.append(query)
            print("Opening calculator ")
            speak("Opening calculator ")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            continue

        elif "open command prompt" in query:
            List.append(query)
            print("Opening cmd ")
            speak("Opening cmd ")
            os.system("start cmd")
            continue

        elif "play music" in query:
            List.append(query)
            print("playing music ")
            speak("playing music ")
            npath='C:\\Users\\mohit\\Documents\\music'
            songs = os.listdir(npath)
            os.startfile(os.path.join(npath,songs[1]))
            continue

        elif "open google" in query:
            List.append(query)
            print("Opening Google ")
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "tell me a joke" in query:
            List.append(query)
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            continue

        elif "search google" in query:
            List.append(query)
            print("Sir, what should i search ")
            speak("Sir, what should i search ")
            res = takeCommand().lower()
            webbrowser.open(f"{res}")
            continue

        elif "play songs on youtube" in query or "songs on youtube" in query:
            List.append(query)
            print("playing songs on youtube ")
            speak("playing songs on youtube ")
            kit.playonyt("mere nishan")
            continue

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            continue

        elif "tell me some news" in query or "news" in query:
            List.append(query)
            print("Please wait sir, fetching the latest news")
            speak("Please wait sir, fetching the latest news")
            news()
            continue

        elif "tell me our current location" in query or "tell me your current location" in query or "where are we now" in query:
            List.append(query)
            print("Sir wait, let me check")
            speak("Sir wait, let me check")
            try:
                add = requests.get("http://api.ipstack.com/check?access_key=1b0e22e97a1b9ffb090f30313d78fce3").text
                geo_data = json.loads(add)
                region = geo_data['region_name']
                country = geo_data['country_name']
                print(f"sir we are in {region} region of country {country}")
                speak(f"sir we are in {region} region of country {country}")
            except Exception as e:
                print("Sorry sir , due to network issues, iam not able to find")
                speak("Sorry sir , due to network issues, iam not able to find")
            continue

        # this will exit and terminate the program
        elif "bye" in query or "no thanks" in query or 'nothing' in query or 'abort' in query or 'stop' in query:
            print("okay, Bye Sir")
            speak("okay, Bye Sir")
            tracemalloc.stop()
            exit()

        elif "thank you" in query or "thanks" in query:
            print("happy to help you Sir")
            speak("happy to help you Sir")
            continue

        elif "which day it is" in query or "date" in query:
            List.append(query)
            tellDay()
            continue

        elif "tell me the time" in query or "time" in query or "what is the time now" in query:
            List.append(query)
            tellTime()
            continue

        elif "tell me your memory consumption" in query or "memory consumption" in query:
            List.append(query)
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage is {current / 10 * 6}MB; Peak was {peak / 10 * 6}MB")
            speak(f"Current memory usage is {current / 10 * 6}MB; Peak was {peak / 10 * 6}MB")
            continue

        elif "wikipedia" in query or "according to wikipedia" in query:
            List.append(query)
            print("Searching the wikipedia ")
            speak("Searching the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(result)
            speak(result)
            continue

        elif "tell me my history" in query or "history" in query:
            List.append(query)
            print("fetching history, please wait sir")
            speak("fetching history, please wait sir")
            history()
            continue

        elif "tell me what can you do" in query or "tell me your skills" in query or "skills" in query:
            List.append(query)
            print("Here are some things I can help you do")
            speak("Here are some things I can help you do")
            print("Check the Weather anywhere")
            speak("Check the Weather anywhere")
            print("Check Daily News")
            speak("Check daily news")
            print("Play Some Music")
            speak("play Some Music")
            print("Search Wikipedia")
            speak("search wikipedia")
            print("Play some music on youtube")
            speak("play some musics on youtube")
            print("Search the google")
            speak("search google")
            print("Raise or Low volume")
            speak("Raise or low volume")
            print("Open system apps")
            speak("open system apps")
            print("Spell any word")
            speak("Spell any word")
            print("Basic calculations")
            speak("Basic calculations")
            print("Find your location")
            speak("Find your location")
            print("check internet speed and availablity")
            speak("check internet speed and availablity")
            continue

        elif "tell me your name" in query or "what\'s your name" in query:
            List.append(query)
            print("I am Jarvis. Your deskstop Assistant")
            speak("I am Jarvis. Your deskstop Assistant")
            continue

        elif "can you calculate" in query or "do some calculations" in query:
            statement = takeCommand().lower()
            print(statement+"=")
            def find_operator(op,op1,op2):
                if op == '+':
                    return operator.add(op1,op2)
                elif op == '-':
                    return operator.sub(op1,op2)
                elif op == 'x':
                    return operator.mul(op1,op2)
                elif op == 'divided':
                    return operator.__truediv__(op1,op2)

            def eval_expression(op1,oper,op2):
                op1,op2 = int(op1),int(op2)
                return find_operator(oper,op1,op2)
            print("your result is")
            print(eval_expression(*(statement.split())))
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

        elif "weather in" in query or "what\'s the weather in" in query:
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"weather is {temp}")
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

        elif "what\'s the internet speed" in query or "internet speed" in query:
            st = speedtest.Speedtest()
            print(f"Download speed is {st.download()} and upload speed is {st.upload()}")
            continue

        elif "Check my internet connection" in query or "internet avilablity" in query or "internet connection" in query:
            url = "http://www.kite.com"
            timeout = 5
            try:
                request = requests.get(url, timeout=timeout)
                print("Connected to the Internet")
                speak("Connected to the Internet")
            except (requests.ConnectionError, requests.Timeout) as exception:
                print("No internet connection.")
                speak("No internet connection.")
            continue

        elif "spell the word" in query:
            word = query.replace("spell the word"," ")
            print(f"spelling of the word {word} is",end =" ")
            speak(f"spelling of the word {word} is")
            for i in word:
                print(i,end =" ")
                speak(i)
            continue


if __name__ == '__main__':
    tracemalloc.start()
    Take_query()
    tracemalloc.stop()