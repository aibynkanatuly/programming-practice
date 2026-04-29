import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 680))
    clock = pygame.time.Clock()

    radius = 5
    mode = 'line'  # текущий инструмент
    color = (255, 0, 0)

    drawing = False
    start_pos = None
    current_pos = None

    shapes = []  # список фигур (для постоянной отрисовки)

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                # выбор цвета
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

                # выбор инструмента
                elif event.key == pygame.K_1:
                    mode = 'line'
                elif event.key == pygame.K_2:
                    mode = 'square'
                elif event.key == pygame.K_3:
                    mode = 'right_triangle'
                elif event.key == pygame.K_4:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_5:
                    mode = 'rhombus'

            # начало рисования
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos

            # конец рисования → сохраняем фигуру
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    shapes.append((mode, start_pos, event.pos, color))

            # движение мыши
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos

        screen.fill((0, 0, 0))

        # --- РИСУЕМ СОХРАНЕННЫЕ ФИГУРЫ ---
        for shape in shapes:
            draw_shape(screen, *shape)

        # --- ПРЕДПРОСМОТР ТЕКУЩЕЙ ФИГУРЫ ---
        if drawing and start_pos and current_pos:
            draw_shape(screen, mode, start_pos, current_pos, color)

        pygame.display.flip()
        clock.tick(60)


def draw_shape(screen, mode, start, end, color):
    x1, y1 = start
    x2, y2 = end

    width = x2 - x1
    height = y2 - y1

    if mode == 'line':
        pygame.draw.line(screen, color, start, end, 3)

    # --- КВАДРАТ ---
    elif mode == 'square':
        size = min(abs(width), abs(height))
        rect = pygame.Rect(x1, y1, size, size)
        pygame.draw.rect(screen, color, rect, 2)

    # --- ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК ---
    elif mode == 'right_triangle':
        points = [start, (x1, y2), end]
        pygame.draw.polygon(screen, color, points, 2)

    # --- РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК ---
    elif mode == 'equilateral_triangle':
        size = abs(width)
        height = int(size * math.sqrt(3) / 2)

        p1 = (x1, y1)
        p2 = (x1 + size, y1)
        p3 = (x1 + size // 2, y1 - height)

        pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

    # --- РОМБ ---
    elif mode == 'rhombus':
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        points = [
            (cx, y1),   # верх
            (x2, cy),   # право
            (cx, y2),   # низ
            (x1, cy)    # лево
        ]

        pygame.draw.polygon(screen, color, points, 2)


main() 