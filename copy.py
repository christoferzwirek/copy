# -*- coding: utf-8 -*-
"""
Created on Sun May 11 18:02:57 2025

@author: Radek
"""


import shutil
print(shutil.which("flac"))
import speech_recognition as sr

# Inicjalizacja rozpoznawacza
recognizer = sr.Recognizer()

# Użycie mikrofonu jako źródła dźwięku
with sr.Microphone() as source:
    print("Powiedz coś...")
    audio = recognizer.listen(source)

    try:
        # Użycie domyślnego silnika Google
        #text = recognizer.recognize_google(audio, language="pl-PL")
        print("Rozpoznany tekst:",audio)#cos z klasą zrobić
    except sr.UnknownValueError:
        print("Nie rozpoznano mowy.")
    except sr.RequestError as e:
        print("Błąd połączenia z usługą Google:", e)
    else:
        print("elo")
