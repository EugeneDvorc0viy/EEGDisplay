import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer, Qt
import time as timeSleep
import random
import mainOne, mainTwo, mainThree
from JSONWORK import WorkJSON
from DateJson import JsonForDate

JSONFile = WorkJSON()
jsonSave = JsonForDate("testFile")

menuBox = []
for elem in JSONFile.openning("json/file.json"):
    menuBox.append(str(elem))

# with open("json/file.json", "r") as filej:
#     file = json.load(filej)

def timeBreak(time):
    timeSleep.sleep(time)


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
        self.btnDel.clicked.connect(self.showDialog)
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

    @pyqtSlot()
    def deleteTasks(self):
        self.boxDelete.addItems(menuBox)
        self.boxDelete.setEnabled(True)
        self.label.setText("Выберите файл для удаления")

    def delete(self, title):
        JSONFile.killing("json/file.json", title)
        menuBox.remove(title)
        self.comboBox.clear()
        self.comboBox.addItems(menuBox)

    def showDialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Delete Dialog',
                                        'Эксперимент нужно удалить:')

        if ok:
            if text in menuBox:
                self.delete(text)
                self.label.setText(f"Эксперимент {str(text)} удален.")
            else:
                self.label.setText("Такого файла нет.")


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
        self.btnHelpJson.clicked.connect(self.addHelp)
        self.btnReset.clicked.connect(self.timeReset)

    def addHelp(self):
        self.fileName = self.leHelpJson.text()
        title = self.label.text()
        jsonSave.newTest(self.fileName, title, 3)
        self.lbHelpJson.setText("Файл создан")
        self.btnHelpJson.setEnabled(False)

    def taskStart(self):
        title = self.label.text()

        if self.btnStart.text() == "Start":
            element = JSONFile.showTest("json/file.json", title)
            self.workTask(element)
        elif self.btnStart.text() == "Stop":
            self.timer.stop()
            self.btnStart.setText("Start")
        else:
            if self.btnStart.text() != "Stop":
                self.tbInfo.setText("Сначала выберите Задание")


    def workTask(self, element):
        self.element = element
        try:
            if self.element:
                self.elem = self.element.pop(0)

                self.tbInfo.setText(self.elem.split('/')[0])
                time = int(self.elem.split('/')[1])
                # print(time)

                self.lcd.display(time)
                self.timeStart(time)
            else:
                self.tbInfo.setText("Эксперимент окончен.")
                self.btnStart.setText("Start")
                print(self.leHelpJson.text())
                jsonSave.fileDone(self.leHelpJson.text())
        except Exception:
            self.tbInfo.setText(element)

    def showTime(self):
        self.time -= 1
        self.lcd.display(self.time)
        self.lbOne.setText(f"Канал 3: {str(random.randint(0, 100))}")
        self.lbTwo.setText(f"Канал 2: {str(random.randint(0, 100))}")
        self.lbThree.setText(f"Канал 1: {str(random.randint(0, 100))}")
        context = [self.lbOne.text().split()[2], self.lbTwo.text().split()[2], self.lbThree.text().split()[2]]
        if self.time >= 0: status = True
        else: status = False
        jsonSave.addInfo(context, self.fileName, status)

        if self.time < 0:
            self.lcd.display(0)
            if self.element:
                timeBreak(3)
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
        self.tbInfo.setText("Программа отменена.")

    def test(self, text):
        self.label.setText(JSONFile.forDisplay("json/file.json", text).split()[0])
        self.tbInfo.setText(JSONFile.forDisplay("json/file.json", text))
        self.btnStart.setText('Start')
        self.btnHelpJson.setEnabled(True)


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
        self.btnReady.clicked.connect(self.goWindowOne)
        self.btnCreateTitleOk.clicked.connect(self.openAccess)
        self.btnCreateYet.clicked.connect(self.addTask)

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
        self.leCreateName.clear()
        self.leCreateDis.clear()
        self.leCreateTime.clear()
        colvo = JSONFile.openning("json/file.json")[self.title]["colvo"]
        if name and time and dis:
            pass
            JSONFile.changingTask("json/file.json", f'add/{self.title}/0', new=name)
            JSONFile.changingTask("json/file.json", f'change/{self.title}/{colvo}', part="disTask", new=dis)
            JSONFile.changingTask("json/file.json", f'change/{self.title}/{colvo}', part="time", new=time)
            self.lbCreateTaskStatus.setText("Okey")
            context = "Successful!"
        else:
            context = "Some Error"
        self.lbCreateTaskStatus.setText(context)


    @pyqtSlot()
    def goWindowOne(self):
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
