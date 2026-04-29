import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()

# Создаём шар по центру
ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT)

running = True
while running:
    clock.tick(60)  # FPS (плавность)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -20)
            elif event.key == pygame.K_DOWN:
                ball.move(0, 20)
            elif event.key == pygame.K_LEFT:
                ball.move(-20, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(20, 0)

    screen.fill(WHITE)

    ball.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()