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

        # for meteorite in self.meteorites:
        #     meteorite.speed = random.choice(range(1, 3))
        #     meteorite.spread = random.choice(range(-3, 4))

        self.main_loop()  # Запускаю main loop

    def check_meteorites(self):
        print(len(self.meteorites))
        if len(self.meteorites) < Config.total_meteorites:
            self.meteorites.add(Meteorite())
            # meteorites[-1].speed = random.choice(range(1, 3))
            # self.meteorites[-1].spread = random.choice(range(-3, 4))

    def check_collisions(self):
        """Обработка столкновений корабля с метеоритами"""
        # Проверяю корабль и метеориты
        collide = pygame.sprite.spritecollide(self.player, self.meteorites, True)
        if collide:
            self.player.health -= 1
        print(self.player.health, collide)

        # Проверяю лазеры и метеориты
        pygame.sprite.groupcollide(self.lasers, self.meteorites, True, True)

    def check_health_points(self):
        """Проверка запаса здоровья корабля"""
        if self.player.health <= 0:
            print('Корабль разрушен')
            pygame.quit()
            exit()

    def event_attack(self, event):
        """Проверка атаки"""
        if event.type == self.player.SPACESHIP_ATTACK:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.lasers.add(self.player.shoot())

    def event_quit(self, event):
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

        # Отрисовываю метеориты
        self.meteorites.update()
        self.meteorites.draw(self.main_window)

        # Отрисовываю лазеры
        self.lasers.update()
        self.lasers.draw(self.main_window)

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
