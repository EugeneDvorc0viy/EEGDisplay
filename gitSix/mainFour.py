# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowFour.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowCreate(object):
    def setupUi(self, WindowCreate):
        WindowCreate.setObjectName("WindowCreate")
        WindowCreate.resize(736, 442)
        self.centralwidget = QtWidgets.QWidget(WindowCreate)
        self.centralwidget.setObjectName("centralwidget")
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
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(160, 80, 20, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(550, 80, 20, 351))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btnDateShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnDateShow.setGeometry(QtCore.QRect(580, 400, 141, 28))
        self.btnDateShow.setObjectName("btnDateShow")
        self.cbData = QtWidgets.QComboBox(self.centralwidget)
        self.cbData.setGeometry(QtCore.QRect(10, 90, 151, 22))
        self.cbData.setObjectName("cbData")
        self.tbData = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbData.setGeometry(QtCore.QRect(170, 130, 381, 311))
        self.tbData.setObjectName("tbData")
        WindowCreate.setCentralWidget(self.centralwidget)

        self.retranslateUi(WindowCreate)
        QtCore.QMetaObject.connectSlotsByName(WindowCreate)

    def retranslateUi(self, WindowCreate):
        _translate = QtCore.QCoreApplication.translate
        WindowCreate.setWindowTitle(_translate("WindowCreate", "MainWindow"))
        self.btnCreate.setText(_translate("WindowCreate", "?????????????? ??????????????????????"))
        self.btnDo.setText(_translate("WindowCreate", "???????????????? ??????????????????????"))
        self.btn.setText(_translate("WindowCreate", "?????????????"))
        self.btnBd.setText(_translate("WindowCreate", "???????? ????????????"))
        self.btnSett.setText(_translate("WindowCreate", "??????????????????"))
        self.btnDateShow.setText(_translate("WindowCreate", "????????????????"))
