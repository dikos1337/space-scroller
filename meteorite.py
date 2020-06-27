import random

from sprites import SpriteMeteorite
from config import Config


class Meteorite(SpriteMeteorite):
    radius = 80  # FIXME: Надо или удалить или брать из конфига

    def update(self):
        """Логика падения метеорита"""
        self.rect.y += self.speed
        self.rect.x += self.spread

        # Обработка случаев если метеорит улетел за пределы окна
        if self.rect.y > Config.HEIGHT:
            self.rect.y = 0
        if self.rect.x > Config.WIDTH + (self.radius * 2) or self.rect.x < -(self.radius * 2):
            self.rect.x = random.randint(0, Config.HEIGHT)
            self.rect.y = random.randint(-Config.WIDTH, -300)
