import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

from facade import Facade


class MainWindow(QMainWindow):
    facade = Facade()
    def __init__(self, Facade):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("forms/MainWindow.ui", self)
        self.window().setWindowTitle("GamesJournal")
        self.btn_add.clicked.connect(lambda: self.add())
        self.btn_delete.clicked.connect(lambda: self.delete())
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Разработчик", "Год релиза"])
        self.build()

    def add(self):
        name = self.name.text()
        developer = self.developer.text()
        year = self.year.text()

        self.facade.insert(name, developer, year)
        self.name.clear()
        self.developer.clear()
        self.year.clear()
        self.build()

    def delete(self):
        self.facade.delete()
        self.tableWidget.clear()

    def build(self):
        self.tableWidget.clear()
        rows = self.facade.read()
        self.tableWidget.setRowCount(len(rows))
        
        for i, shop in enumerate(rows):
            for x, field in enumerate(shop):     # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))        # записываем текст в ячейку
                if x == 0:                      # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, x, item)


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    window = MainWindow(Facade)
    window.show()

    qapp.exec()

