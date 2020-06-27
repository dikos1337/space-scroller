import random

from sprites import SpriteMeteorite
from config import Config


class Meteorite(SpriteMeteorite):
    def __init__(self):
        SpriteMeteorite.__init__(self)
        self.speed = random.randrange(1, 6)
        self.spread = random.randrange(-3, 4)

    def update(self):
        """Логика падения метеорита"""
        self.rect.y += self.speed
        self.rect.x += self.spread

        # Обработка случаев если метеорит улетел за пределы окна, потом он сам заспавнится заного
        if self.rect.y > Config.HEIGHT:
            self.kill()
        if self.rect.x > (Config.WIDTH + (self.radius * 2)) or self.rect.x < -(self.radius * 2):
            self.kill()
