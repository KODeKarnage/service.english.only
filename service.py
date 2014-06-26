#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2014 KODeKarnage
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import xbmc
import xbmcaddon


__addon__        = xbmcaddon.Addon('service.english.only')
__addonid__      = __addon__.getAddonInfo('id')
__setting__      = __addon__.getSetting
script_path       = __addon__.getAddonInfo('path')
addon_path       = xbmc.translatePath('special://home/addons')

check_audio = False

def log(msg, label=''):

    if label:
        combined_message = 'service.ENGLISH.only ::-:: ' + str(label) + ' = ' + str(msg)
    else:
        combined_message = 'service.ENGLISH.only ::-:: ' + str(msg)

    xbmc.log(msg=combined_message)



class myPlayer(xbmc.Player):

    def __init__(self, *args, **kwargs):
        pass

    def onPlayBackStarted(self):
        global check_audio
        check_audio = True
        


def Main():

    english_player = myPlayer()

    global check_audio

    while not xbmc.abortRequested:

        xbmc.sleep(500)

        if check_audio:

            english_player.showSubtitles(False)

            check_audio = False
            
            streams = english_player.getAvailableAudioStreams()

            if streams:
                if 'eng' in streams:
                    stream_number = streams.index('eng')
                    english_player.setAudioStream(stream_number)


if __name__ == "__main__":
    Main()
