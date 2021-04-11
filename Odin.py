import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


odin_voice = pyttsx3.init()
voices = odin_voice.getProperty('voices')


def speak(text):
    for voice in voices:
        odin_voice.setProperty('voice', voice.id)
        odin_voice.say(text)
        odin_voice.runAndWait()


speak("Hail son of Odin")
