# Библиотеки
from pygame import *
import pygame as pg
import random

# Переменные 
import wars

# Инициализация PG
pg.init()

# Окно
window = pg.display.set_mode((900, 600))

# Таймер
clock = pg.time.Clock()
clock.tick(60)

# Кнопка play
play = transform.scale(wars._play, (100, 50))
play_rect = play.get_rect()
play_rect.x = 400
play_rect.y = 250

# Класс игроков
class PLayr():
    def __init__(self, x_player, y_player, images, width, height):
        self.y_player = wars.y1
        self.x_player = x_player
        self.width = width
        self.height = height
        self.image = images
        self.playres = transform.scale(image.load(images), (self.width, self.height))
    
    def draw(self):
        window.blit(self.playres, (self.x_player, self.y_player))


player_1 = PLayr(50, wars.y1, 'player_1.svg', 21, 120)
player_2 = PLayr(850, wars.y2, 'player_2.svg', 21, 120)


# Игровой цикл
while wars.game:
    keys_pressed = key.get_pressed()
    # Фон игры
    window.fill(wars.fon)

    for e in event.get():
        if e.type == QUIT:
            wars.game = False

        elif keys_pressed[K_ESCAPE]:
            wars.game = False

        elif keys_pressed[K_w]:
            wars.y1 = wars.y1 - 3
        
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == pg.BUTTON_LEFT:
                if play_rect.collidepoint(e.pos):
                    wars.begin = False
                    wars.play_game = True
    
    if wars.begin == True:
        window.blit(play, (play_rect.x, play_rect.y))

    if wars.play_game == True:
        window.blit(wars.boll, (450, 250))
        player_1.draw()
        player_2.draw()

    display.update()