import pygame

from sprites import SpritePlayerSpaceship, SpriteLaser


class PlayerSpaceship(SpritePlayerSpaceship):
    SPACESHIP_ATTACK_EVENT = pygame.USEREVENT + 1
    SPACESHIP_ATTACKSPEED = 500  # 2 attacks per second (1000/500=2)
    MOVESPEED = 5  # pixels per frame
    MAX_HEALTH = 5
    health = MAX_HEALTH  # Здоровье корабля

    pygame.time.set_timer(SPACESHIP_ATTACK_EVENT, SPACESHIP_ATTACKSPEED)

    def move(self):
        """Управление кораблем"""
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += self.MOVESPEED
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= self.MOVESPEED
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= self.MOVESPEED
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += self.MOVESPEED

    def shoot(self):
        """Функционал стрельбы из корабля"""
        laser = SpriteLaser(self.rect.centerx, self.rect.top)
        return laser
