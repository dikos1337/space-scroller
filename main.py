import random

import pygame

from sprites import SpriteBackGround
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from interface import Interface


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config.TITLE)

        self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = SpriteBackGround()
        self.player = PlayerSpaceship()
        self.lasers = pygame.sprite.Group()

        # Спавню и конфигурирую метеориты
        self.meteorites = pygame.sprite.Group()
        for _ in range(Config.total_meteorites):
            self.meteorites.add(Meteorite())

        for meteorite in self.meteorites:
            meteorite.speed = random.choice(range(1, 3))
            meteorite.spread = random.choice(range(-3, 4))

        self.main_loop()  # Запускаю main loop

    def check_collisions(self):
        """Обработка столкновений корабля с метеоритами"""
        # TODO добавить еще обработку выстрелов с метеоритами
        collide = pygame.sprite.spritecollide(self.player, self.meteorites, True)
        if collide:
            self.player.health -= 1
        print(self.player.health, collide)

    def check_health_points(self):
        """Проверка запаса здоровья корабля"""
        if self.player.health <= 0:
            print('Корабль разрушен')
            pygame.quit()
            exit()

    def check_attack(self):
        """Проверка атаки"""
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.lasers.add(self.player.shoot())

    def ckeck_events(self):
        """Обработка игровых событий"""
        # Проверяю выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.player.move()  # Проверяю движения игрока
        self.check_collisions()  # Проверяю столкновения метеоритов с кораблем
        self.check_health_points()  # Проверяю здоровье корабля
        self.check_attack()  # Проверяю атаку

    def draw(self):
        """То, что отрисовывается каждый кадр"""
        self.main_window.blit(self.background.image, self.background.rect)  # Заливаю фон

        # Отрисовываю метеориты
        for meteorite in self.meteorites:
            self.main_window.blit(meteorite.image, meteorite.rect)
            meteorite.fall()

        for laser in self.lasers:
            self.main_window.blit(laser.image, laser.rect)
            laser.update()

        self.main_window.blit(self.player.image, self.player.rect)  # Отрисовываю игрока

        # Вывожу на экран очки здоровья
        Interface.health_points(self,
                                surface=self.main_window,
                                start_x=int(Config.SpriteHealthPoints_size[0] / 2),
                                player_hp=self.player.health)

    def tick(self):
        """То что происходит каждый кадр"""
        # Обработка событий
        self.ckeck_events()

        # Отрисовка кадра
        self.draw()

    def scores(self):
        """Считаю игровые очки"""
        pass

    def main_loop(self):
        while True:
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
