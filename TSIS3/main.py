import pygame
from racer import RacerGame, WIDTH, HEIGHT
from ui import Button, draw_text
from persistence import load_settings, save_settings, load_leaderboard, save_score


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS3 Racer")

font = pygame.font.SysFont("arial", 28)
small_font = pygame.font.SysFont("arial", 22)

settings = load_settings()
state = "name"
username = ""
game = None

play_btn = Button(170, 220, 160, 50, "Play")
leader_btn = Button(170, 290, 160, 50, "Leaderboard")
settings_btn = Button(170, 360, 160, 50, "Settings")
quit_btn = Button(170, 430, 160, 50, "Quit")

retry_btn = Button(160, 390, 180, 50, "Retry")
menu_btn = Button(160, 460, 180, 50, "Main Menu")
back_btn = Button(160, 600, 180, 50, "Back")

sound_btn = Button(150, 180, 200, 45, "Sound")
color_btn = Button(150, 250, 200, 45, "Car Color")
diff_btn = Button(150, 320, 200, 45, "Difficulty")

clock = pygame.time.Clock()
running = True


def start_game():
    global game, state
    game = RacerGame(username, settings)
    state = "game"


def draw_name_screen():
    screen.fill((25, 25, 25))
    draw_text(screen, font, "Enter username:", 130, 230)
    draw_text(screen, font, username, 180, 280, (255, 220, 0))
    draw_text(screen, small_font, "Press Enter to continue", 130, 340)


def draw_menu():
    screen.fill((30, 30, 30))
    draw_text(screen, font, "RACER GAME", 160, 130, (255, 220, 0))
    play_btn.draw(screen, font)
    leader_btn.draw(screen, font)
    settings_btn.draw(screen, font)
    quit_btn.draw(screen, font)


def draw_settings():
    screen.fill((30, 30, 30))
    draw_text(screen, font, "SETTINGS", 180, 100, (255, 220, 0))

    sound_btn.draw(screen, small_font)
    color_btn.draw(screen, small_font)
    diff_btn.draw(screen, small_font)
    back_btn.draw(screen, font)

    draw_text(screen, small_font, "Sound: " + str(settings["sound"]), 160, 230)
    draw_text(screen, small_font, "Color: " + settings["car_color"], 160, 300)
    draw_text(screen, small_font, "Difficulty: " + settings["difficulty"], 160, 370)


def draw_leaderboard():
    screen.fill((30, 30, 30))
    draw_text(screen, font, "TOP 10", 200, 60, (255, 220, 0))

    data = load_leaderboard()
    y = 120

    for i, item in enumerate(data):
        line = str(i + 1) + ". " + item["name"] + " | score: " + str(item["score"]) + " | dist: " + str(item["distance"])
        draw_text(screen, small_font, line, 50, y)
        y += 35

    back_btn.draw(screen, font)


def draw_game_over():
    screen.fill((30, 30, 30))

    if game.finished:
        draw_text(screen, font, "FINISH!", 200, 120, (0, 255, 0))
    else:
        draw_text(screen, font, "GAME OVER", 170, 120, (255, 0, 0))

    draw_text(screen, small_font, "Score: " + str(game.score), 180, 190)
    draw_text(screen, small_font, "Distance: " + str(int(game.distance)), 180, 230)
    draw_text(screen, small_font, "Coins: " + str(game.coins), 180, 270)

    retry_btn.draw(screen, font)
    menu_btn.draw(screen, font)


def handle_settings_click(pos):
    if sound_btn.clicked(pos):
        settings["sound"] = not settings["sound"]
        save_settings(settings)

    elif color_btn.clicked(pos):
        if settings["car_color"] == "red":
            settings["car_color"] = "blue"
        elif settings["car_color"] == "blue":
            settings["car_color"] = "green"
        else:
            settings["car_color"] = "red"
        save_settings(settings)

    elif diff_btn.clicked(pos):
        if settings["difficulty"] == "easy":
            settings["difficulty"] = "normal"
        elif settings["difficulty"] == "normal":
            settings["difficulty"] = "hard"
        else:
            settings["difficulty"] = "easy"
        save_settings(settings)


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "name":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username.strip() == "":
                        username = "Player"
                    state = "menu"

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    username += event.unicode

        elif state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.clicked(event.pos):
                    start_game()
                elif leader_btn.clicked(event.pos):
                    state = "leaderboard"
                elif settings_btn.clicked(event.pos):
                    state = "settings"
                elif quit_btn.clicked(event.pos):
                    running = False

        elif state == "settings":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.clicked(event.pos):
                    state = "menu"
                else:
                    handle_settings_click(event.pos)

        elif state == "leaderboard":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.clicked(event.pos):
                    state = "menu"

        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.player.move_right()
                elif event.key == pygame.K_ESCAPE:
                    state = "menu"

        elif state == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.clicked(event.pos):
                    start_game()
                elif menu_btn.clicked(event.pos):
                    state = "menu"

    if state == "name":
        draw_name_screen()

    elif state == "menu":
        draw_menu()

    elif state == "settings":
        draw_settings()

    elif state == "leaderboard":
        draw_leaderboard()

    elif state == "game":
        game.update()
        game.draw(screen, small_font)

        if game.game_over:
            save_score(username, game.score, int(game.distance), game.coins)
            state = "game_over"

    elif state == "game_over":
        draw_game_over()

    pygame.display.flip()

pygame.quit()