import pygame


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, (60, 60, 60), self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


def draw_text(screen, font, text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))