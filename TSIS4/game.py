import pygame
import random
import json


CELL = 20
W = 600
H = 600
GRID = 30 


class SnakeGame:
    def __init__(self, username, best):
        self.username = username
        self.best = best

        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.dir = (1, 0)
        self.next_dir = (1, 0)

        self.score = 0
        self.level = 1
        self.base_speed = 10
        self.speed = self.base_speed

        self.obstacles = []

        self.food = self.spawn_empty()
        self.poison = None

        self.power = None
        self.power_type = None
        self.power_spawn_time = 0

        self.active_power = None
        self.active_until = 0
        self.shield = False

        self.last_move = 0
        self.food_count = 0
        self.game_over = False

        self.load_settings()

    def load_settings(self):
        with open("settings.json", "r", encoding="utf-8") as file:
            s = json.load(file)

        self.color = tuple(s["color"])
        self.grid = s["grid"]
        self.sound = s["sound"]

    def all_busy(self):
        busy = set(self.snake)
        busy.update(self.obstacles)

        if self.food:
            busy.add(self.food)

        if self.poison:
            busy.add(self.poison)

        if self.power:
            busy.add(self.power)

        return busy

    def spawn_empty(self):
        while True:
            p = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
            if p not in self.snake and p not in self.obstacles:
                return p

    def spawn_poison(self):
        if self.poison is None:
            self.poison = self.spawn_empty()

    def spawn_power(self):
        if self.power is None:
            self.power = self.spawn_empty()
            self.power_type = random.choice(["speed", "slow", "shield"])
            self.power_spawn_time = pygame.time.get_ticks()

    def safe_obstacle_position(self):
        head = self.snake[0]

        while True:
            p = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))

            if p in self.all_busy():
                continue

            if abs(p[0] - head[0]) <= 2 and abs(p[1] - head[1]) <= 2:
                continue

            return p

    def spawn_obstacles(self):
        self.obstacles = []

        count = min(5 + self.level, 15)

        for _ in range(count):
            self.obstacles.append(self.safe_obstacle_position())

    def set_dir(self, new_dir):
        if new_dir[0] == -self.dir[0] and new_dir[1] == -self.dir[1]:
            return

        self.next_dir = new_dir

    def apply_power_timer(self):
        now = pygame.time.get_ticks()

        if self.power and now - self.power_spawn_time > 8000:
            self.power = None
            self.power_type = None

        if self.active_power in ["speed", "slow"] and now > self.active_until:
            self.active_power = None
            self.speed = self.base_speed

    def collision(self, head):
        if head[0] < 0 or head[1] < 0 or head[0] >= GRID or head[1] >= GRID:
            return True

        if head in self.snake:
            return True

        if head in self.obstacles:
            return True

        return False

    def handle_collision(self):
        if self.shield:
            self.shield = False
            self.active_power = None
            return False

        return True

    def move(self):
        self.dir = self.next_dir

        head = (
            self.snake[0][0] + self.dir[0],
            self.snake[0][1] + self.dir[1]
        )

        if self.collision(head):
            if self.handle_collision():
                self.game_over = True
                return
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 10
            self.food_count += 1
            self.food = self.spawn_empty()

            if self.food_count % 5 == 0:
                self.level += 1
                self.base_speed += 2

                if self.active_power is None:
                    self.speed = self.base_speed

                if self.level >= 3:
                    self.spawn_obstacles()

        elif self.poison and head == self.poison:
            self.poison = None

            if len(self.snake) <= 3:
                self.game_over = True
                return

            self.snake.pop()
            self.snake.pop()
            self.snake.pop()

        elif self.power and head == self.power:
            now = pygame.time.get_ticks()

            if self.power_type == "speed":
                self.active_power = "speed"
                self.speed = self.base_speed + 5
                self.active_until = now + 5000

            elif self.power_type == "slow":
                self.active_power = "slow"
                self.speed = max(4, self.base_speed - 5)
                self.active_until = now + 5000

            elif self.power_type == "shield":
                self.active_power = "shield"
                self.shield = True

            self.power = None
            self.power_type = None

        else:
            self.snake.pop()

    def update(self):
        if self.game_over:
            return

        now = pygame.time.get_ticks()
        self.apply_power_timer()

        if now - self.last_move > 1000 // self.speed:
            self.move()
            self.last_move = now

        if random.randint(1, 250) == 1:
            self.spawn_poison()

        if random.randint(1, 350) == 1:
            self.spawn_power()

    def draw_grid(self, screen):
        if not self.grid:
            return

        for x in range(0, W, CELL):
            pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, H))

        for y in range(0, H, CELL):
            pygame.draw.line(screen, (30, 30, 30), (0, y), (W, y))

    def draw(self, screen, font):
        screen.fill((0, 0, 0))
        self.draw_grid(screen)

        for x, y in self.snake:
            pygame.draw.rect(screen, self.color, (x * CELL, y * CELL, CELL, CELL))

        pygame.draw.rect(screen, (255, 255, 0), (self.food[0] * CELL, self.food[1] * CELL, CELL, CELL))

        if self.poison:
            pygame.draw.rect(screen, (150, 0, 0), (self.poison[0] * CELL, self.poison[1] * CELL, CELL, CELL))

        if self.power:
            if self.power_type == "speed":
                c = (255, 120, 0)
            elif self.power_type == "slow":
                c = (0, 180, 255)
            else:
                c = (180, 0, 255)

            pygame.draw.rect(screen, c, (self.power[0] * CELL, self.power[1] * CELL, CELL, CELL))

        for x, y in self.obstacles:
            pygame.draw.rect(screen, (100, 100, 100), (x * CELL, y * CELL, CELL, CELL))

        info = f"Score: {self.score}  Level: {self.level}  Best: {self.best}"
        text = font.render(info, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        power = "None"
        if self.active_power == "speed":
            power = "Speed " + str(max(0, (self.active_until - pygame.time.get_ticks()) // 1000))
        elif self.active_power == "slow":
            power = "Slow " + str(max(0, (self.active_until - pygame.time.get_ticks()) // 1000))
        elif self.active_power == "shield":
            power = "Shield"

        text2 = font.render("Power: " + power, True, (255, 255, 255))
        screen.blit(text2, (10, 35))