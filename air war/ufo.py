import pygame
from pygame.sprite import Sprite

class Ufo(Sprite):
    """класс, представляющий одного пришельца."""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в верхнем правом углу.
        self.rect.x = ai_settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца.
        self.y = float(self.rect.y)

    def blitme(self):
        """ Вывод пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)
