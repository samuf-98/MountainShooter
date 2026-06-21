import sqlite3


class DBProxy:

    #08.02.01 - INICIO
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS dados(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    score INTEGER NOT NULL,
                                    date TEXT NOT NULL)     
                                    '''
                                )
    #08.02.01 - FIM

    #08.02.02 - INICIO
    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()
    #08.02.02 - FIM

    #08.02.03 - INICIO
    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()
    #08.02.03 - FIM

    #08.02.04 - INICIO
    def close(self):
        self.connection.close()
    #08.02.04 - FIM


