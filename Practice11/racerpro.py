import pygame, sys
from pygame.locals import *
import random, time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (34, 139, 34)
GRAY  = (60, 60, 60)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
coin_score = 0
LEVEL_UP = 10

line_y = 0

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# группы
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# таймер спавна монет
SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, 1500)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("image", "Enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, 340), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(60, 340), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("image", "Player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 50 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < 350 and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 3, 5])

        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)

        if self.weight == 1:
            color = (255, 215, 0)
        elif self.weight == 3:
            color = (192, 192, 192)
        else:
            color = (205, 127, 50)

        pygame.draw.circle(self.image, color, (10, 10), 10)

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, 340), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# создание объектов
P1 = Player()
E1 = Enemy()

all_sprites.add(P1)
all_sprites.add(E1)
enemies.add(E1)


font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)


# === GAME LOOP ===
while True:

    # 1. события
    for event in pygame.event.get():
        if event.type == SPAWN_COIN:
            if random.random() < 0.8:  # шанс спавна
                coin = Coin()
                coins.add(coin)
                all_sprites.add(coin)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 2. логика (коллизии)
    collected = pygame.sprite.spritecollide(P1, coins, True)

    for coin in collected:
        SCORE += coin.weight
        coin_score += coin.weight

    if coin_score >= LEVEL_UP:
        SPEED += 1
        coin_score = 0

    # 3. движение
    for entity in all_sprites:
        entity.move()

    # 4. отрисовка
    DISPLAYSURF.fill(GREEN)
    pygame.draw.rect(DISPLAYSURF, GRAY, (50, 0, 300, SCREEN_HEIGHT))
    pygame.draw.line(DISPLAYSURF, WHITE, (50, 0), (50, SCREEN_HEIGHT), 5)
    pygame.draw.line(DISPLAYSURF, WHITE, (350, 0), (350, SCREEN_HEIGHT), 5)

    # разметка дороги
    line_y += SPEED
    if line_y > 100:
        line_y = 0
    for y in range(-100, SCREEN_HEIGHT, 100):
        pygame.draw.rect(DISPLAYSURF, WHITE, (195, y + line_y, 10, 50))

    # отрисовка спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    # счёт
    score_text = font_small.render(f"Score: {SCORE}", True, WHITE)
    DISPLAYSURF.blit(score_text, (10, 10))

    # столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        msg = font_big.render("CRASH!", True, BLACK)
        DISPLAYSURF.blit(msg, (80, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # 5. обновление
    pygame.display.update()
    FramePerSec.tick(FPS)