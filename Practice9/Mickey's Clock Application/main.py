import pygame
import sys
import os
from clock import get_angles

pygame.init()

# Устанавливаем размер окна как у картинки
WIDTH, HEIGHT = 800, 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock = pygame.time.Clock()

# --- ЗАГРУЗКА ФОНА ---
# Загружаем твою картинку mickeyclock.jpg
try:
    bg = pygame.image.load("images/mickeyclock.jpeg").convert()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
except:
    print("Ошибка: Положи картинку в images/mickeyclock.jpeg")
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((255, 255, 255))

# --- ФУНКЦИЯ ДЛЯ СТРЕЛОК ---
def create_hand(color, width, length):
    # Создаем поверхность в два раза больше длины стрелки
    # Чтобы точка вращения (центр) была в основании стрелки
    surf = pygame.Surface((length * 2, length * 2), pygame.SRCALPHA)
    # Рисуем стрелку от центра вверх
    # pygame.draw.line(поверхность, цвет, старт, конец, ширина)
    pygame.draw.line(surf, color, (length, length), (length, 0), width)
    return surf

# Создаем стрелки
# Минутная (черная, потолще)
minute_hand_surf = create_hand((0, 0, 0), 8, 230)
# Секундная (красная, потоньше)
second_hand_surf = create_hand((255, 0, 0), 4, 300)

center_pos = (WIDTH // 2, HEIGHT // 2)

def draw_rotated_hand(surf, angle):
    # Вращаем (в Pygame rotate идет против часовой, поэтому в clock.py мы это учли)
    rotated_surf = pygame.transform.rotate(surf, angle)
    rect = rotated_surf.get_rect(center=center_pos)
    screen.blit(rotated_surf, rect)

# --- ГЛАВНЫЙ ЦИКЛ ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем углы из твоего файла clock.py
    min_angle, sec_angle = get_angles()

    # Рисуем фон (Микки Мауса)
    screen.blit(bg, (0, 0))

    # Рисуем стрелки
    draw_rotated_hand(minute_hand_surf, min_angle)
    draw_rotated_hand(second_hand_surf, sec_angle)

    # Маленькая точка в центре для красоты
    pygame.draw.circle(screen, (0, 0, 0), center_pos, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()