import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями выпущенными кораблем"""
    def __init__(self, ai_settings, screen, gun):
        """создает обьект пули в текущей позиции корабля."""
        super().__init__()
        self.screen = screen

        # создание пули в позиции(0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top

        # позиция пули храниться в вещественном формате
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

    def update(self):
        """перемещает пулю вправо по экрану"""
        self.x += self.speed_factor
        # обновление прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        """вывод пули на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)