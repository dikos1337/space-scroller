import os


class Config:
    # TODO: Сделать все константы в upper case
    TITLE = 'Spaceship game'
    FPS = 60
    WIDTH = 1200  # Ширина окна игры
    HEIGHT = 800  # Высота окна игры

    SpritePlayerSpaceship_init_x = WIDTH / 2  # координаты спавна корабля по x
    SpritePlayerSpaceship_init_y = HEIGHT / 1.2  # координаты спавна корабля по y
    SpriteHealthPoints_size = (30, 25)  # x,y ; pixels

    BUFF_PROC_CHANCE = 0.05  # Шнас прока бафа 5%

    total_meteorites = 35  # Количество метеоритов на уровне

    game_folder = os.path.dirname(__file__)  # Папка с игрой
    img_folder = os.path.join(game_folder, 'src', 'sprites')  # Папка со спрайтами
    snd_folder = os.path.join(game_folder, 'src', 'sounds')  # Папка с музыкой
