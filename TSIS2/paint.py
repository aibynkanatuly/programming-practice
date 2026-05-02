import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

# ===== CANVAS =====
CANVAS_Y = 100
canvas = pygame.Surface((WIDTH, HEIGHT - CANVAS_Y))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# ===== SETTINGS =====
color = (0, 0, 0)
brush_size = 2
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

# TEXT
typing = False
text = ""
text_pos = (0, 0)
text_font = pygame.font.SysFont(None, 30)

# ===== BUTTONS =====
buttons = [
    Button(10, 10, 70, 30, (180,180,180), "Pencil"),
    Button(90, 10, 60, 30, (180,180,180), "Line"),
    Button(160, 10, 60, 30, (180,180,180), "Fill"),
    Button(230, 10, 60, 30, (180,180,180), "Text"),
    Button(300, 10, 70, 30, (180,180,180), "Rect"),
    Button(380, 10, 80, 30, (180,180,180), "Square"),
    Button(470, 10, 90, 30, (180,180,180), "Triangle"),
]

# ===== COLORS =====
colors = [
    (0,0,0), (255,0,0), (0,255,0),
    (0,0,255), (255,255,0), (255,165,0)
]

color_rects = []
for i, c in enumerate(colors):
    rect = pygame.Rect(10 + i*40, 50, 30, 30)
    color_rects.append((rect, c))

# ===== LOOP =====
running = True
while running:
    screen.fill((220, 220, 220))
    screen.blit(canvas, (0, CANVAS_Y))

    # UI
    for b in buttons:
        b.draw(screen, font)

    for rect, c in color_rects:
        pygame.draw.rect(screen, c, rect)

    pygame.draw.line(screen, (150,150,150), (0, 95), (WIDTH, 95), 2)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ===== KEYBOARD =====
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # TEXT
            if typing:
                if event.key == pygame.K_RETURN:
                    rendered = text_font.render(text, True, color)
                    canvas.blit(rendered, text_pos)
                    typing = False
                    text = ""

                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode

        # ===== MOUSE DOWN =====
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # кнопки
            for b in buttons:
                if b.is_clicked((x, y)):
                    tool = b.text.lower()
                    drawing = False
                    start_pos = None
                    break

            # цвета
            for rect, c in color_rects:
                if rect.collidepoint((x, y)):
                    color = c
                    break

            # canvas
            if y > CANVAS_Y:
                y -= CANVAS_Y

                if tool == "fill":
                    flood_fill(canvas, x, y, color)

                elif tool == "text":
                    typing = True
                    text_pos = (x, y)
                    text = ""

                else:
                    drawing = True
                    start_pos = (x, y)
                    last_pos = (x, y)

        # ===== MOUSE UP =====
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                x, y = event.pos
                y -= CANVAS_Y

                if tool == "line":
                    draw_line(canvas, color, start_pos, (x, y), brush_size)

                elif tool == "rect":
                    draw_rectangle(canvas, color, start_pos, (x, y), brush_size)

                elif tool == "square":
                    draw_square(canvas, color, start_pos, (x, y), brush_size)

                elif tool == "triangle":
                    draw_triangle(canvas, color, start_pos, (x, y), brush_size)

            drawing = False
            start_pos = None
            last_pos = None

        # ===== MOUSE MOVE =====
        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                x, y = event.pos
                y -= CANVAS_Y
                draw_pencil(canvas, color, last_pos, (x, y), brush_size)
                last_pos = (x, y)

    # ===== PREVIEW =====
    if drawing and start_pos:
        mx, my = pygame.mouse.get_pos()

        if my > CANVAS_Y:
            my_canvas = my - CANVAS_Y

            if tool == "line":
                pygame.draw.line(screen, color,
                                 (start_pos[0], start_pos[1] + CANVAS_Y),
                                 (mx, my),
                                 brush_size)

            elif tool == "rect":
                draw_rectangle(screen, color,
                               (start_pos[0], start_pos[1] + CANVAS_Y),
                               (mx, my),
                               brush_size)

            elif tool == "square":
                draw_square(screen, color,
                            (start_pos[0], start_pos[1] + CANVAS_Y),
                            (mx, my),
                            brush_size)

            elif tool == "triangle":
                draw_triangle(screen, color,
                              (start_pos[0], start_pos[1] + CANVAS_Y),
                              (mx, my),
                              brush_size)

    # TEXT PREVIEW
    if typing:
        preview = text_font.render(text, True, color)
        screen.blit(preview, (text_pos[0], text_pos[1] + CANVAS_Y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()