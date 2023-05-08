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

# Кнопка play
play = transform.scale(wars._play, (100, 50))
play_rect = play.get_rect()
play_rect.x = 400
play_rect.y = 250

# Класс игроков
class PLayr():
    def __init__(self, x_player, y_player, images, width, height):
        self.width = width
        self.height = height
        self.images = images
        self.playres = transform.scale(image.load(self.images), (self.width, self.height))
        self.rect = self.playres.get_rect()
        self.rect.x = x_player
        self.rect.y = y_player

    def draw(self):
        window.blit(self.playres, (self.rect.x, self.rect.y))

    # Прередвижение первого игрока
    def vector_p1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 8     
            wars.y -= 8

        if keys_pressed[K_s] and self.rect.y < 480:
            self.rect.y += 8
            wars.y += 8

    # Прередвижение второго игрока
    def vector_p2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 8

        if keys_pressed[K_DOWN] and self.rect.y < 480:
            self.rect.y += 8

# Класс мяч
class Boll():
    def __init__(self, x_boll, y_boll, images, width, height):
        self.x_boll = x_boll
        self.y_boll = y_boll
        self.images = images
        self.width = width
        self.height = height
        self.boll = transform.scale(image.load(self.images), (width, height))
    
    def draw(self):
        window.blit(self.boll, (self.x_boll, self.y_boll))
    
    def vector_boll(self, vectorX, vectorY):
        self.y_boll += vectorY
        self.x_boll += vectorX

        if self.y_boll <= 0:
            wars.vector_y = 3

        if self.y_boll >= 570:
            wars.vector_y = -3

        if self.x_boll <= 0:
            wars.vector_x = 3
        
        if self.x_boll >= 870:
            wars.vector_x = -3

        if self.x_boll == wars.x and self.y_boll == wars.y:
            wars.vector_x = 3

player_1 = PLayr(50, 250, 'player_1.svg', 21, 120)
player_2 = PLayr(850, 250, 'player_2.svg', 21, 120)

boll = Boll(450, 250, 'boll.svg', 30, 30)

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
        
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == pg.BUTTON_LEFT:
                if play_rect.collidepoint(e.pos):
                    wars.begin = False
                    wars.play_game = True
    
    if wars.begin == True:
        window.blit(play, (play_rect.x, play_rect.y))

    if wars.play_game == True:
        player_1.draw()
        player_1.vector_p1()

        player_2.draw()
        player_2.vector_p2()

        boll.draw()
        boll.vector_boll(wars.vector_x, wars.vector_y)

    clock.tick(60)
    display.update()