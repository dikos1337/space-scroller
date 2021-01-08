from config import Config
from sprites import SpriteHealthRecovery, SpriteWeaponUpgrade


class BuffHealthRecovery(SpriteHealthRecovery):
    """Баф который востанавливает здоровье кораблю"""
    speedy = 5  # Скорость движения

    def update(self):
        """Обновление анимации падения бафа"""
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.top > Config.HEIGHT:
            self.kill()


class BuffWeaponUpgrade(SpriteWeaponUpgrade):
    """Баф который увеличивает скорость атаки корабля на 10%"""
    speedy = 5  # Скорость движения бафа

    def update(self):
        """Обновление анимации падения бафа"""
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.top > Config.HEIGHT:
            self.kill()
