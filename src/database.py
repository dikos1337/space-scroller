import sqlite3

from config import Config


class Database:
    """Класс для работы с базой данных игры"""

    def __init__(self):
        self.conn = sqlite3.connect(Config.DATABASE_NAME)
        self.cursor = self.conn.cursor()
        self._init_db()

    def insert_scores(self, datetime, score, session_time_sec, meteorite_hits):
        self.cursor.execute("INSERT INTO leaderboard VALUES(?,?,?,?)",
                            (datetime, score, session_time_sec, meteorite_hits))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def get_leaderborad(self):
        """Возвращает 10 записей из базы, отсортированных по очкам.
        Возвращает список кортежей, пример : [('2020-07-05 22:13:52.484312', 3350, 177, 161),]"""
        query = self.cursor.execute("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 10").fetchall()

        return query

    def _init_db(self):
        """Создание таблицы если её нет"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `leaderboard` (
                                `datetime` DATETIME,
                                `score` INT,
                                `session_time_sec` INT,
                                `meteorite_hits` INT
                                );
                               """)
        self.conn.commit()
