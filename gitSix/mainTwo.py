# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowTwo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 80, 351, 351))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.widgetMain = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.widgetMain.setContentsMargins(0, 0, 0, 0)
        self.widgetMain.setObjectName("widgetMain")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.widgetMain.addWidget(self.label)
        self.tbInfo = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.tbInfo.setObjectName("tbInfo")
        self.widgetMain.addWidget(self.tbInfo)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbThree = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbThree.setText("")
        self.lbThree.setObjectName("lbThree")
        self.horizontalLayout_3.addWidget(self.lbThree)
        self.lbTwo = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbTwo.setText("")
        self.lbTwo.setObjectName("lbTwo")
        self.horizontalLayout_3.addWidget(self.lbTwo)
        self.lbOne = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lbOne.setText("")
        self.lbOne.setObjectName("lbOne")
        self.horizontalLayout_3.addWidget(self.lbOne)
        self.widgetMain.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd.setObjectName("lcd")
        self.horizontalLayout_2.addWidget(self.lcd)
        self.btnStart = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout_2.addWidget(self.btnStart)
        self.btnReset = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout_2.addWidget(self.btnReset)
        self.widgetMain.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(560, 80, 160, 351))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.widgetSecond = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.widgetSecond.setContentsMargins(0, 0, 0, 0)
        self.widgetSecond.setObjectName("widgetSecond")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 711, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCreate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout.addWidget(self.btnCreate)
        self.btnDo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnDo.setObjectName("btnDo")
        self.horizontalLayout.addWidget(self.btnDo)
        self.btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn.setObjectName("btn")
        self.horizontalLayout.addWidget(self.btn)
        self.btnBd = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnBd.setObjectName("btnBd")
        self.horizontalLayout.addWidget(self.btnBd)
        self.btnSett = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSett.setObjectName("btnSett")
        self.horizontalLayout.addWidget(self.btnSett)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 70, 16, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(540, 80, 16, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 90, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.leHelpJson = QtWidgets.QLineEdit(self.centralwidget)
        self.leHelpJson.setGeometry(QtCore.QRect(10, 210, 151, 21))
        self.leHelpJson.setObjectName("leHelpJson")
        self.btnHelpJson = QtWidgets.QPushButton(self.centralwidget)
        self.btnHelpJson.setEnabled(False)
        self.btnHelpJson.setGeometry(QtCore.QRect(10, 240, 93, 28))
        self.btnHelpJson.setObjectName("btnHelpJson")
        self.lbHelpJson = QtWidgets.QLabel(self.centralwidget)
        self.lbHelpJson.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.lbHelpJson.setObjectName("lbHelpJson")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tbInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">?????????? ???????????? ?????????????????????? ?????????? ?????????????? ???????????????? ???????? ???? ???????????? ???????????????????? ????????</span></p></body></html>"))
        self.btnStart.setText(_translate("MainWindow", "????????????"))
        self.btnReset.setText(_translate("MainWindow", "??????????"))
        self.btnCreate.setText(_translate("MainWindow", "?????????????? ??????????????????????"))
        self.btnDo.setText(_translate("MainWindow", "???????????????? ??????????????????????"))
        self.btn.setText(_translate("MainWindow", "?????????????"))
        self.btnBd.setText(_translate("MainWindow", "???????? ????????????"))
        self.btnSett.setText(_translate("MainWindow", "??????????????????"))
        self.btnHelpJson.setText(_translate("MainWindow", "??????????????"))
        self.lbHelpJson.setText(_translate("MainWindow", "?????????????? ????????"))
