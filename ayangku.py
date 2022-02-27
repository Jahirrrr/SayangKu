# Sayangku Virtual Asisstant Projects


import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import datetime
import sys
import brainlypy
from translate import Translator


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
Mic = sr.Microphone()


def sayangku_talk(text):
    engine.say(text)
    engine.runAndWait()


def im_talk():
    try:
        with Mic as source:
            print('mendengarkan.....')
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice, language='id')
            command = command.lower()
            if 'sayang' in command:
                command = command.replace('sayang', '')
                print(command)
    except:
       pass
    return command



def run_sayangku():
    command = im_talk()
    print(command)
    if 'bangun' in command:
        sayangku_talk('online, babe')
    elif 'jam' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        sayangku_talk('The time is' + time)
    elif 'cariin di wikipedia' in command:
        person = command.replace('cariin di wikipedia', '')
        info = wikipedia.summary(person, 1)
        sayangku_talk('here the answers, babe')
        print(info)
    elif 'terjemahkan' in command:
        ans = command.replace('terjemahkan', '')
        translator = Translator(to_lang="en")
        translation = translator.translate(ans)
        sayangku_talk("here you translate :")
        print(translation)
    elif 'carikan jawaban' in command:
        br = command.replace('carikan jawaban', '')
        brainlypy.set_lang("id")
        results = brainlypy.search(br)
        question = results.questions[0]
        sayangku_talk("here the answer: ")
        print('Jawaban 1:', question.answers[0])
        if question.answers_count == 2:
            print('Jawaban 2:', question.answers[1])
        if question.answers_count == 3:
            print('Jawaban 3:', question.answers[2])
        if question.answers_count == 4:
            print('Jawaban 4:', question.answers[3])
        if question.answers_count == 5:
            print('Jawaban 5:', question.answers[4])
    elif 'udahan yang' in command:
        sayangku_talk('okay')
        sys.exit()

    else:
        sayangku_talk('please say the command again, babe')


while True:
    run_sayangku()
