import pygame
from settings import Settings
from gun import Gun
import game_func as gf
from pygame.sprite import Group
from statistic import Statistic
from button import Button

def run_game():
    # иницаилизация pygame и создание обьекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    # создание кнопки  Play.
    play_button = Button(ai_settings, screen, "Play")

    # созадние экземпляра для хранения игровой статистики.
    stats = Statistic(ai_settings)

    # создание gun
    gun = Gun(ai_settings, screen)

    # создание Ufo
    ufos = Group()

    # создание пуль
    bullets = Group()

    gf.create_fleet(ai_settings, screen, gun, ufos)

    # запуск основного цикла
    while True:
        # отслеживание событий с клавиатуры
        gf.check_events(ai_settings, screen, stats,
                        play_button, gun, ufos, bullets)
        if stats.game_active:
            gun.update()
            gf.update_bullets(ai_settings, screen, gun, ufos, bullets)
            gf.update_ufos(ai_settings, stats, screen, gun, ufos, bullets)
            gf.update_screen(ai_settings, screen, stats,
                             gun, ufos, bullets, play_button)

run_game()
