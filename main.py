import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer, Qt
import time

import mainOne, mainTwo, mainThree
from JSONWORK import WorkJSON

JSONFile = WorkJSON()

menuBox = []
for elem in JSONFile.openning("json/file.json"):
    menuBox.append(elem)

with open("json/file.json", "r") as filej:
    file = json.load(filej)


class WindowOne(QtWidgets.QMainWindow, mainOne.Ui_WindowCreate):
    def __init__(self):
        # self.status = status
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.comboBox.addItems(menuBox)
        self.comboBox.activated[str].connect(self.active)
        self.btnDo.clicked.connect(self.goWindowTwo)
        self.btnAdd.clicked.connect(self.goWindowThree)
        # if self.status:
        #     self.label.setText(self.status)

    def active(self, text):
        self.label.setText(JSONFile.forDisplay("json/file.json", text))

    @pyqtSlot()
    def goWindowTwo(self):
        self.window = WindowTwo()
        self.window.show()
        self.close()

    @pyqtSlot()
    def goWindowThree(self):
        self.window = WindowThree()
        self.window.show()
        self.close()

class WindowTwo(QtWidgets.QMainWindow, mainTwo.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.setInterval(1000)
        self.time = 0

        self.comboBox_2.addItems(menuBox)
        self.comboBox_2.activated[str].connect(self.test)

        self.btnCreate.clicked.connect(self.windowDecoratorTwo)
        self.btnStart.clicked.connect(self.taskStart)

        self.btnReset.clicked.connect(self.timeReset)

    def taskStart(self):
        title = self.label.text().split()[0]
        if self.btnStart.text() == "Start":
            element = JSONFile.showTest("json/file.json", title)
            self.label.setText("Начало через 5 сек.")
            self.workTask(element)
        elif self.btnStart.text() == "Stop":
            self.timer.stop()
            self.btnStart.setText("Start")
        else:
            if self.btnStart.text() != "Stop":
                self.label.setText("Сначала выберите Задание")


    def workTask(self, element):
        self.element = element
        if self.element:
            self.elem = self.element.pop(0)

            self.label.setText(self.elem.split('/')[0])
            time = int(self.elem.split('/')[1])
            # print(time)

            self.lcd.display(time)
            self.timeStart(time - 1)
        else:
            print("Done")
            self.btnStart.setText("Start")

    def showTime(self):
        self.lcd.display(self.time)
        self.time -= 1
        if self.time < 0:
            self.timer.stop()
            self.time = 0
            self.workTask(self.element)

    def timeStart(self, time):
        if not self.time:
            self.time = time
        if not self.time: self.time = 10
        self.timer.start()
        self.btnStart.setText("Stop")

    def timeReset(self):
        self.timer.stop()
        self.btnStart.setText("Start")
        self.time = 0
        self.label.setText("Программа отменена.")

    def test(self, text):
        self.label.setText(JSONFile.forDisplay("json/file.json", text))
        self.btnStart.setText('Start')


    @pyqtSlot()
    def windowDecoratorTwo(self):
        self.window = WindowOne()
        self.window.show()
        self.close()

class WindowThree(QtWidgets.QMainWindow, mainThree.Ui_WindowCreate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        # self.btnReady.clicked.connect(self.goWindowOne)
        self.btnCreateTitleOk.clicked.connect(self.openAccess)
        self.btnReady.clicked.connect(self.addTask)

        self.flag = 0

    @pyqtSlot()
    def openAccess(self):
        self.title = self.leCreateTitle.text()
        if self.title:
            fileJson = JSONFile.openning("json/file.json")
            context = JSONFile.adding("json/file.json", self.title)
            if self.title not in fileJson:
                self.leCreateName.setEnabled(True)
                self.leCreateTime.setEnabled(True)
                self.leCreateDis.setEnabled(True)
                self.lbCreateTitleStatus.setText(context)
            else:
                self.lbCreateTitleStatus.setText(context)

    @pyqtSlot()
    def addTask(self):
        name = self.leCreateName.text()
        dis = self.leCreateDis.toPlainText()
        time = self.leCreateTime.text()
        colvo = JSONFile.openning("json/file.json")[self.title]["colvo"]
        if name and time and dis:
            pass
            JSONFile.changingTask("json/file.json", f'add/{self.title}/0', new=name)
            JSONFile.changingTask("json/file.json", f'change/{self.title}/{colvo}', part="disTask", new=dis)
            JSONFile.changingTask("json/file.json", f'change/{self.title}/{colvo}', part="time", new=time)
            self.lbCreateTaskStatus.setText("Okey")
            context = "Successful!"

        self.window = WindowOne()
        self.window.show()
        self.close()

    @pyqtSlot()
    def goWindowOne(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowOne()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
