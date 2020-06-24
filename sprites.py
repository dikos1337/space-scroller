import pygame
from config import Config
import random
import os


class SpritePlayerSpaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'spaceship.png'))
        player_img = pygame.transform.scale(player_img, (160, 160))
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect(center=(Config.SpritePlayerSpaceship_init_x,
                                                Config.SpritePlayerSpaceship_init_y))

class SpriteMeteorite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(os.path.join(Config.img_folder, 'meteorite.png'))
        image = pygame.transform.scale(image, (100, 100))
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(0,Config.WIDTH),random.randint(-1000,0)))

class SpriteBackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'background.jpg'))
        player_img = pygame.transform.scale(player_img, (Config.WIDTH, Config.HEIGHT))
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect(center=(Config.WIDTH / 2,Config.HEIGHT / 2))
