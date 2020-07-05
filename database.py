import os
import sqlite3

from config import Config


class Database:
    """Класс для работы с базой данных игры"""

    def __init__(self):
        self.conn = sqlite3.connect(Config.DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def insert_scores(self, datetime, score, sesion_time_sec, meteorite_hits):
        self.cursor.execute("INSERT INTO leaderboard VALUES(?,?,?,?)", (datetime, score, sesion_time_sec, meteorite_hits))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def _init_table(self):
        """Если база создаётся впервые, то надо проинициализоровать таблицу"""
        self.cursor.execute("""CREATE TABLE `leaderboard` (
                                `datetime` DATETIME,
                                `score` INT,
                                `session_time_sec` int,
                                `meteorite_hits` INT
                                );
                               """)

        self.conn.commit()


# Если базы нету, то создаём её и таблицу в ней
db_doesnt_exist = Config.DATABASE_NAME not in os.listdir(Config.GAME_FOLDER)

if db_doesnt_exist:
    Database()._init_table()
