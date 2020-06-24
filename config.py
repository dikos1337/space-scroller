import os


class Config:
    FPS = 30
    TITLE = 'Spaceship game'
    WIDTH = 1200
    HEIGHT = 800

    SpritePlayerSpaceship_init_x = WIDTH / 2
    SpritePlayerSpaceship_init_y = HEIGHT / 1.2

    total_meteorites = 15  # Количество метеоритов на уровне

    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'sprites')
