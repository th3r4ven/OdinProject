#  #!/usr/bin/env python3.8
#  #coding=UTF-8
#
#  Copyright (c) 2021 Matheus Chiarato | TH3R4VEN
#  #
#  This file is part of the program Odin Project
#  #
#  Odin Project is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 3 of the
#  License, or (at your option) any later version.
#  #
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
#  USA

import speech_recognition as sr
from brain import *


class OdinStartup:
    def __init__(self):
        self.__odin_speech = OdinSpeech()
        self.__odin_hearing = OdinHearing()

    def startup(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in').lower()
            if "start" or "odin start" in statement:
                self.__odin_speech.greetings()
                self.__odin_speech.speak('Hi, Im Odin, your personal Artificial Intelligence, how can I help you?')

                return OdinRecon(self.__odin_hearing.listen(), self.__odin_speech, self.__odin_hearing)

            elif "good bye" in statement or "ok bye" in statement or "bye" in statement:
                self.__odin_speech.speak('Ok, Im returning to valhalla')
                exit()
            else:
                self.startup()

        except Exception:
            self.__odin_speech.speak("I dont understand you, please say it again")
            self.startup()
        return
