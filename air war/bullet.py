import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями выпущенными кораблем"""
    def __init__(self, ai_settings, screen, gun):
        """создает обьект пули в текущей позиции корабля."""
        super().__init__()
        self.screen = screen
        # загрузка изображения снаряда
        self.image = pygame.image.load('images/bulet.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # создание пули в позиции(0,0) и назначение правильной позиции.
        # self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        #                        ai_settings.bullet_height)
        self.rect.right = gun.rect.right
        self.rect.center = gun.rect.center

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
        self.screen.blit(self.image, self.rect)
