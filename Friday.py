import time
import tkinter
import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random
import wikipedia
import google
import datetime
import calendar
import math
from tkinter import *
# import time
import time as ctime
import webbrowser
import playsound



speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver not found")
except RuntimeError:
    print("Driver failed to initialize")

try:
    from googlesearch import search
except ImportError:
    print("No module named google found")

voices = engine.getProperty("voices")

for voice in voices:
    print(voice.id) # This is to list all the voices available of the computer
engine.setProperty("voice", "com.apple.speech.synthesis.voice.samantha")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate)

# engine.say("Hello Sir. This is Friday...")
engine.runAndWait()




def speak_text_cmd(cmd):
    print("Friday: "+cmd)
    engine.say(cmd)
    engine.runAndWait()


def read_voice_cmd(ask = False):
    voice_text = ""
    print("Listening...")
    if ask:
        speak_text_cmd(ask)
    with sr.Microphone() as source:
        audio = speech.listen(source)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand the audio, unknown error")
    except sr.RequestError as e:
        print("Request results from google speech recognition service error " + e)
    return voice_text


greeting_responses = ["Hi", "hey", "hello"]


# Finding information about a specific person


def getPerson(text):
    word_list = text.split()

    for i in range(0, len(word_list)):
        if i + 3 <= len(word_list) - 1 and word_list[i].lower() == "who" and word_list[i + 1].lower() == "is":
            return word_list[i + 2] + " " + word_list[i + 3]


# mathematics with program
def maths(query):
    word_list = query.split()

    for i in word_list:
        if "plus" in query:
            addition = i[0] + i[1]
            return addition
        if "minus" in query:
            subtraction = i[0] - i[1]
            return subtraction
        if "division" in query:
            division = i[0] / i[1]
            return division

    return ""




def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_Name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

    # List of ordinal numbers
    ordinal_Numbers = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th",
                       "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th",
                       "26th", "27th", "28th", "29th", "30th", "31st"]

    return "Today is " + weekday + " " + month_Name[monthNum - 1] + " the " + ordinal_Numbers[dayNum - 1] + "."





def responses(data):
    if "what is your name" in data:
        speak_text_cmd("Alexa")
    if "what is today's date" in  data:
        speak_text_cmd(getDate())
    if "what is the time " in data:
        speak_text_cmd(ctime())
    if "search" in data:
        search = read_voice_cmd("What do you want to search for?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak_text_cmd("Here is what i found for" + search)
    if "Find location" in data:
        locate = read_voice_cmd("what is the location")
        url = "https://www.google.nl/maps/place/" + locate + "/&mp"
        webbrowser.get().open(url)
        speak_text_cmd("Here is what i found for" + locate)
    if "exit" in data:
        speak_text_cmd("Byeeeee!!!. ")
        exit()


time.sleep(1)
speak_text_cmd("How can i help you")
while 1:
    data = read_voice_cmd()
    responses(data)


    # def showdata():
    #     txtName = responses(data)

        # txt.insert(0.1, txtName)

    # txt = Text(root, width=25,height=20,wrap=WORD)
    # txt.grid(row=3,columnspan=2,sticky=W)
    #
    # root.mainloop()
