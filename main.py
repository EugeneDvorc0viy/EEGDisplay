import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import mainOne, mainTwo
from JSONWORK import WorkJSON

JSONFile = WorkJSON()

menuBox = []
for elem in JSONFile.openning("json/file.json"):
    menuBox.append(elem)

with open("json/file.json", "r") as filej:
    file = json.load(filej)

class WindowOne(QtWidgets.QMainWindow, mainOne.Ui_WindowCreate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.comboBox.addItems(menuBox)
        self.comboBox.activated[str].connect(self.active)
        self.btnDo.clicked.connect(self.windowDecorator)

    def active(self, text):
        self.label.setText(JSONFile.forDisplay("json/file.json", text))

    @pyqtSlot()
    def windowDecorator(self):
        self.window = WindowTwo()
        self.window.show()
        self.close()

class WindowTwo(QtWidgets.QMainWindow, mainTwo.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.comboBox_2.addItems(menuBox)
        self.comboBox_2.activated[str].connect(self.test)

        self.btnCreate.clicked.connect(self.windowDecoratorTwo)
        self.btnStart.clicked.connect(self.debutTest)


    def test(self, text):
        self.label.setText(JSONFile.forDisplay("json/file.json", text))
        self.btnStart.setText(f'Запустить программу "{text}"')

    def debutTest(self):
        try:
            programma = self.label.text().split()[0]

        except Exception:
            self.label.setText("Сначала выберите программу.")

    def checkProg(self):
        self.label.setText(self.comboBox.text())

    @pyqtSlot()
    def windowDecoratorTwo(self):
        self.window = WindowOne()
        self.window.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowOne()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
