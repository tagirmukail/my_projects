import sys

import pygame
from bullet import Bullet
from gun import Gun

def check_keydown_events(event, ai_settings, screen, gun, bullets):
    """реагирует на нажатия клавиш"""
    if event.key == pygame.K_RIGHT:
        # переместить gun вправо
        gun.moving_right = True
    elif event.key == pygame.K_LEFT:
        # переместить влево
        gun.moving_left = True
    elif event.key == pygame.K_UP:
        # переместить вверх
        gun.moving_up = True
    elif event.key == pygame.K_DOWN:
        # переместить вниз
        gun.moving_down = True
    elif event.key == pygame.K_SPACE:
        # создание новой пули и вкючение ее в группу bullets.
        fire_bullet(ai_settings, screen, gun, bullets)

def check_keyup_events(event, gun):
    """Реагирует на отпускания клавиш"""
    if event.key == pygame.K_RIGHT:
        gun.moving_right = False
    if event.key == pygame.K_LEFT:
        gun.moving_left = False
    if event.key == pygame.K_UP:
        gun.moving_up = False
    if event.key == pygame.K_DOWN:
        gun.moving_down = False

def check_events(ai_settings, screen, gun, bullets):
    """обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, gun,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, gun)

def update_screen(ai_settings, screen, gun, bullets):
    """обновляет изображение на экране и отображает новый экран"""
    # при каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # все пули выводят выходят позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.blitme()
    # отображение последнего прорисованного экрана
    pygame.display.flip()

def update_bullets(bullets):
    """обновление позиции пуль и уничтожает старые пули"""
    bullets.update()

    # Удаление пуль, вышедших за экран
    for bullet in bullets.copy():
        if bullet.rect.left >= 800:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, gun, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, gun)
        bullets.add(new_bullet)