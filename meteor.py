import pygame
import numpy as np
from sprites import SpriteMeteorite
from config import Config

class Meteorite(SpriteMeteorite):
    speed = np.random.choice([1,5,10])
    radius = 80
    def fall(self):
        self.rect.y += self.speed
        self.rect.x += np.random.randint(-3,3)
        self.speed = np.random.choice([1,5,10])
        if self.rect.y > Config.HEIGHT:
            self.rect.y = 0
        if self.rect.x > Config.WIDTH + (self.radius * 2) or self.rect.x < self.radius:
            self.rect.x = np.random.randint(0,Config.HEIGHT)
            self.rect.y = np.random.randint(-Config.WIDTH,-300)