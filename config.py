import os


class Config:
    FPS = 60
    TITLE = 'Spaceship game'
    WIDTH = 1200
    HEIGHT = 800

    SpritePlayerSpaceship_init_x = WIDTH / 2
    SpritePlayerSpaceship_init_y = HEIGHT / 1.2
    SpriteHealthPoints_size = (30, 25)  # x,y ; pixels

    total_meteorites = 25  # Количество метеоритов на уровне

    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'sprites')
