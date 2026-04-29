import pygame
import random
import os

pygame.init()

# --- НАСТРОЙКИ ---
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

BG_COLOR = (30, 30, 30)
SNAKE_COLOR = (50, 200, 50)
APPLE_RED = (255, 50, 50)
TEXT_COLOR = (240, 240, 240)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Advanced")
clock = pygame.time.Clock()

font = pygame.font.SysFont("avenir", 25, bold=True)

# --- КЛАСС ЕДЫ ---
class Food:
    def __init__(self):
        # Позиция кратна сетке
        self.x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        
        # Вес еды (влияет на очки)
        self.weight = random.choice([1, 3, 5])
        
        # Время появления
        self.spawn_time = pygame.time.get_ticks()
        
        # Через сколько исчезнет (мс)
        self.lifetime = random.randint(3000, 7000)

    def draw(self, surface):
        # Цвет зависит от веса
        if self.weight == 1:
            color = (255, 50, 50)
        elif self.weight == 3:
            color = (255, 150, 50)
        else:
            color = (255, 255, 50)

        pygame.draw.circle(surface, color, (int(self.x + 10), int(self.y + 10)), 10)


def draw_snake(snake):
    for i, segment in enumerate(snake):
        color = (70, 255, 70) if i == len(snake) - 1 else SNAKE_COLOR
        pygame.draw.rect(screen, color, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE], border_radius=5)


def draw_ui(score, level):
    s = font.render(f"SCORE: {score}", True, TEXT_COLOR)
    l = font.render(f"LEVEL: {level}", True, TEXT_COLOR)
    screen.blit(s, (20, 10))
    screen.blit(l, (WIDTH - 140, 10))


def gameLoop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake = []
    length = 1

    score = 0
    level = 1
    speed = 10

    foods = []
    foods.append(Food())

    while not game_over:

        # --- GAME OVER SCREEN ---
        while game_close:
            screen.fill(BG_COLOR)
            msg = font.render("GAME OVER | C - restart | Q - quit", True, APPLE_RED)
            screen.blit(msg, (60, HEIGHT // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        # --- СОБЫТИЯ ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        # --- ДВИЖЕНИЕ ---
        x += dx
        y += dy

        # Столкновение со стеной
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BG_COLOR)

        # --- УДАЛЕНИЕ ЕДЫ ПО ТАЙМЕРУ ---
        current_time = pygame.time.get_ticks()
        for food in foods[:]:
            if current_time - food.spawn_time > food.lifetime:
                foods.remove(food)

        # --- СПАВН НОВОЙ ЕДЫ ---
        if len(foods) < 3:
            if random.random() < 0.02:
                foods.append(Food())

        # --- ОТРИСОВКА ЕДЫ ---
        for food in foods:
            food.draw(screen)

        # --- ЗМЕЙКА ---
        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Столкновение с собой
        for segment in snake[:-1]:
            if segment == head:
                game_close = True

        draw_snake(snake)
        draw_ui(score, level)

        # --- ПОЕДАНИЕ ---
        for food in foods[:]:
            if x == food.x and y == food.y:
                foods.remove(food)
                length += 1
                score += food.weight

                # Каждые 5 очков — ускорение
                if score % 5 == 0:
                    level += 1
                    speed += 1

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    quit()


gameLoop()