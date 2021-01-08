import pygame

from config import Config
from events import Events
from gui import Gui
from meteorite import Meteorite
from player import PlayerSpaceship
from sounds import Sounds
from sprites import SpriteBackGround
from states import States


class Game:
    # background_sound_is_playing = False
    game_is_inited = False

    def __init__(self):
        if self.game_is_inited is False:
            pygame.init()
            pygame.display.set_caption(Config.TITLE)

            self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
            Sounds.background_sound.play(loops=-1)  # Фоновая музыка
            self.game_is_inited = True

        self.clock = pygame.time.Clock()
        self.background = SpriteBackGround()
        self.player = PlayerSpaceship()
        self.states = States()

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

        self.events = Events(self)
        self.main_loop()  # Запускаю main loop

    def draw(self):
        """То, что отрисовывается каждый кадр"""
        if self.states.current_state == "PLAY":
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
            text_surface, text_rect = Gui.scores(text='Score: ' + str(self.events.stats['score']), text_size=25, x=0,
                                                 y=Config.SPRITE_HEALTH_POINTS_SIZE[1] + 15)
            self.main_window.blit(text_surface, text_rect)

        if self.states.current_state == "START_MENU":
            self.main_window.blit(self.background.image, self.background.rect)  # Заливаю фон

            # Рисую стартовое меню
            start_menu, start_menu_rect = Gui.start_menu(self.states)
            self.main_window.blit(start_menu, start_menu_rect)

    def tick(self):
        """То что происходит каждый кадр"""

        # NOTE: Не менять порядок вызовов draw и check_events
        self.draw()  # Отрисовка кадра
        self.events.ckeck_events()  # Обработка событий

    def main_loop(self):
        # Фоновая музыка
        # if self.background_sound_is_playing:
        #     pass
        # else:
        #     self.background_sound_is_playing = True
        #     Sounds.background_sound.play(loops=-1)

        while True:
            if self.states.current_state == "RESTART":
                self.__init__()

            # Задержка
            self.clock.tick(Config.FPS)

            # Изменение объектов и многое др.
            self.events.ckeck_events()
            self.tick()

            # Обновление экрана
            pygame.display.update()


if __name__ == '__main__':
    app = Game()
