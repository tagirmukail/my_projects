class Settings():
    """Статические настройки игры"""

    def __init__(self):
        # парамтры экрана
        self.caption = "Guns_run"
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (20, 100, 190)
        # настройки самолета
        self.gun_speed = 1.3
        self.limit_guns = 2
        # праметры снарядов
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        # настройки пришельцев
        self.ufo_speed_factor = 0.7
        self.fleet_drop_speed = 10
        # Темп ускорения игры.
        self.speedup = 1.1
        self.dynamic_settings()
        # fleet_direction = 1 обозначает движение вверх; а -1 вниз
        self.fleet_direction = 1

    def dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.gun_speed = 1.5
        self.bullet_speed = 2
        self.ufo_speed_factor = 1

        # движение в право или в лево.
        self.fleet_direction = 1

    def up_speed(self):
        """Увеличение скорости."""
        self.gun_speed += self.speedup
        self.bullet_speed += self.speedup
        self.ufo_speed_factor += self.speedup
