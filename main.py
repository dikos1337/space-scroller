import pygame
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from sprites import SpriteBackGround


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config.TITLE)

        self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = SpriteBackGround()
        self.player = PlayerSpaceship()
        self.meteorites = [Meteorite() for _ in range(Config.total_meteorites)]

        self.main_loop()  # Запускаю main loop

    def ckeck_events(self):
        """Обработка игровых событий"""

        self.player.move()  # Проверяю движения игрока

        # Проверяю выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw(self):
        """То, что отрисовывается каждый кадр"""

        self.main_window.blit(self.background.image, self.background.rect)  # Заливаю фон
        self.main_window.blit(self.player.image, self.player.rect)  # Отрисовываю игрока

        # Отрисовываю метеориты
        for meteorite in self.meteorites:
            self.main_window.blit(meteorite.image, meteorite.rect)
            meteorite.fall()

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
