import pygame
import sys
from player import MusicPlayer

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Создаем объект плеера (укажи путь к своей папке с музыкой)
player = MusicPlayer("music")

def draw_text():
    screen.fill(WHITE)
    
    # Инструкции
    instr = [
        "P - Play/Unpause",
        "S - Stop",
        "N - Next Track",
        "B - Previous Track",
        "Q - Quit"
    ]
    
    for i, line in enumerate(instr):
        text = font.render(line, True, BLACK)
        screen.blit(text, (20, 20 + i * 30))
    
    # Текущий трек
    track_name = player.get_current_track_name()
    current_track_text = font.render(f"Now playing: {track_name}", True, (0, 100, 250))
    screen.blit(current_track_text, (20, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.pause() # В данном случае пауза удобнее стопа
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.key.key_code("b"): # Кнопка B (назад)
                player.prev_track()
            # Можно использовать и такой вариант для N и B:
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    draw_text()
    pygame.display.flip()

pygame.quit()
sys.exit()