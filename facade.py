from sql import Database

class Facade:
    def __init__(self, name="database.db"):
        self.D = Database(name)
        self.D.createTable()

    def insert(self, name, developer, year):
        self.D.insertTable(name, developer, year)

    def read(self):
        result = self.D.readTable()
        return result

    def delete(self):
        self.D.deleteTable()

    def getName(self):
        name = []

        for i in self.D.readTable():
            name.append(i[1])
        print(name)
        return name

    def getDeveloper(self):
        developer = []

        for i in self.D.readTable():
            developer.append(i[2])
        print(developer)
        return developer

    def getYear(self):
        year = []

        for i in self.D.readTable():
            year.append(i[3])
        print(year)
        return year



if __name__ == '__main__':
    F = Facade()
    #F.insert("GTAV", "Rockstar", 2013)
    #F.read()
    #F.insert("STALKER", "GSC GAME WORLD", 2007)
    #F.getName()
    #F.getDeveloper()
    #F.getYear()
    #F.delete()
    F.insert("Metro2033", "4A Games", 2013)
    
