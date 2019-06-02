# Faça um programa em Python que abra e reproduza um áudio em MP3. 

from pygame import *

mixer.init()
mixer.music.load('Ai No Corrida - QUINCY JONES 1981.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
