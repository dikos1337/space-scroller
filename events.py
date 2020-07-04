import random

import pygame

from buffs import BuffWeaponUpgrade, BuffHealthRecovery
from config import Config
from meteorite import Meteorite
from sounds import Sounds


class Events:
    def __init__(self, player, meteorites, lasers, powerups, all_sprites, states):
        self.player = player
        self.meteorites = meteorites
        self.all_sprites = all_sprites
        self.lasers = lasers
        self.powerups = powerups
        self.score = 0
        self.states = states

    @staticmethod
    def event_quit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def check_meteorites(self):
        if len(self.meteorites) < Config.TOTAL_METEORITES:
            tmp_meteorite = Meteorite()
            self.meteorites.add(tmp_meteorite)
            self.all_sprites.add(tmp_meteorite)

    def check_collisions(self):
        """Обработка столкновений корабля с метеоритами"""
        # Проверяю корабль и метеориты
        collide = pygame.sprite.spritecollide(self.player, self.meteorites, True, pygame.sprite.collide_circle)
        if collide:
            self.player.health -= 1
            Sounds.hurt_sound.play()

        # Проверяю лазеры и метеориты
        laser_hits = pygame.sprite.groupcollide(self.meteorites, self.lasers, True, True, pygame.sprite.collide_circle)

        # Если лазер попадает в метеорит, то начисляю очки
        for hit in laser_hits:
            self.score += 50 - hit.radius  # Тут радиус метеорита, у лазера нет свойтва радиус.
            Sounds.explosion_sound.play()

            # C некоторой вероятностью из метеорита упадет баф
            if random.random() < Config.BUFF_PROC_CHANCE:
                random_buff = random.choice([BuffHealthRecovery(hit.rect.center), BuffWeaponUpgrade(hit.rect.center)])
                self.powerups.add(random_buff)
                self.all_sprites.add(random_buff)

        # Проверяю бафы
        if len(self.powerups) > 0:
            powerups_hits = pygame.sprite.spritecollide(self.player, self.powerups, True, pygame.sprite.collide_circle)
            for buff in powerups_hits:
                if type(buff) == BuffHealthRecovery:
                    if self.player.health < self.player.MAX_HEALTH:
                        self.player.health += 1

                if type(buff) == BuffWeaponUpgrade:
                    if self.player.spaceship_attack_speed > self.player.SPACESHIP_ATTACK_SPEED_LIMIT:
                        self.player.spaceship_attack_speed = int(self.player.spaceship_attack_speed
                                                                 / Config.BUFF_ATTACK_SPEED_UPG_RATE)
                        pygame.time.set_timer(self.player.SPACESHIP_ATTACK_EVENT, self.player.spaceship_attack_speed)

    def check_health_points(self):
        """Проверка запаса здоровья корабля"""
        if self.player.health < 1:
            print('Корабль разрушен')
            print('Набранные очки:', self.score)
            self.states.restart()

    def event_attack(self, event):
        """Проверка атаки"""
        if event.type == self.player.SPACESHIP_ATTACK_EVENT:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                laser = self.player.shoot()
                self.lasers.add(laser)
                self.all_sprites.add(laser)
                Sounds.shoot_sound.play()

    def ckeck_events(self):
        """Обработка игровых событий"""
        for event in pygame.event.get():
            # Проверяю выход из игры
            self.event_quit(event)

            # Проверяю и ограничиваю скорость атаки
            self.event_attack(event)

        self.player.move()  # Проверяю движения игрока
        self.check_meteorites()  # Проверяю кол-во метеоритов
        self.check_collisions()  # Проверяю столкновения метеоритов с кораблем
        self.check_health_points()  # Проверяю здоровье корабля
