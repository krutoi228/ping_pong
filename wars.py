import random
from pygame import *
import pygame as pg

font.init()

font = font.Font(None, 70)

# Цвета
fon = (156, 187, 255)
red = (255, 0, 0)
paint = (239, 241, 251)

# Переменные с True False
game = True
begin = True
play_game = False


# Переменные int

# Картинки
boll = transform.scale(image.load('boll.svg'), (30, 30))

player_1 = transform.scale(image.load('player_1.svg'), (21, 120))
player_2 = transform.scale(image.load('player_2.svg'), (21, 120))

# Надписи
_play = font.render(
    'PLAY', 1, paint
)