import pygame
import json
from game import SnakeGame
from db import save_game, get_top10, get_best


pygame.init()

W = 600
H = 600

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("TSIS4 Snake")

font = pygame.font.SysFont("arial", 26)
small = pygame.font.SysFont("arial", 20)

state = "menu"
username = ""
game = None
best = 0
saved = False

clock = pygame.time.Clock()
running = True


def load_settings():
    with open("settings.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_settings(s):
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(s, file, indent=4)


settings = load_settings()


def text(txt, x, y, color=(255, 255, 255), f=None):
    if f is None:
        f = font

    img = f.render(txt, True, color)
    screen.blit(img, (x, y))


def button(x, y, w, h, label):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, (50, 50, 50), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect, 2)

    img = font.render(label, True, (255, 255, 255))
    img_rect = img.get_rect(center=rect.center)
    screen.blit(img, img_rect)

    return rect


def draw_menu():
    screen.fill((0, 0, 0))

    text("SNAKE GAME", 210, 90, (0, 255, 0))
    text("Username: " + username, 170, 150, (255, 255, 0))

    play = button(200, 220, 200, 50, "Play")
    lead = button(200, 290, 200, 50, "Leaderboard")
    sett = button(200, 360, 200, 50, "Settings")
    quitb = button(200, 430, 200, 50, "Quit")

    text("Type username on keyboard", 170, 510, (180, 180, 180), small)

    return play, lead, sett, quitb


def draw_leaderboard():
    screen.fill((0, 0, 0))
    text("TOP 10", 250, 40, (255, 255, 0))

    rows = get_top10()

    y = 100
    text("Rank  Name        Score  Level  Date", 50, y, (0, 255, 255), small)
    y += 35

    for i, row in enumerate(rows):
        date = str(row[3])[:19]
        line = f"{i + 1}. {row[0]}   {row[1]}   {row[2]}   {date}"
        text(line, 50, y, (255, 255, 255), small)
        y += 30

    back = button(200, 520, 200, 50, "Back")
    return back


def draw_settings():
    screen.fill((0, 0, 0))
    text("SETTINGS", 230, 70, (255, 255, 0))

    grid = button(180, 160, 240, 45, "Grid: " + str(settings["grid"]))
    sound = button(180, 225, 240, 45, "Sound: " + str(settings["sound"]))

    color_text = str(settings["color"])
    color = button(180, 290, 240, 45, "Color: " + color_text)

    save = button(180, 400, 240, 50, "Save & Back")

    text("Color changes: green -> blue -> red", 145, 360, (180, 180, 180), small)

    return grid, sound, color, save


def draw_game_over():
    screen.fill((0, 0, 0))
    text("GAME OVER", 220, 100, (255, 0, 0))

    text("Score: " + str(game.score), 220, 180)
    text("Level: " + str(game.level), 220, 220)
    text("Personal best: " + str(max(best, game.score)), 180, 260)

    retry = button(190, 360, 220, 50, "Retry")
    menu = button(190, 430, 220, 50, "Main Menu")

    return retry, menu


def start_game():
    global game, best, saved, state, username

    if username.strip() == "":
        username = "Player"

    best = get_best(username)
    game = SnakeGame(username, best)
    saved = False
    state = "game"


while running:
    clock.tick(60)

    buttons = None

    if state == "menu":
        buttons = draw_menu()
    elif state == "leaderboard":
        buttons = draw_leaderboard()
    elif state == "settings":
        buttons = draw_settings()
    elif state == "game_over":
        buttons = draw_game_over()
    elif state == "game":
        game.update()
        game.draw(screen, small)

        if game.game_over:
            if not saved:
                save_game(username, game.score, game.level)
                saved = True
            state = "game_over"

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if state == "menu":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif e.key == pygame.K_RETURN:
                    start_game()
                else:
                    username += e.unicode

            if e.type == pygame.MOUSEBUTTONDOWN and buttons:
                play, lead, sett, quitb = buttons

                if play.collidepoint(e.pos):
                    start_game()
                elif lead.collidepoint(e.pos):
                    state = "leaderboard"
                elif sett.collidepoint(e.pos):
                    state = "settings"
                elif quitb.collidepoint(e.pos):
                    running = False

        elif state == "leaderboard":
            if e.type == pygame.MOUSEBUTTONDOWN and buttons:
                if buttons.collidepoint(e.pos):
                    state = "menu"

        elif state == "settings":
            if e.type == pygame.MOUSEBUTTONDOWN and buttons:
                grid, sound, color, save = buttons

                if grid.collidepoint(e.pos):
                    settings["grid"] = not settings["grid"]

                elif sound.collidepoint(e.pos):
                    settings["sound"] = not settings["sound"]

                elif color.collidepoint(e.pos):
                    if settings["color"] == [0, 255, 0]:
                        settings["color"] = [0, 0, 255]
                    elif settings["color"] == [0, 0, 255]:
                        settings["color"] = [255, 0, 0]
                    else:
                        settings["color"] = [0, 255, 0]

                elif save.collidepoint(e.pos):
                    save_settings(settings)
                    state = "menu"

        elif state == "game":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.set_dir((0, -1))
                elif e.key == pygame.K_DOWN:
                    game.set_dir((0, 1))
                elif e.key == pygame.K_LEFT:
                    game.set_dir((-1, 0))
                elif e.key == pygame.K_RIGHT:
                    game.set_dir((1, 0))
                elif e.key == pygame.K_ESCAPE:
                    state = "menu"

        elif state == "game_over":
            if e.type == pygame.MOUSEBUTTONDOWN and buttons:
                retry, menu = buttons

                if retry.collidepoint(e.pos):
                    start_game()
                elif menu.collidepoint(e.pos):
                    state = "menu"

    pygame.display.flip()

pygame.quit()