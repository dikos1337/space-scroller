import os


class Config:
    TITLE = 'Space Shooter'
    FPS = 60
    WIDTH = 1200  # Ширина окна игры
    HEIGHT = 800  # Высота окна игры

    SPRITE_PLAYER_SPACESHIP_INIT_X = WIDTH / 2  # координаты спавна корабля по x

    SPRITE_PLAYER_SPACESHIP_INIT_Y = HEIGHT / 1.2  # координаты спавна корабля по y
    SPRITE_HEALTHPOINTS_SIZE = (30, 25)  # x,y ; pixels

    BUFF_PROC_CHANCE = 0.05  # Шнас прока бафа 5%

    TOTAL_METEORITES = 35  # Количество метеоритов на уровне

    GAME_FOLDER = os.path.dirname(__file__)  # Папка с игрой
    IMG_FOLDER = os.path.join(GAME_FOLDER, 'res', 'sprites')  # Папка со спрайтами
    SND_FOLDER = os.path.join(GAME_FOLDER, 'res', 'sounds')  # Папка с музыкой
