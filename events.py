import random
from datetime import datetime

import pygame

from buffs import BuffWeaponUpgrade, BuffHealthRecovery
from config import Config
from database import Database
from meteorite import Meteorite
from sounds import Sounds


class Events:
    def __init__(self, player, meteorites, lasers, powerups, all_sprites, states):
        self.player = player
        self.meteorites = meteorites
        self.all_sprites = all_sprites
        self.lasers = lasers
        self.powerups = powerups
        self.states = states
        self.db = Database()
        self.stats = {
            "start_time": datetime.now(),
            "score": 0,
            "sessoin_time": 0,
            "meteorite_hits": 0,
        }

    def event_quit(self, event):
        if event.type == pygame.QUIT:
            self.db.close_connection()
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
            self.stats['score'] += 50 - hit.radius  # Тут радиус метеорита, у лазера нет свойтва радиус.
            self.stats['meteorite_hits'] += 1
            Sounds.explosion_sound.play()

            # C некоторой вероятностью из метеорита упадет баф
            if random.random() < Config.BUFF_PROC_CHANCE:
                random_buff = random.choice((BuffHealthRecovery(hit.rect.center), BuffWeaponUpgrade(hit.rect.center)))
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
            print('Набранные очки:', self.stats['score'])
            # Вычисляю время сессии
            self.stats['sesion_time'] = (datetime.now() - self.stats['start_time']).seconds

            # Костыль, чтоб успелось обрабаботься всё и в базу по 2 раза не писались очки
            pygame.time.wait(100)

            # Записываю очки в базу
            self.db.insert_scores(self.stats['start_time'], int(self.stats['score']),
                                  self.stats['sesion_time'], self.stats['meteorite_hits'])

            # Перезапускаю игру
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
