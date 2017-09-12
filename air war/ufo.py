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

    def check_edges(self):
        """Возвращвет True, если пришелец достиг края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.centery <= screen_rect.top:
            return True
        elif self.rect.centery >= screen_rect.bottom:
            return True

    def update(self):
        """Перемещает пришельца вверх и вниз"""
        self.y += (self.ai_settings.ufo_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y