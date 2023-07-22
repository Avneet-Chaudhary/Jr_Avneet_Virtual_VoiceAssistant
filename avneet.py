#------------------------------------------------------------------------------------------------------------------#
#************************* INFO ABOUT LIBRARY AND MODULES THAT ARE USED IN JR. AVNEET *****************************#
#------------------------------------------------------------------------------------------------------------------#
"""
random:- Random variable generators.

*** time *** ================== This module provides various functions to manipulate time values.
*** webbrowser *** ============ Interfaces for launching and remotely controlling Web browsers.
*** imdb *** ================== This package can be used to retrieve information about a movie or a person from the IMDb database. It can fetch data through different media such as the IMDb web pages, or a SQL database.

*** pyautogui *** ============= PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

*** requests *** ============== Requests is a simple, yet elegant, HTTP library.
*** wikipedia *** ============= Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
*** pyttsx3 *** =============== pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

*** datetime *** ============== Concrete date/time and related types.
*** speech_recognition *** Library for performing speech recognition, with support for several engines and APIs, online and offline.

*** os *** ===================== OS routines for NT or Posix depending on what system we're on.
*** smtplib *** ================ The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

*** pyjokes *** ================ One line jokes for programmers (jokes as a service)
*** pywhatkit *** ============== it is one of the most popular library for WhatsApp and YouTube automation. 
*** winshell *** =============== winshell - convenience functions to access Windows shell functionality
"""

#====================================================================================================#
## SECTION - CODE BEGIN

# ------------------------------------------ Import Modules -----------------------------------------#
import random
import time
import webbrowser
import imdb
import pyautogui
import requests
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import os
import smtplib
from newsapi import NewsApiClient
import pyjokes
import wolframalpha
import pywhatkit
from time import sleep
import winshell
"""engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)"""

#-- Initialize the engine --#
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()


def speak(voice):
    '''This is speak function for voice'''
    engine.say(voice)
    engine.runAndWait()


#=========================================================================================================================#


def wishMe():
    ''''It works as wisher according to the time'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Junior Avneet, Sir. Please tell me how may I help you.")


#=========================================================================================================================#


def takeCommand():
    '''It takes microphone input from user and returns string output.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print('Say that again please...')
        return "none"
    return query


#====================================================================================================================#

# Dictionary for check system apps if it is present in the dictapp.
dictapp = {
    "command prompt": "cmd",
    "paint": "paint",
    # "word": "word",
    "excel": "excel",
    "chrome": "chrome",
    "vs code": "code",
    # "power point": "powerpoint",
    "pycharm": "pycharm",
    "notepad": "notepad",
    "outlook": "outlook"
}


def openappweb(query):
    '''This function is used to open the application if it is present in the dictionary or if it is contain .com .in .org'''
    speak(f"Alright sir! {query}")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("avneet", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


#=========================================================================================================================#


def closeappweb(query):
    '''This function will close the application'''
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")


#=========================================================================================================================#


def news():
    '''It takes microphone input from the command line and outputs the results'''

    newsapi = NewsApiClient(api_key='5840b303fb45654efdg46570e1016fc1155')
    speak("What topic you need the news about")
    topic = takeCommand()
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        speak(y["description"])


#=========================================================================================================================#


def Wikipedia():
    '''It takes microphone input from user and returns string output searching from Wikipedia'''

    speak('searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)


#=========================================================================================================================#


def play_music():
    '''This function will play music from given directory'''

    path = "D:\\music"
    files = os.listdir(path)
    song = random.choice(files)
    # os.startfile(song)

    # music_dir = "D:\\music"
    # songs = os.listdir(music_dir)
    os.startfile(os.path.join(path, song))


#=========================================================================================================================#


def search_movie():
    '''It takes microphone input from user and  ask for movie name to be searched and then speak the results'''

    speak("Say the movie name")

    # gathering information from IMDb
    moviesdb = imdb.IMDb()

    # search for title
    text = takeCommand()

    # passing input for searching movie
    movies = moviesdb.search_movie(text)

    speak("Searching for " + text)
    if len(movies) == 0:
        speak("No result found")
    else:

        speak("I found these:")

        for movie in movies:

            title = movie['title']
            year = movie['year']
            # speaking title with releasing year
            speak(f'{title}-{year}')

            info = movie.getID()
            movie = moviesdb.get_movie(info)

            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']

            # the below if-else is for past and future release
            if year < int(datetime.datetime.now().strftime("%Y")):
                speak(
                    f'{title}was released in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                print(
                    f'{title}was released in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')
                break

            else:
                print(
                    f'{title}will release in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')

                speak(
                    f'{title}will release in {year} has IMDB rating of {rating}.\
                    The plot summary of movie is{plot}')


#=========================================================================================================================#


def Day():
    '''This function is for telling the day of the week'''

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


#=========================================================================================================================#


def playGame():
    '''This function is called when the input is play game'''

    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS Goooooooooooooo.....")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors")  #Tuple
        com_choose = random.choice(choose)
        speak("choose")
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")

        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME : {Me_score+1} : COMPUTER : {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME : {Me_score} : COMPUTER : {Com_score}")
        i += 1

    print(f"FINAL SCORE :- ME : {Me_score} : COMPUTER : {Com_score}")


#=========================================================================================================================#


def currentWeather():
    '''Tell the weather data.'''

    city = "Aligarh"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16i878986esr6786879tre650b&units=metric"
    ).json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}"
    )
    # Google Open weather website
    # to get API of Open weather
    # api_key = "3d1a53b25705215"
    # speak(" City name ")
    # print("City name : ")
    # city_name = takeCommand()
    # base_url = f"https://openweathermap.org/find?utf8=%E2%9C%93&q=?{city_name}"  #http://api.openweathermap.org / data / 2.5 / weather?"

    # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    # response = requests.get(complete_url)
    # x = response.json()

    # if x["code"] != "404":
    #     y = x["main"]
    #     current_temperature = y["temp"]
    #     current_pressure = y["pressure"]
    #     current_humidiy = y["humidity"]
    #     z = x["weather"]
    #     weather_description = z[0]["description"]
    #     print(" Temperature (in kelvin unit) = " + str(current_temperature) +
    #           "\n atmospheric pressure (in hPa unit) =" +
    #           str(current_pressure) + "\n humidity (in percentage) = " +
    #           str(current_humidiy) + "\n description = " +
    #           str(weather_description))

    # else:
    #     speak(" City Not Found ")


