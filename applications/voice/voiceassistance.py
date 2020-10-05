import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import os
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        speak('Listening..')
    try:
        print('Recognizing...')
        voice = r.recognize_google(audio)
        print(f"user said {voice} \n")
    except Exception as err:
        print(f"ERROR:{err}")
        speak('Please Say Again')
        return "none"
    return voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good evening!')
    speak('Hello I am your assistant')
    time.sleep(1)
    speak('How may I help you sir?')


if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak('opening')
            browser = webdriver.Chrome()
            browser.get('https://www.youtube.com/')
        elif 'song' in query:
            speak('playing')
            browser = webdriver.Chrome()
            query = query.replace('play song', "")
            browser.get('https://www.google.com/')
            browser.find_element_by_name("q").send_keys(query)
            time.sleep(5)
            browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]").click()
            time.sleep(5)
            browser.switch_to_alert().dismiss()
            time.sleep(1)
            browser.find_element_by_class_name("j0joJb").click()
        elif 'google search' in query:
            speak('searching')
            browser = webdriver.Chrome()
            query = query.replace('google search', "")
            browser.get('https://www.google.com/')
            browser.find_element_by_name("q").send_keys(query)
            time.sleep(2)
            browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]").click()
            time.sleep(2)
        elif 'code' in query:
            speak('opening')
            os.startfile("C:/Users/dell pc/AppData/Local/Programs/Microsoft VS Code/Code.exe")
        elif 'exit' in query:
            speak("ok bye")
            break
        else:
            pass
            # more to be written
