import random
import os

import pygame

from config import Config


class SpritePlayerSpaceship(pygame.sprite.Sprite):
    """Спрайт корабля игрока"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'spaceship.png'))
        player_img = pygame.transform.scale(player_img, (120, 120))
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect(center=(Config.SpritePlayerSpaceship_init_x,
                                                Config.SpritePlayerSpaceship_init_y))
        self.radius = int(self.rect.width / 2)


class SpriteMeteorite(pygame.sprite.Sprite):
    """Спрайты метеоритов"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        all_sprites = [file_name for file_name in os.listdir(Config.img_folder) if 'meteorite' in file_name]
        random_sprite = random.choice(all_sprites)
        random_size = random.randrange(50, 101)

        image = pygame.image.load(os.path.join(Config.img_folder, random_sprite))
        image = pygame.transform.scale(image, (random_size, random_size))  # Задаю случайный размер
        image = pygame.transform.rotate(image, random.randrange(360))  # Задаю случайный поворот
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(0, Config.WIDTH), random.randint(-Config.HEIGHT, 0)))
        self.radius = int(self.rect.width * 0.6 / 2)


class SpriteBackGround(pygame.sprite.Sprite):
    """background sprite"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'background.jpg'))
        player_img = pygame.transform.scale(player_img, (Config.WIDTH, Config.HEIGHT))
        self.image = player_img.convert()
        self.rect = self.image.get_rect()


class SpriteLaser(pygame.sprite.Sprite):
    """Спрайт лазера для атаки корабля"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        laser_img = pygame.image.load(os.path.join(Config.img_folder, 'laser.png'))
        laser_img = pygame.transform.scale(laser_img, (20, 30))
        self.image = laser_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


class SpriteHealthPoints(pygame.sprite.Sprite):
    """Спрайт для очков здоровья"""
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(os.path.join(Config.img_folder, 'hp.png'))
        player_img = pygame.transform.scale(player_img, (Config.SpriteHealthPoints_size[0],
                                                         Config.SpriteHealthPoints_size[1]))
        self.image = player_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
