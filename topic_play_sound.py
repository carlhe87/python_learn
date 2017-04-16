import winsound
from collections import deque #allow fast list.popleft
from pygame import mixer #allow play mp3
#import vlc
from const import lib_path
lib_path[]


def play_sound(sound = "\a"):
        
    try:
        if sound.endswith(".wav"):
            winsound.PlaySound(sound, winsound.SND_FILENAME)
        elif sound.endswith(".mp3"):
            print "pygame player"
            mixer.init()
            mixer.music.load(sound)
            mixer.music.play()
            """
            print "vlc player"
            temp = vlc.MediaPlayer(sound)
            temp.play()
            """
        return
    except Exception:
        print "\a"
        print "Unknown error"