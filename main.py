import webbrowser
import time
import speech_recognition as sr
from time import ctime

import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            lisa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            lisa_speak('Sorry. I did not understand that')
        except sr.RequestError:
            lisa_speak('Sorry. Currently my speech service is not aviable')
        return voice_data


def lisa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    ran = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voiced):
    if ('what is your name' in voiced) or ('who are you' in voiced):
        lisa_speak('My name is Lisa')
    if ('what time is it' in voiced) or ('current time' in voiced):
        lisa_speak(ctime())
    if 'search' in voiced:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        lisa_speak('Here is what I found for ' + search)
    if 'find location' in voiced:
        location = record_audio('What location do you want?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        lisa_speak('Here is location I found for ' + location)
    if 'exit' in voiced:
        lisa_speak('Thank you')
        exit()


time.sleep(1)
lisa_speak("How can I help You?")
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
