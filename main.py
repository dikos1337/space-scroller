import random

import pygame

from buffs import BuffHealthRecovery, BuffWeaponUpgrade
from sprites import SpriteBackGround
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from gui import Gui
from sounds import Sounds


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config.TITLE)

        self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = SpriteBackGround()
        self.player = PlayerSpaceship()
        self.score = 0

        # Группа для всех спрайтов, их я буду обновлять и отрисовывать
        self.all_sprites = pygame.sprite.Group()

        # Группы для проверки коллизий
        self.lasers = pygame.sprite.Group()  # Выстрелы из корабля (лазеры)
        self.powerups = pygame.sprite.Group()  # Бафы

        # Создаю метеориты
        self.meteorites = pygame.sprite.Group()
        for _ in range(Config.TOTAL_METEORITES):
            tmp_meteorite = Meteorite()
            self.meteorites.add(tmp_meteorite)
            self.all_sprites.add(tmp_meteorite)

        self.main_loop()  # Запускаю main loop

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
        if self.player.health <= 0:
            print('Корабль разрушен')
            print('Набранные очки:', self.score)
            pygame.quit()
            exit()

    def event_attack(self, event):
        """Проверка атаки"""
        if event.type == self.player.SPACESHIP_ATTACK_EVENT:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                laser = self.player.shoot()
                self.lasers.add(laser)
                self.all_sprites.add(laser)
                Sounds.shoot_sound.play()

    @staticmethod
    def event_quit(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    def draw(self):
        """То, что отрисовывается каждый кадр"""
        self.main_window.blit(self.background.image, self.background.rect)  # Заливаю фон

        # Отрисоваю метеориты, лазеры, бафы
        self.all_sprites.update()
        self.all_sprites.draw(self.main_window)

        self.main_window.blit(self.player.image, self.player.rect)  # Отрисовываю игрока

        # Вывожу на экран очки здоровья
        healthpoints_surface, healthpoints_rect = Gui.health_points(
            start_x=Config.SPRITE_HEALTH_POINTS_SIZE[0] // 2,
            player_hp=self.player.health)

        self.main_window.blit(healthpoints_surface, healthpoints_rect)

        # Вывожу счёт
        text_surface, text_rect = Gui.scores(text='Score: ' + str(self.score), text_size=25, x=0,
                                             y=Config.SPRITE_HEALTH_POINTS_SIZE[1] + 15)
        self.main_window.blit(text_surface, text_rect)
        # Gui.start_menu(self.main_window,self.background)

    def tick(self):
        """То что происходит каждый кадр"""
        # Обработка событий
        self.ckeck_events()

        # Отрисовка кадра
        self.draw()

    def main_loop(self):
        # Фоновая музыка
        Sounds.background_sound.play(loops=-1)
        STATE = "START_MENU"
        while True:
            if STATE == "START_MENU":
                STATE = Gui.start_menu(self.main_window, self.background, STATE)
                self.ckeck_events()
            elif STATE == "PLAY":
                # Задержка
                self.clock.tick(Config.FPS)

                # Цикл обработки событий
                self.ckeck_events()

                # Изменение объектов и многое др.
                self.tick()

                # Обновление экрана
                pygame.display.update()


if __name__ == '__main__':
    Game()
