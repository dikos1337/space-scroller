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
        all_sprites = [file_name for file_name in os.listdir(Config.img_folder) if 'meteorite' in file_name]
        random_sprite = random.choice(all_sprites)
        random_size = random.choice([size for size in range(50,101,10)])

        image = pygame.image.load(os.path.join(Config.img_folder, random_sprite))
        image = pygame.transform.scale(image, (random_size, random_size))
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(0, Config.WIDTH), random.randint(-1000, 0)))


class SpriteBackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'background.jpg'))
        player_img = pygame.transform.scale(player_img, (Config.WIDTH, Config.HEIGHT))
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect(center=(Config.WIDTH / 2, Config.HEIGHT / 2))
