#python 021
from pygame.mixer_music import load 
from pygame import init
from pygame.mixer_music import play
from pygame.event import wait


init()
load('BoDleasons_-_For_Medical.mp3')
play()
input()
wait()