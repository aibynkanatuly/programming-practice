import pygame
import random
import os


WIDTH = 500
HEIGHT = 700

ROAD_X = 80
ROAD_W = 340
LANES = [125, 205, 285, 365]

FINISH_DISTANCE = 3000


def load_image(path, size, color):
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, size)

    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf


class Player:
    def __init__(self, assets, color):
        self.lane = 1
        self.x = LANES[self.lane]
        self.y = 570
        self.w = 50
        self.h = 80
        self.speed = 5
        self.shield = False
        self.color = color

        if color == "red":
            self.image = assets["player"]
        elif color == "blue":
            self.image = assets["player_blue"]
        else:
            self.image = assets["player_green"]

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.x = LANES[self.lane]

    def move_right(self):
        if self.lane < len(LANES) - 1:
            self.lane += 1
            self.x = LANES[self.lane]

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.shield:
            pygame.draw.rect(screen, (0, 180, 255), self.rect, 4)


class RoadObject:
    def __init__(self, kind, lane, y, image, value=0):
        self.kind = kind
        self.lane = lane
        self.x = LANES[lane]
        self.y = y
        self.image = image
        self.value = value
        self.w = image.get_width()
        self.h = image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.timer = 0

    def update(self, speed):
        self.y += speed
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.timer += 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class RacerGame:
    def __init__(self, username, settings):
        self.username = username
        self.settings = settings
        self.assets = self.load_assets()
        self.player = Player(self.assets, settings["car_color"])

        self.objects = []
        self.coins = 0
        self.distance = 0
        self.score = 0
        self.road_offset = 0
        self.finished = False
        self.game_over = False

        self.base_speed = 5
        self.spawn_timer = 0
        self.power_timer = 0
        self.active_power = None

        if settings["difficulty"] == "easy":
            self.spawn_limit = 55
        elif settings["difficulty"] == "hard":
            self.spawn_limit = 25
        else:
            self.spawn_limit = 40

    def load_assets(self):
        assets = {}

        assets["player"] = load_image("assets/player.png", (50, 80), (220, 0, 0))
        assets["player_blue"] = load_image("assets/player.png", (50, 80), (0, 80, 220))
        assets["player_green"] = load_image("assets/player.png", (50, 80), (0, 180, 80))

        assets["enemy"] = load_image("assets/enemy.png", (50, 80), (40, 40, 40))
        assets["coin"] = load_image("assets/coin.webp", (35, 35), (255, 210, 0))
        assets["nitro"] = load_image("assets/nitro.png", (40, 40), (0, 200, 255))
        assets["shield"] = load_image("assets/shield.png", (40, 40), (0, 100, 255))
        assets["repair"] = load_image("assets/repair.png", (40, 40), (0, 220, 0))
        assets["oil"] = load_image("assets/fuel.png", (50, 40), (20, 20, 20))
        assets["barrier"] = load_image("assets/barrier.png", (60, 45), (255, 80, 0))
        assets["pothole"] = load_image("assets/pothole.jpg", (55, 40), (90, 60, 40))

        return assets

    def current_speed(self):
        if self.active_power == "nitro":
            return self.base_speed + 4
        return self.base_speed

    def spawn_object(self):
        lane = random.randint(0, 3)

        if abs(LANES[lane] - self.player.x) < 10 and random.randint(1, 100) <= 60:
            lane = random.choice([i for i in range(4) if i != self.player.lane])

        r = random.randint(1, 100)

        if r <= 25:
            obj = RoadObject("enemy", lane, -90, self.assets["enemy"])
        elif r <= 40:
            obj = RoadObject("coin", lane, -40, self.assets["coin"], random.choice([1, 2, 3]))
        elif r <= 55:
            obj = RoadObject("oil", lane, -40, self.assets["oil"])
        elif r <= 68:
            obj = RoadObject("barrier", lane, -50, self.assets["barrier"])
        elif r <= 78:
            obj = RoadObject("pothole", lane, -45, self.assets["pothole"])
        elif r <= 86:
            obj = RoadObject("nitro", lane, -45, self.assets["nitro"])
        elif r <= 94:
            obj = RoadObject("shield", lane, -45, self.assets["shield"])
        else:
            obj = RoadObject("repair", lane, -45, self.assets["repair"])

        self.objects.append(obj)

    def update(self):
        if self.game_over:
            return

        speed = self.current_speed()

        self.distance += speed / 5
        self.score = int(self.distance + self.coins * 20)

        if self.distance >= FINISH_DISTANCE:
            self.finished = True
            self.game_over = True

        self.road_offset += speed
        if self.road_offset >= 60:
            self.road_offset = 0

        self.spawn_timer += 1

        density = max(12, self.spawn_limit - int(self.distance / 300))

        if self.spawn_timer >= density:
            self.spawn_object()
            self.spawn_timer = 0

        if self.active_power == "nitro":
            self.power_timer -= 1
            if self.power_timer <= 0:
                self.active_power = None

        self.player.update()

        for obj in self.objects[:]:
            obj.update(speed)

            if obj.y > HEIGHT:
                self.objects.remove(obj)
                continue

            if obj.kind in ["nitro", "shield", "repair"] and obj.timer > 300:
                self.objects.remove(obj)
                continue

            if self.player.rect.colliderect(obj.rect):
                self.handle_collision(obj)

    def handle_collision(self, obj):
        if obj.kind == "coin":
            self.coins += obj.value
            self.objects.remove(obj)

        elif obj.kind == "nitro":
            if self.active_power is None:
                self.active_power = "nitro"
                self.power_timer = 240
            self.objects.remove(obj)

        elif obj.kind == "shield":
            if self.active_power is None:
                self.active_power = "shield"
                self.player.shield = True
            self.objects.remove(obj)

        elif obj.kind == "repair":
            if self.objects:
                for item in self.objects[:]:
                    if item.kind in ["oil", "barrier", "pothole"]:
                        self.objects.remove(item)
                        break
            self.objects.remove(obj)

        elif obj.kind in ["enemy", "barrier", "pothole"]:
            if self.player.shield:
                self.player.shield = False
                self.active_power = None
                self.objects.remove(obj)
            else:
                self.game_over = True

        elif obj.kind == "oil":
            self.base_speed = max(3, self.base_speed - 1)
            self.objects.remove(obj)

    def draw_road(self, screen):
        pygame.draw.rect(screen, (40, 40, 40), (ROAD_X, 0, ROAD_W, HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (ROAD_X, 0, 5, HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (ROAD_X + ROAD_W, 0, 5, HEIGHT))

        for x in [165, 245, 325]:
            y = -60 + self.road_offset
            while y < HEIGHT:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 5, 35))
                y += 70

    def draw_hud(self, screen, font):
        remaining = max(0, int(FINISH_DISTANCE - self.distance))

        text1 = font.render("Name: " + self.username, True, (255, 255, 255))
        text2 = font.render("Score: " + str(self.score), True, (255, 255, 255))
        text3 = font.render("Coins: " + str(self.coins), True, (255, 255, 255))
        text4 = font.render("Distance: " + str(int(self.distance)), True, (255, 255, 255))
        text5 = font.render("Remaining: " + str(remaining), True, (255, 255, 255))

        screen.blit(text1, (10, 10))
        screen.blit(text2, (10, 35))
        screen.blit(text3, (10, 60))
        screen.blit(text4, (10, 85))
        screen.blit(text5, (10, 110))

        if self.active_power == "nitro":
            seconds = self.power_timer // 60
            text = font.render("Power: Nitro " + str(seconds), True, (0, 255, 255))
            screen.blit(text, (300, 10))
        elif self.active_power == "shield":
            text = font.render("Power: Shield", True, (0, 255, 255))
            screen.blit(text, (300, 10))
        else:
            text = font.render("Power: None", True, (255, 255, 255))
            screen.blit(text, (300, 10))

    def draw(self, screen, font):
        screen.fill((20, 120, 20))
        self.draw_road(screen)

        for obj in self.objects:
            obj.draw(screen)

        self.player.draw(screen)
        self.draw_hud(screen, font)