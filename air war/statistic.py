class Statistic():
    """Отслеживание статистики"""

    def __init__(self, ai_settings):
        """Инициализация статистики"""
        self.ai_settings = ai_settings
        self.status_reset()
        # запуск игры в активном состоянии.
        self.game_active = False

    def status_reset(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.gun_limit_life = self.ai_settings.limit_guns