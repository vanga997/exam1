from sqlite3 import connect

class Database:
    def __init__(self, name):
        self.name = (f"{name}")
        self.table = "GamesJournal"
        self.sql = connect(self.name)
        self.createTable()

    def createTable(self):
        cursor = self.sql.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS '{self.table}' ( 
        name TEXT UNIQUE,
        developer TEXT,
        year INTEGER 
        )""")
        self.sql.commit()
        cursor.close()

    def insertTable(self, name, developer, year):
        cursor = self.sql.cursor()
        cursor.execute(f"""INSERT INTO '{self.table}' (name, developer, year) VALUES ('{name}', '{developer}', '{year}')""")
        self.sql.commit()
        cursor.close()

    def readTable(self):
        cursor = self.sql.cursor()
        cursor.execute(f"""SELECT * FROM '{self.table}'""")
        result = cursor.fetchall()
        print(result)
        return result

    def deleteTable(self):
        cursor = self.sql.cursor()
        cursor.execute(f"""DROP TABLE '{self.table}' """)
        self.sql.commit()
        cursor.close()


if __name__ == '__main__':
    D = Database()
    #D.createTable()
    #D.insertTable("MenOfWar", "BestWay", 2004)
    D.readTable()
    
