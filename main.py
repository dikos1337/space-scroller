import pygame
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from sprites import SpriteBackGround


def main():
    pygame.init()
    main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(Config.TITLE)
    clock = pygame.time.Clock()

    background = SpriteBackGround()
    player = PlayerSpaceship()
    meteors = [Meteorite() for _ in range(Config.total_meteorites)]
    while True:
        # задержка
        clock.tick(Config.FPS)

        # цикл обработки событий
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        # --------
        # изменение объектов и многое др.
        # --------

        main_window.blit(background.image, background.rect)  # fill background
        main_window.blit(player.image, player.rect)
        player.move()
        for meteor in meteors:
            main_window.blit(meteor.image, meteor.rect)
            meteor.fall()
        # обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()
