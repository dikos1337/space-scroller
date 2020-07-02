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
        # Создаю полотно и определяю его размер в зависимости от текущего здоровья
        healthpoints_surface = pygame.Surface((Config.SPRITE_HEALTHPOINTS_SIZE[0] // 2
                                               + Config.SPRITE_HEALTHPOINTS_SIZE[0] * player_hp,
                                               Config.SPRITE_HEALTHPOINTS_SIZE[1]))
        healthpoints_surface.set_colorkey((0, 0, 0))  # Делаю фон прозрачным
        healthpoints_rect = healthpoints_surface.get_rect()

        healthpoints = pygame.sprite.Group()

        # Создаю сердечки
        for x in range(start_x, Config.SPRITE_HEALTHPOINTS_SIZE[0] * player_hp, Config.SPRITE_HEALTHPOINTS_SIZE[0]):
            healthpoints.add(SpriteHealthPoints(x))

        # Рисую сердечки
        for hp in healthpoints:
            healthpoints_surface.blit(hp.image, hp.rect)

        return healthpoints_surface, healthpoints_rect
