import pygame
import time
import random
import os

# Инициализация
pygame.init()

# Цвета для "современного" интерфейса
BG_COLOR = (30, 30, 30)       # Глубокий серый (вместо черного)
SNAKE_COLOR = (50, 200, 50)   # Сочный зеленый
APPLE_RED = (255, 50, 50)
TEXT_COLOR = (240, 240, 240)

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake: Apple Edition')
clock = pygame.time.Clock()

# Попытка загрузить картинку яблока
try:
    apple_img = pygame.image.load(os.path.join("images", "apple.png")).convert_alpha()
    apple_img = pygame.transform.scale(apple_img, (BLOCK_SIZE, BLOCK_SIZE))
except:
    apple_img = None  # Если файла нет, будем рисовать круг

# Шрифты
score_font = pygame.font.SysFont("avenir", 25, bold=True)

def display_ui(score, level):
    # Рисуем плашку для счета
    s_txt = score_font.render(f"SCORE: {score}", True, TEXT_COLOR)
    l_txt = score_font.render(f"LEVEL: {level}", True, TEXT_COLOR)
    dis.blit(s_txt, [20, 20])
    dis.blit(l_txt, [WIDTH - 120, 20])

def draw_snake(snake_list):
    """Рисуем змейку со скругленными углами."""
    for i, segment in enumerate(snake_list):
        # Рисуем голову чуть светлее
        color = (70, 255, 70) if i == len(snake_list) - 1 else SNAKE_COLOR
        
        # Рисуем скругленный прямоугольник (border_radius делает его красивым)
        pygame.draw.rect(dis, color, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE], border_radius=5)
        
        # Добавляем маленькие "глазки" на голову
        if i == len(snake_list) - 1:
            eye_color = (0, 0, 0)
            pygame.draw.circle(dis, eye_color, (segment[0]+5, segment[1]+5), 2)
            pygame.draw.circle(dis, eye_color, (segment[0]+15, segment[1]+5), 2)

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0
    
    snake_list = []
    length = 1
    score, level, speed = 0, 1, 10

    # Генерация первой еды
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:
        while game_close:
            dis.fill(BG_COLOR)
            msg = score_font.render("GAME OVER! Press C to Restart", True, APPLE_RED)
            dis.blit(msg, [WIDTH/4, HEIGHT/2])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c: gameLoop()
                    if event.key == pygame.K_q: game_over = True; game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change, x1_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change, x1_change = BLOCK_SIZE, 0

        # Столкновение со стеной
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(BG_COLOR)

        # РИСУЕМ ЯБЛОКО
        if apple_img:
            dis.blit(apple_img, (foodx, foody))
        else:
            # Если картинки нет, рисуем красивый красный круг с "бликом"
            pygame.draw.circle(dis, APPLE_RED, (foodx + 10, foody + 10), 10)
            pygame.draw.circle(dis, (255, 150, 150), (foodx + 6, foody + 6), 3)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head: game_close = True

        draw_snake(snake_list)
        display_ui(score, level)

        pygame.display.update()

        # Поедание яблока
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length += 1
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()