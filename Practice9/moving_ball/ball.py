import pygame

class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 20

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        # Проверка границ (ключевая часть задания)
        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)