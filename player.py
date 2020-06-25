import pygame

from sprites import SpritePlayerSpaceship


class PlayerSpaceship(SpritePlayerSpaceship):
    movespeed = 10  # pixels per frame

    def move(self):
        """Управление кораблем"""
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.movespeed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.movespeed
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= self.movespeed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += self.movespeed

    def shoot(self):
        """Функционал стрельбы из корабля"""
        pass
