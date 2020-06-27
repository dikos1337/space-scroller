import pygame

from sprites import SpriteBackGround
from player import PlayerSpaceship
from meteorite import Meteorite
from config import Config
from interface import Interface
from sounds import Sounds

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Config.TITLE)

        self.main_window = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = SpriteBackGround()
        self.player = PlayerSpaceship()
        self.lasers = pygame.sprite.Group()
        self.score = 0

        # Создаю метеориты
        self.meteorites = pygame.sprite.Group()
        for _ in range(Config.total_meteorites):
            self.meteorites.add(Meteorite())

        self.main_loop()  # Запускаю main loop

    def check_meteorites(self):
        if len(self.meteorites) < Config.total_meteorites:
            self.meteorites.add(Meteorite())

    def check_collisions(self):
        """Обработка столкновений корабля с метеоритами"""
        # Проверяю корабль и метеориты
        collide = pygame.sprite.spritecollide(self.player, self.meteorites, True, pygame.sprite.collide_circle)
        if collide:
            self.player.health -= 1
            Sounds.hurt_sound.play()

        # Проверяю лазеры и метеориты
        laser_hits = pygame.sprite.groupcollide(self.meteorites, self.lasers, True, True)
        # Если лазер попадает в метеорит, то начисляю очки
        for hit in laser_hits:
            self.score += 50 - hit.radius  # Тут радиус метеорита, у лазера нет свойтва радиус.
            Sounds.explosion_sound.play()

    def check_health_points(self):
        """Проверка запаса здоровья корабля"""
        if self.player.health <= 0:
            print('Корабль разрушен')
            print('Набранные очки:', self.score)
            pygame.quit()
            exit()

    def event_attack(self, event):
        """Проверка атаки"""
        if event.type == self.player.SPACESHIP_ATTACK:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.lasers.add(self.player.shoot())
                Sounds.shoot_sound.play()

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

        # Вывожу счёт
        Interface.scores(self,
                         surface=self.main_window,
                         text='Scores: ' + str(self.score),
                         size=25,
                         x=0,
                         y=Config.SpriteHealthPoints_size[1] + 15)

    def tick(self):
        """То что происходит каждый кадр"""
        # Обработка событий
        self.ckeck_events()

        # Отрисовка кадра
        self.draw()

    def main_loop(self):
        Sounds.background_sound.play()
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
