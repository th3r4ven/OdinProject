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

from setup import *
import datetime


class OdinSpeech:

    def __init__(self):
        self.odin_voice = setupSpeech.odin_voice

    def speak(self, text):
        self.odin_voice.say(text)
        self.odin_voice.runAndWait()

    def greetings(self):
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            self.speak("Good Morning")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")
