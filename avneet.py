# ------------------------------------------------------------------------------------------------------------------#
# ************************* INFO ABOUT LIBRARY AND MODULES THAT ARE USED IN JR. AVNEET *****************************#
# ------------------------------------------------------------------------------------------------------------------#
"""
*** random *** ================ Random variable generators.

*** time *** ================== This module provides various functions to manipulate time values.
*** webbrowser *** ============ Interfaces for launching and remotely controlling Web browsers.
*** imdb *** ================== This package can be used to retrieve information about a movie or a person from the IMDb database. It can fetch data through different media such as the IMDb web pages, or a SQL database.

*** pyautogui *** ============= PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

*** requests *** ============== Requests is a simple, yet elegant, HTTP library.
*** wikipedia *** ============= Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
*** pyttsx3 *** =============== pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

*** datetime *** ============== Concrete date/time and related types.
*** speech_recognition *** ==== Library for performing speech recognition, with support for several engines and APIs, online and offline.

*** os *** ==================== OS routines for NT or Posix depending on what system we're on.
*** smtplib *** =============== The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

*** pyjokes *** =============== One line jokes for programmers (jokes as a service)
*** pywhatkit *** ============= it is one of the most popular library for WhatsApp and YouTube automation.
*** winshell *** ============== winshell - convenience functions to access Windows shell functionality
"""

# ====================================================================================================#
# SECTION - CODE BEGIN

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
# import winshell
import winreg


# ------------------------------------------------------------------------------------------------------------------------#
"""engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)"""
# -- Initialize the engine --#
engine = pyttsx3.init()

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def speak(voice):
    '''This is speak function for voice'''
    engine.say(voice)
    engine.runAndWait()


# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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


# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂

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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def news():
    '''It takes microphone input from the command line and outputs the results'''
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    speak("What topic you need the news about")
    topic = takeCommand()
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        speak(y["description"])

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def Wikipedia():
    '''It takes microphone input from user and returns string output searching from Wikipedia'''
    speak('searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


music_dir = None
music_files = []
current_song = None
current_index = -1

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def find_music_directory():
    '''This function finds the music directory on Windows.'''
    global music_dir
    # Open the Windows registry
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
    )
    # Get the value of the 'My Music' directory key
    try:
        music_dir = winreg.QueryValueEx(reg_key, "My Music")[0]
    except FileNotFoundError:
        print("Music directory not found.")
    # Close the registry key
    winreg.CloseKey(reg_key)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def get_music_files():
    '''This function retrieves the list of music files from the music directory.'''
    global music_dir, music_files
    music_files = []
    # Find the music directory
    find_music_directory()
    # Check if the music directory exists
    if music_dir and os.path.exists(music_dir) and os.path.isdir(
            music_dir):
        # Get the list of music files
        music_files = [
            file for file in os.listdir(music_dir) if file.endswith(".mp3")
        ]
        # Shuffle the music files
        random.shuffle(music_files)
        if not music_files:
            print("No music files found in the Music directory.")
    else:
        print("Music directory not found.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def play_song(song):
    '''This function plays a specific song.'''
    global music_dir, current_song
    current_song = song
    song_path = os.path.join(music_dir, current_song)
    # Play the song using the default media player
    os.startfile(song_path)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def play_music():
    '''This function will play music from the music directory on the current computer.'''
    global music_files, current_index
    # Get the list of music files
    get_music_files()
    # Check if there are any music files
    if music_files:
        print("Playing music...")
        # Check if it's the first time playing
        if current_index == -1:
            # Choose a random music file
            current_index = random.randint(0, len(music_files) - 1)
        else:
            # Play the current song again
            play_song(music_files[current_index])
        # Open lyrics in a web browser
        song_name = os.path.splitext(music_files[current_index])[0]
        search_query = f"{song_name} lyrics"
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        # Display the currently playing song name
        print(f"Now playing: {song_name}")
    else:
        print("No music files found in the Music directory.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def pause_music():
    '''This function pauses the currently playing song.'''
    global current_song
    if current_song:
        # Pause the song using the default media player
        os.system("TASKKILL /F /IM wmplayer.exe")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def play_previous_song():
    '''This function plays the previous song.'''
    global music_files, current_index
    # Check if there are any music files
    if music_files:
        # Decrease the current index
        current_index = (current_index - 1) % len(music_files)
        # Play the previous song
        play_song(music_files[current_index])

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def play_next_song():
    '''This function plays the next song.'''
    global music_files, current_index
    # Check if there are any music files
    if music_files:
        # Increase the current index
        current_index = (current_index + 1) % len(music_files)
        # Play the next song
        play_song(music_files[current_index])

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def skip_song(seconds):
    '''This function skips the currently playing song by a specified number of seconds.'''
    global current_song
    if current_song:
        # Skip the song using the default media player
        os.system(
            f'echo "seek {seconds}" > "C:\\Program Files\\Windows Media Player\\wmplayer.exe"'
        )
# def play_music():
#     '''This function will play music from given directory'''
#     path = "D:\\music"
#     files = os.listdir(path)
#     song = random.choice(files)
#     # os.startfile(song)
#     # music_dir = "D:\\music"
#     # songs = os.listdir(music_dir)
#     os.startfile(os.path.join(path, song))

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playGame():
    '''This function is called when the input is play game'''
    speak("Which game would you like to play?")
    query = takeCommand().lower()
    if "rock paper scissors" in query:
        playRockPaperScissors()
    elif "guess the number" in query:
        playGuessTheNumber()
    elif "tic tac toe" in query:
        playTicTacToe()
    elif "hangman" in query:
        playHangman()
    elif "dice roll" in query:
        playDiceRoll()
    elif "word search" in query:
        playWordSearch()
    elif "memory game" in query:
        playMemoryGame()
    elif "coin flip" in query:
        playCoinFlip()
    elif "battleship" in query:
        playBattleship()
    elif "sudoku" in query:
        playSudoku()
    else:
        speak("I'm sorry, I don't know that game.")
    speak(
        "Thank you for playing! If you want to play more games, just let me know."
    )

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playRockPaperScissors():
    '''This function plays the Rock Paper Scissors game'''
    speak("Let's play Rock Paper Scissors!")
    speak("Choose: rock, paper, or scissors?")
    user_choice = takeCommand().lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if user_choice in choices:
        speak(f"You chose {user_choice}.")
        speak(f"The computer chose {computer_choice}.")
        if user_choice == computer_choice:
            speak("It's a tie!")
        elif ((user_choice == "rock" and computer_choice == "scissors")
              or (user_choice == "paper" and computer_choice == "rock") or
              (user_choice == "scissors" and computer_choice == "paper")):
            speak("You win!")
        else:
            speak("The computer wins!")
    else:
        speak("Sorry, I didn't understand your choice.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playGuessTheNumber():
    '''This function plays the Guess the Number game'''
    speak("Let's play Guess the Number!")
    speak("Think of a number between 1 and 100.")
    speak(
        "I will try to guess it. Let me know if my guess is too high, too low, or correct."
    )
    lower_bound = 1
    upper_bound = 100
    while True:
        guess = (lower_bound + upper_bound) // 2
        speak(f"My guess is {guess}. Is it too high, too low, or correct?")
        feedback = takeCommand().lower()
        if "high" in feedback:
            upper_bound = guess - 1
        elif "low" in feedback:
            lower_bound = guess + 1
        elif "correct" in feedback:
            speak("I guessed it right! That was fun.")
            break
        else:
            speak("Sorry, I didn't understand your feedback.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playTicTacToe():
    '''This function plays the Tic Tac Toe game'''
    board = [" " for _ in range(9)]
    player = "X"
    game_over = False

    def draw_board():
        print("-------------")
        print("|", board[0], "|", board[1], "|", board[2], "|")
        print("-------------")
        print("|", board[3], "|", board[4], "|", board[5], "|")
        print("-------------")
        print("|", board[6], "|", board[7], "|", board[8], "|")
        print("-------------")

    def check_win():
        nonlocal game_over
        winning_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # columns
            [0, 4, 8],
            [2, 4, 6]  # diagonals
        ]
        for combo in winning_combos:
            if board[combo[0]] == board[combo[1]] == board[
                    combo[2]] != " ":
                print(f"Player {board[combo[0]]} wins!")
                game_over = True
                break
        if " " not in board and not game_over:
            print("It's a tie!")
            game_over = True

    def make_move():
        nonlocal player
        print(f"Player {player}'s turn. Enter a position (1-9):")
        position = int(input()) - 1
        if board[position] == " ":
            board[position] = player
            draw_board()
            check_win()
            if not game_over:
                player = "O" if player == "X" else "X"
                make_move()
        else:
            print("Invalid move. Try again.")
            make_move()
    draw_board()
    make_move()

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playHangman():
    '''This function plays the Hangman game'''
    words = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        'gizmo',
        'glowworm',
        'glyph',
        'gnarly',
        'gnostic',
        'gossip',
        'grogginess',
        'haiku',
        'haphazard',
        'hyphen',
        'iatrogenic',
        'icebox',
        'injury',
        'ivory',
        'ivy',
        'jackpot',
        'jaundice',
        'jawbreaker',
        'jaywalk',
        'jazziest',
        'jazzy',
        'jelly',
        'jigsaw',
        'jinx',
        'jiujitsu',
        'jockey',
    ]
    word = random.choice(words).lower()
    guessed_letters = []
    tries = 6

    def draw_hangman():
        stages = [
            '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            ''', '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
            ''', '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
            ''', '''
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
            ''', '''
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
            ''', '''
                --------
                |      |
                |      O
                |    
                |      
                |
                -
            ''', '''
                --------
                |      |
                |      
                |    
                |      
                |
                -
            '''
        ]
        return stages[tries]

    def draw_word():
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def make_guess():
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                guessed_letters.append(guess)
                if guess not in word:
                    nonlocal tries
                    tries -= 1
        else:
            print("Invalid input. Please enter a single letter.")
    print("Let's play Hangman!")
    print("Guess the word:")
    draw_word()
    while tries > 0:
        print(draw_hangman())
        make_guess()
        draw_word()
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly.")
            break
    if tries == 0:
        print("Sorry, you ran out of tries. The word was", word)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playDiceRoll():
    '''This function is called when the user wants to play a dice rolling game'''
    speak("Let's play the dice rolling game!")
    speak("How many dice would you like to roll?")
    num_dice = int(takeCommand())
    speak("How many sides should each die have?")
    num_sides = int(takeCommand())
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    speak(f"You rolled {num_dice} dice with {num_sides} sides each.")
    speak(f"The total sum of the rolls is {total}.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playWordSearch():
    '''This function is called when the user wants to play a word search game'''
    words = [
        'apple', 'banana', 'cherry', 'grape', 'orange', 'kiwi', 'melon',
        'pear', 'plum', 'strawberry'
    ]
    grid = [['a', 'p', 'p', 'l', 'e'], ['b', 'a', 'n', 'a', 'n'],
            ['c', 'h', 'e', 'r', 'r'], ['g', 'r', 'a', 'p', 'e'],
            ['o', 'r', 'a', 'n', 'g'], ['k', 'i', 'w', 'i', 'i'],
            ['m', 'e', 'l', 'o', 'n'], ['p', 'e', 'a', 'r', 'p'],
            ['p', 'l', 'u', 'm', 's'], ['s', 't', 'r', 'a', 'w']]
    found_words = []
    found_count = 0
    while found_count < len(words):
        speak("Find a fruit:")
        word = takeCommand().lower()
        if word in words and word not in found_words:
            found_words.append(word)
            found_count += 1
            speak("You found a fruit!")
        else:
            speak("Try again.")
    speak("Congratulations! You found all the fruits!")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playMemoryGame():
    '''This function is called when the user wants to play the Memory Game'''
    speak("Welcome to the Memory Game!")
    speak(
        "I will show you a sequence of numbers. Your task is to repeat the sequence correctly."
    )
    speak("Are you ready?")
    ready = takeCommand().lower()
    if "yes" in ready:
        numbers = generateNumberSequence()
        showNumberSequence(numbers)
        user_sequence = getUserInput(len(numbers))
        checkUserInput(numbers, user_sequence)
    else:
        speak("Okay, maybe next time!")


def generateNumberSequence():
    '''This function generates a random sequence of numbers for the Memory Game'''
    numbers = []
    for _ in range(5):
        numbers.append(random.randint(0, 9))
    return numbers


def showNumberSequence(numbers):
    '''This function displays the number sequence to the user'''
    speak("Remember the following sequence:")
    for number in numbers:
        speak(str(number))
        time.sleep(1)
    speak("Now it's your turn!")


def getUserInput(length):
    '''This function takes user input for the number sequence'''
    user_sequence = []
    for _ in range(length):
        user_number = int(takeCommand())
        user_sequence.append(user_number)
    return user_sequence


def checkUserInput(numbers, user_sequence):
    '''This function checks the user's input against the generated number sequence'''
    if user_sequence == numbers:
        speak("Congratulations! You got the sequence right.")
    else:
        speak("Oops! That's not the correct sequence.")
        speak(
            f"The correct sequence was: {' '.join(str(num) for num in numbers)}"
        )

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playCoinFlip():
    '''This function allows the user to play the coin flip game'''
    speak(
        "Let's play the coin flip game! I will flip a coin, and you have to guess if it's heads or tails."
    )
    speak("Okay, here's the coin flip. Please make your guess.")
    guess = takeCommand().lower()
    if guess == "heads" or guess == "tails":
        result = random.choice(["heads", "tails"])
        speak(f"The coin landed on {result}.")
        if guess == result:
            speak("Congratulations! You guessed it right.")
        else:
            speak("Oops! Better luck next time.")
    else:
        speak(
            "Sorry, I didn't recognize that. Please say heads or tails to make your guess."
        )


def create_board(size):
    '''Create an empty game board'''
    board = []
    for _ in range(size):
        row = ['O'] * size
        board.append(row)
    return board


def display_board(board):
    '''Display the game board'''
    for row in board:
        print(' '.join(row))


def place_ships(board, num_ships):
    '''Randomly place ships on the game board'''
    ships = []
    size = len(board)
    for _ in range(num_ships):
        ship = (random.randint(0, size - 1), random.randint(0, size - 1))
        while ship in ships:
            ship = (random.randint(0,
                                   size - 1), random.randint(0, size - 1))
        ships.append(ship)
    return ships


def check_guess(board, ships, row, col):
    '''Check if the user's guess is a hit or miss'''
    if (row, col) in ships:
        board[row][col] = 'X'
        print("Hit!")
        return True
    else:
        board[row][col] = 'M'
        print("Miss!")
        return False


def all_ships_sunk(ships):
    '''Check if all ships are sunk'''
    for ship in ships:
        if 'X' not in ship:
            return False
    return True

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playBattleship():
    '''This function allows the user to play the Battleship game'''
    # Game setup
    board_size = 5
    num_ships = 3
    board = create_board(board_size)
    ships = place_ships(board, num_ships)
    num_guesses = 0
    # Game loop
    while True:
        # Display the board
        display_board(board)
        # Get user's guess
        print("Enter row number (1-5):")
        row = int(input()) - 1
        print("Enter column number (1-5):")
        col = int(input()) - 1
        # Process the user's guess
        hit = check_guess(board, ships, row, col)
        num_guesses += 1
        # Check if all ships are sunk
        if all_ships_sunk(ships):
            display_board(board)
            print("Congratulations! You sunk all the ships!")
            print("Number of guesses:", num_guesses)
            break
        # Check if the user wants to quit
        print("Do you want to quit the game? (yes/no)")
        response = input().lower()
        if "yes" in response:
            print("Thanks for playing!")
            break
        # Clear the console
        # Uncomment the line below if you're running the code in a console/terminal
        # import os; os.system('cls' if os.name == 'nt' else 'clear')
    # Game over
    print("Game over!")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def playSudoku():
    '''This function allows the user to play a game of Sudoku'''
    # Code for the Sudoku game goes here
    # You can implement your own logic or use a Sudoku solver library
    # Example code:
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    # Display the initial Sudoku board
    print("Initial Sudoku board:")
    for row in board:
        print(row)
    # Play the game logic goes here
    # Example code:
    solved_board = [[5, 3, 4, 6, 7, 8, 9, 1,
                     2], [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6,
                     7], [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9,
                     1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8,
                     4], [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    # Display the solved Sudoku board
    print("Solved Sudoku board:")
    for row in solved_board:
        print(row)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def listen():
    '''Listen to user's voice command and return the recognized text.'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError:
        print(
            "Sorry, I am unable to access the Google Speech Recognition service."
        )
    return ""

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def currentWeather(city):
    '''Tell the weather data for a specific city.'''
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        speak(
            f"The temperature in {city} is {temperature} degree Celsius. The weather is {weather_description}."
        )
    else:
        speak(
            "Sorry, I couldn't fetch the weather data for the requested city."
        )

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def sendEmail():
    '''This function sends an email to the user'''
    # Update the email credentials and sender information
    sender_email = 'avneetchaudhary8273@gmail.com'
    sender_password = '@Mahi8273'
    # Ask for recipient's email address
    print("Please provide the email address of the recipient.")
    recipient_email = takeCommand()
    if not recipient_email:
        print(
            "Recipient's email address not recognized. Please try again.")
        return
    # Ask for email subject
    print("Please say the email subject.")
    subject = takeCommand()
    if not subject:
        print("Email subject not recognized. Please try again.")
        return
    # Ask for email content
    print("Please say the email content.")
    content = takeCommand()
    if not content:
        print("Email content not recognized. Please try again.")
        return
    # Format the email message
    message = f"Subject: {subject}\n\n{content}"
    try:
        # Create an SMTP server object
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start the server connection
        server.ehlo()
        server.starttls()
        # Login to the email account
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, recipient_email, message)
        # Close the server connection
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def searchYoutube(query):
    '''This function searches for videos on YouTube'''
    if "youtube" in query or "play" in query:
        query = query.replace(
            "youtube",
            "").strip()  # Remove the word "youtube" from the query
        query = query.replace(
            "play youtube",
            "").strip()  # Remove the word "play youtube" from the query
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(
            web
        )  # Open the YouTube search results in the default web browser
        speak("Here are the search results for your query.")
        # Get the list of search results
        search_results = pywhatkit.search(query)
        # if query:
        #     # Check if the query contains the word "play"
        #     if "play" in query:
        #         # Extract the video name from the query
        #         video_name = query.replace("play", "").strip()
        #         # Call the function to play the video on YouTube
        #         play_video_by_name(video_name)
        #         return
        # If it doesn't contain "play," open the YouTube search results
        if search_results:
            speak(
                "Please choose a video from the search results by saying the corresponding number."
            )
            # Show the search results to the user
            for i, result in enumerate(search_results, start=1):
                speak(f"{i}. {result}")
            # Get the user's choice of video
            choice = get_user_choice(len(search_results))
            if choice is not None:
                play_video(search_results[choice - 1])
            else:
                speak("Invalid choice. Please try again.")
        else:
            speak("No search results found.")
    else:
        speak("Please provide a valid search query.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def get_user_choice(max_choice):
    '''Get the user's choice from the search results'''
    choice = None
    while choice is None:
        user_input = get_voice_input(
            "Please say the corresponding number: ")
        if user_input.isdigit() and 1 <= int(user_input) <= max_choice:
            choice = int(user_input)
    return choice

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def play_video(video_url):
    '''Play the selected video'''
    pywhatkit.playonyt(video_url)  # Play the selected YouTube video
    speak("Playing the selected video.")


def play_video_by_name(video_name):
    '''Play the video on YouTube by name'''
    # Search for the video on YouTube
    video_url = pywhatkit.search(video_name)
    if video_url:
        # If a video URL is found, play the video
        play_video(video_url[0])
    else:
        speak("Video not found.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def close_web_browser():
    '''Close the web browser window'''
    # Add code to close the web browser window
    # For example, if using Chrome, you can use the following code:
    os.system("taskkill /im chrome.exe /f")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def get_voice_input(prompt):
    '''Get user input through voice'''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def searchGoogle(query):
    '''This function performs a Google search for a given query'''
    if "google" in query:
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on Google")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            web_results = pywhatkit.search(query, num_results=5)
            speak("Here are some related web results:")
            for i, result in enumerate(web_results, start=1):
                speak(f"Website {i}: {result}")
        except wikipedia.exceptions.DisambiguationError as e:
            # If there are multiple results, provide the first result
            result = wikipedia.summary(e.options[0], sentences=2)
            speak(result)
        except wikipedia.exceptions.PageError:
            speak("Sorry, I could not find any information on that topic.")
        except Exception as e:
            speak("An error occurred while performing the Google search.")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def searchQuestion():
    # Taking input from user
    speak('question')
    question = takeCommand()
    # App id obtained by the above steps
    app_id = "63UG78-AP8GPX2LU3"
    # Instance of wolf ram alpha
    # client class
    client = WolfRamAlpha.Client(app_id)
    # Stores the response from
    # wolf ram alpha
    res1 = client.query(question)
    # Includes only text from the response
    answer = next(res1.results).text
    speak(answer)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def WolfRamAlpha(query):
    apikey = "63UG78-AP8GPX2LU3"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


def Calc(query):
    '''This function calculates for given query'''
    Term = str(query)
    Term = Term.replace("avneet", "")
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

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂


if __name__ == '__main__':

    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query.
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
            print(strTime)

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
            speak("Current date is " + str(datetime.datetime.now().day) +
                  " " + str(datetime.datetime.now().month) + " " +
                  str(datetime.datetime.now().year))
        elif 'day' in query:
            Day()

        elif 'email to avi' in query:
            sendEmail()
        elif 'temperature' in query or 'weather' in query:
            currentWeather()

        elif 'avneet' in query or 'something about avneet' in query or 'tell me something about avneet' in query:
            # webbrowser.open('https://avneetchaudhary.me/')
            speak(
                'I can not describe in words, Mr. Avneet is everything to me. I am nothing without Mr Avneet...'
            )

        elif 'search youtube' in query or 'search on youtube' in query:
            searchYoutube(query)
        elif 'google' in query or 'search google' in query:
            searchGoogle(query)
            # webbrowser.open('www.google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            play_music()

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

            query = query.replace("calculate", "")
            query = query.replace("avneet", "")
            Calc(query)

        elif 'play game' in query or 'play a game' in query:
            playGame()
        elif "open" in query:  # EASY METHOD
            query = query.replace("open", "")
            query = query.replace("avneet", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
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
            query = query.replace("avneet", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            # Get the current date
            today = datetime.date.today()
            # Check if the query asks for the festival today or festival date
            if "today" in query or "is on" in query or "date" in query:
                # Perform a Google search
                pywhatkit.search(query)
                # Get the search results
                search_results = searchGoogle.search(query, num_results=1)
                if search_results:
                    # Speak the search result
                    speak(
                        f"According to Google, {search_results[0].description}"
                    )
                else:
                    speak(
                        "Sorry, I couldn't find any search results for festivals."
                    )
            else:
                speak(
                    "Sorry, I didn't understand your question. Could you please ask again?"
                )
        elif 'is love' in query:
            speak("It is the 7th sense that destroy all other senses")

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
            speak("According to me")
            print(results)
            speak(results)

# ❂☆━━━━━━━━━━━━━━━━━━━☆❂ ✨✨✨✨✨✨✨✨✨✨ ❂☆━━━━━━━━━━━━━━━━━━━☆❂
'''Personal Voice Assistant
Developed by: Avneet Singh
Year: 2023

All rights reserved. No part of this personal voice assistant project may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the developer, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

For inquiries, please contact:
Avneet Singh
Email: ch.avneet01@gmail.com'''
