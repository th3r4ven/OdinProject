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

import pyttsx3


class OdinSpeechSetup:

    def __init__(self):
        self._odin_voice = pyttsx3.init()
        self.voices = self.odin_voice.getProperty('voices')

    def setup_speech(self):
        for voice in self.voices:
            if voice.gender == 'male':
                self._odin_voice.setProperty('voice', voice.id)  # try to get an male voice by default
                break
            else:
                try:
                    # Try david custom voice on windows (my system settings)
                    self._odin_voice.setProperty('voice', self.voices[2].id)
                except IndexError:
                    # try set default male system voice
                    self._odin_voice.setProperty('voice', self.voices[0].id)
                break

    def setup_speech_rate(self):
        self._odin_voice.setProperty('rate', self._odin_voice.getProperty('rate') - 55)

    def setup_speech_volume(self):
        self._odin_voice.setProperty('volume', 0.75)

    @property
    def odin_voice(self):
        return self._odin_voice
