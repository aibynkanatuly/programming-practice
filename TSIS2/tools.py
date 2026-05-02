import pygame

# ======================
# DRAW FUNCTIONS
# ======================

def draw_pencil(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


# ======================
# SHAPES
# ======================

def draw_rectangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
    pygame.draw.rect(surface, color, rect, size)


def draw_square(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(surface, color, rect, size)


def draw_triangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    points = [
        (x1, y2),
        ((x1 + x2) // 2, y1),
        (x2, y2)
    ]
    pygame.draw.polygon(surface, color, points, size)

# ======================
# FLOOD FILL (улучшенный)
# ======================

def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]
    visited = set()

    while stack:
        x, y = stack.pop()

        if (x, y) in visited:
            continue

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)
        visited.add((x, y))

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


# ======================
# UI BUTTON
# ======================

class Button:
    def __init__(self, x, y, w, h, color, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        label = font.render(self.text, True, (0, 0, 0))
        screen.blit(label, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)