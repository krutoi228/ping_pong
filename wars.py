import random
from pygame import *
import pygame as pg

font.init()

font = font.Font(None, 70)

# Цвета
fon = (156, 187, 255)
red = (255, 0, 0)
paint = (239, 241, 251)
ping = (255, 169, 188)

# Переменные с True False
game = True
begin = True
play_game = False

# Переменные int
vector_y = -3
vector_x = -3

x = 50 
y = 250

# Надписи
_play = font.render(
    'ИГРАТЬ', 1, paint
)

_check = pg.font.SysFont('verbana', 50).render('Счет:', True, paint)