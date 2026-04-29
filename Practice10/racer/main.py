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
GREEN = (34, 139, 34)  # Темно-зеленый
GRAY  = (60, 60, 60)   # Цвет асфальта

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
line_y = 0 # Для анимации разметки

DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("images", "Enemy.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, SCREEN_WIDTH-60), 0)  

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(60, SCREEN_WIDTH - 60), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("images", "Player.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Ограничиваем движение, чтобы не выезжать на траву
        if self.rect.left > 50:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 350:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2 # Чуть помедленнее ускорение     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # --- РИСУЕМ ТРАССУ ---
    DISPLAYSURF.fill(GREEN) # Трава
    pygame.draw.rect(DISPLAYSURF, GRAY, (50, 0, 300, SCREEN_HEIGHT)) # Дорога
    pygame.draw.line(DISPLAYSURF, WHITE, (50, 0), (50, SCREEN_HEIGHT), 5) # Левый край
    pygame.draw.line(DISPLAYSURF, WHITE, (350, 0), (350, SCREEN_HEIGHT), 5) # Правый край

    # Анимация пунктира
    line_y += SPEED
    if line_y > 100:
        line_y = 0
    for y in range(-100, SCREEN_HEIGHT, 100):
        pygame.draw.rect(DISPLAYSURF, WHITE, (195, y + line_y, 10, 50))

    # Отрисовка счета
    scores = font_small.render(f"Score: {SCORE}", True, WHITE)
    DISPLAYSURF.blit(scores, (10, 10))

    # Движение объектов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Столкновение
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        msg = font_big.render("CRASH!", True, BLACK)
        DISPLAYSURF.blit(msg, (80, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)