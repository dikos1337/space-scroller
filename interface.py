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

    @staticmethod
    def scores(text, text_size, x, y):
        """Считаю игровые очки"""
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, text_size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midleft = (x, y)
        return text_surface, text_rect

    def leaderboard(self):
        """Рейтинг по набраным за игру очкам"""
        pass

    @staticmethod
    def health_points(start_x, player_hp):
        """Отображения здоровье игрока"""
        healthpoints_surface = pygame.Surface((Config.SPRITE_HEALTHPOINTS_SIZE[0] // 2
                                               + Config.SPRITE_HEALTHPOINTS_SIZE[0] * player_hp,
                                               Config.SPRITE_HEALTHPOINTS_SIZE[1]))
        healthpoints_surface.set_colorkey((0, 0, 0))
        healthpoints = pygame.sprite.Group()

        for x in range(start_x, Config.SPRITE_HEALTHPOINTS_SIZE[0] * player_hp, Config.SPRITE_HEALTHPOINTS_SIZE[0]):
            healthpoints.add(SpriteHealthPoints(x))

        for hp in healthpoints:
            healthpoints_surface.blit(hp.image, hp.rect)

        return healthpoints_surface

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

#     # Рендеринг
#     screen.fill(BLACK)
#     for hp in healthpoints:
#         screen.blit(hp.image, hp.rect)
#     # После отрисовки всего, переворачиваем экран
#     pygame.display.update()
#
# pygame.quit()
