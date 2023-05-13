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

# Кнопка играть
play = transform.scale(wars._play, (120, 50))
play_rect = play.get_rect()
play_rect.x = 400
play_rect.y = 250

# Кнопка заново
reset = transform.scale(wars._reset, (100, 30))
reset_rect = reset.get_rect()
reset_rect.x = 380
reset_rect.y = 250

ch_goal1 = 0
ch_goal2 = 0

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
        global ch_goal1, ch_goal2

        self.rect.y += wars.vector_y
        self.rect.x += wars.vector_x

        if self.rect.y <= 0:
            wars.vector_y = 3

        if self.rect.y >= 570:
            wars.vector_y = -3

        if self.rect.x <= 0:
            wars.vector_x = 3
            self.rect.y = 250
            self.rect.x = 450
            ch_goal2 += 1
        
        if self.rect.x >= 870:
            wars.vector_x = -3
            self.rect.y = 250
            self.rect.x = 450
            ch_goal1 += 1

playres = sprite.Group()
playres2 = sprite.Group()
bolls = sprite.Group()

player_1 = PLayr(50, 250, 'player_1.svg', 21, 120)
player_2 = PLayr(820, 250, 'player_2.svg', 21, 120)

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
        
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == BUTTON_LEFT:
                if play_rect.collidepoint(e.pos) and wars.b == 0:
                    wars.begin = False
                    wars.play_game = True
                    wars.b = 1
                
                elif reset_rect.collidepoint(e.pos) and wars.play_game == False:
                    playres.empty()
                    bolls.empty()

                    playres.add(player_1)
                    playres2.add(player_2)

                    bolls.add(boll)
                    wars.play_game = True
                    ch_goal1 = 0
                    ch_goal2 = 0
    
    if wars.begin == True:
        window.blit(play, (play_rect.x, play_rect.y))

    if wars.play_game == True:
        goal1 = pg.font.SysFont('verbana', 50).render(str(ch_goal1), True, wars.ping)
        goal2 = pg.font.SysFont('verbana', 50).render(str(ch_goal2), True, wars.gray)

        if sprite.groupcollide(bolls, playres, False, False):
            wars.vector_x = 3

        if sprite.groupcollide(bolls, playres2, False, False):
            wars.vector_x = -3

        window.blit(wars._check, (300, 8))
        window.blit(goal1, (410, 13))
        window.blit(goal2, (450, 13))
        
        player_1.draw()
        player_1.vector_p1()

        player_2.draw()
        player_2.vector_p2()

        boll.draw()
        boll.update()
    
    if ch_goal1 == 3:
        window.blit(wars.win_1, (280, 200))
        window.blit(reset, (reset_rect.x, reset_rect.y))
        wars.play_game = False

    if ch_goal2 == 3:
        window.blit(wars.win_2, (280, 200))
        window.blit(reset, (reset_rect.x, reset_rect.y))
        wars.play_game = False

    clock.tick(60)
    display.update()