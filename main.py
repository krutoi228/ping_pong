# Библиотеки
from pygame import *
import pygame as pg
import random

# Переменные 
import wars

# Инициализация PG
pg.init()

# Окно
window = display.set_mode((900, 600))

# Таймер
clock = pg.time.Clock()

# Кнопка play
play = transform.scale(wars._play, (100, 50))
play_rect = play.get_rect()
play_rect.x = 400
play_rect.y = 250

# Класс игроков
class PLayr(sprite.Sprite):
    def __init__(self, x_player, y_player, images, width, height):
        super().__init__()
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
class Boll(sprite.Sprite):
    def __init__(self, x_boll, y_boll, images, width, height):
        super().__init__()
        self.x_boll = x_boll
        self.y_boll = y_boll
        self.width = width
        self.height = height
        self.images = images
        self.boll = transform.scale(image.load(self.images), (width, height))
        self.rect = self.boll.get_rect()
        self.rect.x = x_boll
        self.rect.y = y_boll
    
    def draw(self):
        window.blit(self.boll, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += wars.vector_y
        self.rect.x += wars.vector_x

        if self.rect.y <= 0:
            wars.vector_y = 3

        if self.rect.y >= 570:
            wars.vector_y = -3

        if self.rect.x <= 0:
            wars.vector_x = 3
        
        if self.rect.x >= 870:
            wars.vector_x = -3

        if self.rect.x == wars.x and self.rect.y == wars.y:
            wars.vector_x = 3

playres = sprite.Group()
playres2 = sprite.Group()
bolls = sprite.Group()

player_1 = PLayr(50, 250, 'player_1.svg', 21, 120)
player_2 = PLayr(850, 250, 'player_2.svg', 21, 120)

playres.add(player_1)
playres2.add(player_2)

boll = Boll(450, 250, 'boll.svg', 30, 30)

bolls.add(boll)

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
        if sprite.groupcollide(bolls, playres, False, False):
            wars.vector_x = 3

        if sprite.groupcollide(bolls, playres2, False, False):
            wars.vector_x = -3

        window.blit(wars._check, (0, 8))

        player_1.draw()
        player_1.vector_p1()

        player_2.draw()
        player_2.vector_p2()

        boll.draw()
        bolls.update()

    clock.tick(60)
    display.update()