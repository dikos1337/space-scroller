import pygame

from sprites import SpriteHealthPoints
from config import Config

class Interface:
    """Класс с пользовательским интерфейсом"""
    def main_menu(self):
        """Основное меню"""
        pass

    def pause(self):
        """Меню паузы"""
        pass

    def settings(self):
        """Меню настроек"""
        pass

    def leaderboard(self):
        """Рейтинг по набраным за игру очкам"""
        pass

    def health_points(self,surface,start_x,player_hp):
        healthpoints = pygame.sprite.Group()
        for x in range(start_x,
                       start_x + Config.SpriteHealthPoints_size[0] * player_hp,
                       Config.SpriteHealthPoints_size[0]):
            healthpoints.add(SpriteHealthPoints(x))

        for hp in healthpoints:
            surface.blit(hp.image, hp.rect)

# pygame.init()
# clock = pygame.time.Clock()
# FPS = 30
# BLACK = (0, 0, 0)
# screen = pygame.display.set_mode((500, 500))
# running = True
# healthpoints = pygame.sprite.Group()
#
# start_x = 30
# player_hp = 5
# for x in range(start_x,start_x + 60*player_hp,60):
#     healthpoints.add(SpriteHealthPoints(x))
# #    [SpriteHealthPoints(x+60) for x in range(0,60*5,60)]
# while running:
#     # Держим цикл на правильной скорости
#     clock.tick(FPS)
#     # Ввод процесса (события)
#     for event in pygame.event.get():
#         # check for closing window
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Обновление
#
#
#
#     # Рендеринг
#     screen.fill(BLACK)
#     for hp in healthpoints:
#         screen.blit(hp.image, hp.rect)
#     # После отрисовки всего, переворачиваем экран
#     pygame.display.update()
#
# pygame.quit()