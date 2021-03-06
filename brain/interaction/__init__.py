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

from brain import *


class OdinRecon:
    def __init__(self, statement, speech, hearing):
        self.__statement = statement
        self.__odinspeech = speech
        self.__odin_hearing = hearing
        self.recon_interaction()

    def background(self):
        statement = self.__odin_hearing.listen()

        if 'odin' in statement:
            self.__odinspeech.speak("Hail!, Im listening you!")
            OdinRecon(self.__odin_hearing.listen(), self.__odinspeech, self.__odin_hearing)
        else:
            self.background()

    def recon_interaction(self):

        if 'help' in self.__statement:
            self.__odinspeech.speak("My developed is in progress, so i can't answer that now, sorry")
        elif 'wikipedia' in self.__statement:
            OdinWikipedia(self.__odinspeech, self.__odin_hearing)
        elif 'open' in self.__statement:
            OdinWebBrowser(self.__odinspeech, self.__odin_hearing, self.__statement)
        elif 'time' in self.__statement:
            OdinTime(self.__odinspeech)
        elif 'news' in self.__statement:
            OdinWebBrowser(self.__odinspeech, self.__odin_hearing, self.__statement)
        elif "search" in self.__statement:
            OdinWebBrowser(self.__odinspeech, self.__odin_hearing, self.__statement)
        elif "power off" or "turn off" in self.__statement:
            OdinCommand(self.__odinspeech, self.__odin_hearing, self.__statement).powerOff()
        elif 'sleep' in self.__statement:
            self.background()
        self.background()
