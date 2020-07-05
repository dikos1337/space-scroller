from functools import lru_cache

import pygame

from config import Config
from sprites import SpriteHealthPoints, SpriteStartMenu


class Gui:
    """Класс с пользовательским интерфейсом"""

    @staticmethod
    def start_menu(main_surface, background, state):
        """Стартовое меню игры"""
        menu_sprite = SpriteStartMenu()
        main_surface.blit(background.image, background.rect)
        start_menu = pygame.Surface((Config.WIDTH // 2, Config.HEIGHT // 2))
        start_menu.set_colorkey((181, 230, 29))  # Делаю прозрачный фон, тут зеленый цвет
        start_menu.blit(menu_sprite.image, menu_sprite.rect)
        main_surface.blit(start_menu, start_menu.get_rect().center)  # Отрисовываю по центру
        pressed = pygame.mouse.get_pressed()  # Информация о нажатиях кнопок мышки
        pos = pygame.mouse.get_pos()  # Информация о координатах мышки

        # Проверка кнопки Start Game
        start_game_button = ((360, 230), (830, 298))  # Координаты верхнего левого и правого нижнего угла кнопки
        if pressed[0] or pygame.key.get_pressed()[pygame.K_SPACE]:  # На пробел игра тоже стартует
            if ((start_game_button[0][0] < pos[0] < start_game_button[1][0]) and (
                    start_game_button[0][1] < pos[1] < start_game_button[1][1])):
                return "PLAY"
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                return "PLAY"

        # Проверка кнопки Exit
        exit_game_button = ((360, 525), (830, 593))  # Координаты верхнего левого и правого нижнего угла кнопки
        if pressed[0]:
            if ((exit_game_button[0][0] < pos[0] < exit_game_button[1][0]) and (
                    exit_game_button[0][1] < pos[1] < exit_game_button[1][1])):
                pygame.quit()
                quit()

        pygame.display.update()
        return state

    def pause(self):
        """Меню паузы"""
        pass

    def settings(self):
        """Меню настроек"""
        pass

    @staticmethod
    @lru_cache(maxsize=1)
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
    @lru_cache(maxsize=5)
    def health_points(start_x, player_hp):
        """Отображения здоровье игрока"""
        # Создаю полотно и определяю его размер в зависимости от текущего здоровья
        healthpoints_surface = pygame.Surface((Config.SPRITE_HEALTH_POINTS_SIZE[0] // 2
                                               + Config.SPRITE_HEALTH_POINTS_SIZE[0] * player_hp,
                                               Config.SPRITE_HEALTH_POINTS_SIZE[1]))

        healthpoints_surface.set_colorkey((0, 0, 0))  # Делаю фон прозрачным
        healthpoints_surface_rect = healthpoints_surface.get_rect()

        # Создаю и рисую сердечки
        for x in range(start_x, Config.SPRITE_HEALTH_POINTS_SIZE[0] * player_hp, Config.SPRITE_HEALTH_POINTS_SIZE[0]):
            hp = SpriteHealthPoints(x)
            healthpoints_surface.blit(hp.image, hp.rect)

        return healthpoints_surface, healthpoints_surface_rect
