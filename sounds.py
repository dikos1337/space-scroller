from os import path

import pygame

from config import Config


class Sounds:
    pygame.mixer.init()

    shoot_sound = pygame.mixer.Sound(path.join(Config.snd_folder, 'Laser_Shoot21.wav'))
    hurt_sound = pygame.mixer.Sound(path.join(Config.snd_folder, 'Hit_Hurt22.wav'))
    explosion_sound = pygame.mixer.Sound(path.join(Config.snd_folder, 'Explosion51.wav'))
    background_sound = pygame.mixer.Sound(path.join(Config.snd_folder, 'through_space.ogg'))

    shoot_sound.set_volume(0.2)
    hurt_sound.set_volume(0.3)
    explosion_sound.set_volume(0.1)
    background_sound.set_volume(0.5)
