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

from webbrowser import open_new_tab as open_tab
from time import sleep


class OdinWebBrowser:

    def __init__(self, speech, hearing):
        self.__odinspeech = speech
        self.__odin_hearing = hearing
        self.search()

    def search(self):
        self.__odinspeech.speak('What do you want me to open on your browser?')
        statement = self.__odin_hearing.listen()
        if 'twitch' in statement:
            open_tab("https://twitch.com")
            self.__odinspeech.speak("Twich is now open, Enjoy!")
            sleep(3)
        elif 'github' in statement:
            open_tab("https://github.com")
            self.__odinspeech.speak("Github is now open, Enjoy!")
            sleep(3)
        elif 'youtube' in statement:
            open_tab("https://youtube.com")
            self.__odinspeech.speak("youtube is now open, Enjoy!")
            sleep(3)
        elif 'netflix' in statement:
            open_tab("https://netflix.com")
            self.__odinspeech.speak("Netflix is now open, Enjoy!")
            sleep(3)
        elif 'disney' in statement:
            open_tab("https://disneyplus.com/")
            self.__odinspeech.speak("Disney plus is now open, Enjoy!")
            sleep(3)
        elif 'google' in statement:
            open_tab("https://google.com")
            self.__odinspeech.speak("Google is now open, Enjoy!")
            sleep(3)
        elif 'gmail' in statement:
            open_tab("https://gmail.com")
            self.__odinspeech.speak("Gmail is now open, Enjoy!")
            sleep(3)
