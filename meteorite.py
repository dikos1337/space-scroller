import random
from sprites import SpriteMeteorite
from config import Config


class Meteorite(SpriteMeteorite):
    speed = random.choice([1, 5, 10, 15, 20])
    radius = 80
    spread = 5

    def fall(self):
        """Логика падения метеорита"""
        self.rect.y += self.speed
        self.rect.x += random.randint(-self.spread, self.spread)
        self.speed = random.choice([1, 5, 10])

        # Обработка случаев если метеорит улетел за пределы окна
        if self.rect.y > Config.HEIGHT:
            self.rect.y = 0
        if self.rect.x > Config.WIDTH + (self.radius * 2) or self.rect.x < -(self.radius * 2):
            self.rect.x = random.randint(0, Config.HEIGHT)
            self.rect.y = random.randint(-Config.WIDTH, -300)
