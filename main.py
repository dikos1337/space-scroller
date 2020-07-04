import pygame

from events import Events
from sprites import SpriteBackGround
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from gui import Gui
from sounds import Sounds
from states import States


class Game:
    background_sound_is_playing = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config.TITLE)

        self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
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

        self.events = Events(self.player, self.meteorites, self.lasers,
                             self.powerups, self.all_sprites, self.states)
        self.main_loop()  # Запускаю main loop

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
        text_surface, text_rect = Gui.scores(text='Score: ' + str(self.events.score), text_size=25, x=0,
                                             y=Config.SPRITE_HEALTH_POINTS_SIZE[1] + 15)
        self.main_window.blit(text_surface, text_rect)

    def tick(self):
        """То что происходит каждый кадр"""

        # NOTE: Не менять порядок вызовов draw и check_events
        self.draw()  # Отрисовка кадра
        self.events.ckeck_events()  # Обработка событий

    def main_loop(self):
        # Фоновая музыка
        if self.background_sound_is_playing:
            pass
        else:
            self.background_sound_is_playing = True
            Sounds.background_sound.play(loops=-1)

        while True:
            # Задержка
            self.clock.tick(Config.FPS)

            if self.states.current_state == "RESTART":
                self.__init__()

            if self.states.current_state == "START_MENU":
                self.events.ckeck_events()
                self.states.current_state = Gui.start_menu(self.main_window, self.background, self.states.current_state)

            elif self.states.current_state == "PLAY":
                # Цикл обработки событий
                self.events.ckeck_events()

                # Изменение объектов и многое др.
                self.tick()

                # Обновление экрана
                pygame.display.update()


if __name__ == '__main__':
    Game()
