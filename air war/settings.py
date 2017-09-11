class Settings():
    """настройки игры"""

    def __init__(self):
        # парамтры экрана
        self.caption = "Guns_run"
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (20, 100, 190)
        # настройки ракеты
        self.gun_speed = 1.3
        # праметры пули
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3