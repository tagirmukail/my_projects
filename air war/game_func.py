import sys

import pygame
from bullet import Bullet
from gun import Gun
from ufo import Ufo

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
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

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

def update_screen(ai_settings, screen, gun, ufos, bullets):
    """обновляет изображение на экране и отображает новый экран"""
    # при каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # все пули выводят выходят позади изображений корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.blitme()
    ufos.draw(screen)
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

def get_number_ufo_y(ai_settings, ufo_height):
    """вычисляет количество пришельцев в ряду"""
    available_space_y = ai_settings.screen_height - 2 * ufo_height
    number_ufo_y = int(available_space_y / (2 + ufo_height))
    return number_ufo_y

def create_ufo(ai_settings, screen, ufos, ufo_number, row_number):
    """создает пришельца и размещает его в ряду"""
    ufo = Ufo(ai_settings, screen)
    ufo_height = ufo.rect.height
    ufo.y = 2 * ufo_height * ufo_number
    ufo.rect.y = ufo.y
    ufo.rect.x =ai_settings.screen_width - (ufo.rect.width + 2 * ufo.rect.width * row_number)
    ufos.add(ufo)

def create_fleet(ai_settings, screen, gun, ufos):
    """создает флот пришельцев."""
    # создание пришельца и вычисление количества пришельцев в ряду
    ufo = Ufo(ai_settings, screen)
    number_ufo_y = get_number_ufo_y(ai_settings, ufo.rect.height)
    number_rows = get_number_rows(ai_settings, gun.rect.width, ufo.rect.width)

    # создание флота пришельцев
    for row_number in range(number_rows):
        for ufo_number in range(number_ufo_y):
            create_ufo(ai_settings, screen, ufos, ufo_number, row_number)

def get_number_rows(ai_settings, gun_width, ufo_width):
    """определяет количество рядов, помещающихся на экране."""
    available_space_x = (ai_settings.screen_width - (3 * ufo_width) - gun_width)
    number_rows = int(available_space_x / (2 * ufo_width))
    return number_rows