#=========================================================================================================================#


def sendEmail(to, content):
    '''This function sends an email to the user'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('....@gmail.com', '@password')
    server.sendmail('....@gmail.com', to, content)
    server.close()


def sendMail():
    '''This function sends a mail to the specified address.'''
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "....@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")

    except Exception as e:
        print(e)
        speak("Sorry my friend. I am not able to send this email")


#=========================================================================================================================#


def searchYoutube(query):
    '''This function searches for videos on YouTube'''

    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("search youtube", "")
        query = query.replace("search on youtube", "")
        query = query.replace("avneet", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


#=========================================================================================================================#


def searchGoogle(query):
    '''This function searches for Google search results for a given query'''

    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("No speakable output available")


#=========================================================================================================================#


def searchQuestion():
    # Taking input from user
    speak('question')
    question = takeCommand()

    # App id obtained by the above steps
    app_id = "68-A2LU3"

    # Instance of wolf ram alpha
    # client class
    client = WolfRamAlpha.Client(app_id)

    # Stores the response from
    # wolf ram alpha
    res1 = client.query(question)

    # Includes only text from the response
    answer = next(res1.results).text
    speak(answer)


def WolfRamAlpha(query):
    apikey = "63UG788u9y8767gfLU3"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


#=========================================================================================================================#


def Calc(query):
    '''This function calculates for given query'''

    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = wolframalpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")


#==========================================================================================================================#

# class MainThread(QThread):
if __name__ == '__main__':
    # speak("Avneet Singh is awesome")
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query.
        if 'wikipedia' in query:
            Wikipedia()

        # elif 'youtube' in query:
        #     webbrowser.open('www.youtube.com')
        elif 'hello' in query or 'hi' in query or 'hai' in query:
            speak("Ram Ram, how are you? sir")

        elif 'Ram Ram' in query or 'ram ram' in query:
            speak("Ram Ram, Jeete Raho")

        elif 'time' in query:
            strTime = str(datetime.datetime.now().strftime('%H:%M:%S'))
            hour = strTime[0:2]
            min = strTime[3:5]
            hour = hour.replace("0", '')
            # print(hour)
            print(strTime)
            # speak('Sir, The time is+ "hour" + Hours and " + min + "Minutes"')
            speak("The time is sir" + hour + "Hours and" + min + "Minutes")

        elif 'who are you' in query or 'you do' in query or 'tell me something about you' in query:
            speak(
                "I am your friend avneet assistant.I have been created by My best friend, Avneet Singh. I can look up answers for you. if you need anything just ask, your wish in my commands"
            )

        elif 'how are you' in query:
            speak("I am good, feeling energetic. Hope to respond well.")

        elif 'i am good' in query or 'i am fine' in query:
            speak("thats great sir, have a good time ahead.")

        elif 'thanks' in query or 'thank you' in query:
            speak("you are welcome sir!")

        elif 'founder of you' in query or 'father of you' in query:
            speak("Honorable Mr. Avneet Singh")

        elif 'you speak good english' in query or 'speak good english' in query:
            speak(
                "Thank you sir! no doubt, i am one of the best virtual assistant. but i want to speak hindi, As it is my favorite language."
            )

        elif 'you are amazing' in query or 'you are awesome' in query or 'you are wonderful' in query or ' you are so good' in query:
            speak("Thank you sir! I know, I am...")

        elif ('date' in query):
            speak("Current date is " + str(datetime.datetime.now().day) + " " +
                  str(datetime.datetime.now().month) + " " +
                  str(datetime.datetime.now().year))

        elif 'day' in query:
            Day()
        # elif 'open code' in query:
        #     codePath = "C:\\Users\\avnee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
        elif 'email to avi' in query:
            sendMail()

        elif 'temperature' in query or 'weather' in query:
            currentWeather()
            # search = "temperature"
            # url = f"https://www.google.com//search?q{search}"
            # r = requests.get(url)
            # data = BeautifulSoup(r.text, 'html.parser')
            # temp = data.find("div", class_="BNeawe").text
            # speak(f"sir the current {search} is {temp}")

        elif 'avneet' in query or 'something about avneet' in query or 'tell me something about avneet' in query:
            webbrowser.open('https://avneetchaudhary.me/')
            speak('searching on google...')
            # query = query.replace("avneet", "")
            # results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            # print(results)
            # speak(results)

        elif 'search youtube' in query or 'search on youtube' in query:
            searchYoutube(query)

        elif 'google' in query or 'search google' in query:
            searchGoogle(query)

            # webbrowser.open('www.google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            play_music()
            # music_dir = os
            # songs = os.listdir(music_dir)
            # os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open app' in query or 'open' in query:
            openappweb(query)

        elif 'close app' in query or 'close' in query:
            closeappweb(query)

        elif ("news" in query):
            news()

        elif ("joke" in query):
            speak(pyjokes.get_joke())

        elif 'movie' in query:
            search_movie()

        elif ("bad joke" in query):
            speak("Sorry sir about any type of inconvenience")

        elif "teams" in query:
            speak("Alright Sir!, Opening microsoft team")
            os.startfile(
                'C:\\Users\\avnee\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'
            )

        elif "word" in query:
            speak("Alright Sir!, Opening microsoft word!")
            os.startfile(
                'C:\\Program Files (x86)\Microsoft Office\\root\Office16\\WINWORD.EXE'
            )

        elif 'visual studio' in query or 'open code' in query or 'open vs code' in query:
            speak("Alright Sir!, Opening  visual studio")
            os.startfile(
                "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\Common7\\IDE\\devenv.exe"
            )

        elif "ssms" in query:
            speak("Alright Sir!, Opening  SQL Server management studio")
            os.startfile(
                "C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 18\\Common7\\IDE\\Ssms.exe"
            )

        elif "power point" in query or 'open power point' in query:
            speak("Alright Sir!, Opening  Power Point!")
            os.startfile(
                "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            )

        elif 'question' in query.lower():
            searchQuestion()

        elif 'calculate' in query:
            # WolfRamAlpha()
            # Calc()
            query = query.replace("calculate", "")
            query = query.replace("avneet", "")
            Calc(query)

        # elif 'whatsapp' in query or 'send message' in query:
        #     from whatsapp import sendMessages
        #     sendMessages()

        elif 'play game' in query or 'play a game' in query:
            playGame()

        elif "open" in query:  #EASY METHOD
            query = query.replace("open", "")
            query = query.replace("avneet", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif 'bye' in query or 'sleep' in query:
            speak(
                "Bye. Take care, hope you get desired results. Happy to talk to you. Have fun."
            )
            exit()

        elif 'you are so boring' in query or 'you are so bad' in query or 'you are not good' in query:
            speak(
                'If you do not understand then Thats not my problem Sir, I think you need a break. I am best as my boss Mr Avneet singh try to make most of it. Thanks for your comments.'
            )

        elif 'you become angry' in query or 'you are so rude' in query or "don't angry" in query or "don't be rude" in query:
            speak(
                'No, I am not. As i am Jr. Avneet, so i follow my boss footprints. I will try to help you and continue to do that irrespective of results.if you do not get desired results then you dont have to complain, i do what i am able to do. thats it.'
            )

        elif 'cool' in query or 'cool down' in query or 'cool down avneet' in query:
            speak(
                "I am always cool, don't you know what i am able to do? i think you are not, no worries mannn..."
            )

        elif 'sorry' in query or 'sorry mate' in query:
            speak("Not a problem, Mannn....")

        elif 'festival' in query or 'which festival' in query:
            searchGoogle(query)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False,
                                         show_progress=False,
                                         sound=True)
            speak("Recycle Bin Recycled")

        # elif "where is" in query:
        #     query = query.replace("where is", "")
        #     location = query
        #     speak("User asked to Locate")
        #     speak(location)
        #     webbrowser.open(
        #         "https://www.googl8833819,7z" +
        #         location + "")

        elif "write a note" in query or 'write note' in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('avneet.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query or 'so note' in query:
            speak("Showing Notes")
            file = open("avneet.txt", "r")
            texxt = file.read()
            print(texxt)
            speak(texxt)

        elif "don't listen" in query or "stop listening" in query or 'take a break' in query or 'take break' in query:
            speak(
                "for how much time you want to stop Jr. Avneet from listening commands"
            )
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'bye' in query or 'sleep' in query:
            speak(
                "Bye. Take care, hope you get desired results. Happy to talk to you. Have fun."
            )
            exit()

        elif ' ' in query:
            speak('searching...')
            query = query.replace('', "")
            results = wikipedia.summary(query, sentences=2)
            # results = searchGoogle(query)
            speak("According to me")
            print(results)
            speak(results)
