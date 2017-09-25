import pygame

class Gun():

    def __init__(self, ai_settings, screen):
        """инициализация самолета, задание его начальной позиции"""
        self.screen = screen
        self.ai_settings = ai_settings

        #загрузка изображения самолета
        self.image = pygame.image.load('images/gun.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # каждый новый  самолет появляется в центре
        self.rect.centerx = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        # сохранение вещественной координаты центра самолета
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)
        # флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """обновляет позицию самолета с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.ai_settings.gun_speed

        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.ai_settings.gun_speed

        if self.moving_up and self.rect.top > 0:
            self.centerY -= self.ai_settings.gun_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_settings.gun_speed

        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY

    def blitme(self):
        """рисует самолет в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_left(self):
        """Размещает самолет в центре левого края экрана."""
        self.centerX = self.screen_rect.left
        self.centerY = self.screen_rect.centery
