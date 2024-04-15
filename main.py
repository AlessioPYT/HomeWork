import random
import os
import pygame
import sys
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIHDT = 1200

FONT = pygame.font.SysFont("Verdana", 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLU = (0, 0, 255)
COLOR_BONUS = (0, 255, 0)

main_display = pygame.display.set_mode((WIHDT, HEIGHT))

bg = pygame.transform.scale(pygame.image.load("background.png"), (WIHDT, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH ="Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_color = (0, 0, 0) # black
player_size = (20, 20)
player = pygame.transform.scale(pygame.image.load("player.png"), (150, 80)).convert_alpha()
player_rect = player.get_rect().move(150, 350)
player_move_down = [0, 6]
player_move_right = [6, 0]
player_move_top = [0, -6]
player_move_left = [-6, 0]


def create_enemy():
    enemy_size = (5, 5)
    enemy = pygame.transform.scale(pygame.image.load("enemy.png"), (100, 30)).convert_alpha()
    enemy_rect = pygame.Rect(WIHDT, random.randint(50, HEIGHT - 50), *enemy_size)
    enemy_move = [random.randint(-10, -6), 0]
    return [enemy, enemy_rect, enemy_move]


def create_bonus():
    bonus_size = (5, 5)
    bonus = pygame.transform.scale(pygame.image.load("bonus.png"), (60, 80)).convert_alpha()
    bonus_rect = pygame.Rect(random.randint(40, WIHDT - 40), 40, *bonus_size)
    bonus_move = [0, random.randint(3, 6)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []

score = 0

image_index = 0

playing = True

while True:
    FPS.tick(600)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CREATE_ENEMY:
            enemies. append(create_enemy()) 
        if event.type == CREATE_BONUS:
            bonuses. append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0   
    
 #   main_display.fill(COLOR_WHITE)
    bg_X1 -= bg_move
    bg_X2 -= bg_move
    
    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:  # а чому стало навпаки (знак нерівності) ніж коли він відбивався?
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIHDT: # і тут
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0: # і тут
        player_rect = player_rect.move(player_move_top)

    if keys[K_LEFT] and player_rect.left > 0: # і тут
        player_rect = player_rect.move(player_move_left)

    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = pygame.quit()

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))

    main_display.blit(FONT.render(str(score), True, player_color), (WIHDT-50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    for enemy in enemies:
        if enemy [1].left < 0:
            enemies.pop(enemies.index(enemy))
    
    for bonus in bonuses:
        if bonus [1].bottom >= HEIGHT:
            bonuses.pop(bonuses.index(bonus))    