# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admin\PycharmProjects\Exhibition-mjun1 (1)\Exhibition-mjun1\vievs\softForCar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_softForCar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1299, 711)
        MainWindow.setMinimumSize(QtCore.QSize(1299, 711))
        MainWindow.setMaximumSize(QtCore.QSize(1299, 34343))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stream = QtWidgets.QGraphicsView(self.centralwidget)
        self.stream.setGeometry(QtCore.QRect(9, 38, 1211, 623))
        self.stream.setMinimumSize(QtCore.QSize(1211, 623))
        self.stream.setMaximumSize(QtCore.QSize(1211, 623))
        self.stream.setObjectName("stream")
        self.battery = QtWidgets.QProgressBar(self.centralwidget)
        self.battery.setGeometry(QtCore.QRect(30, 60, 151, 21))
        self.battery.setProperty("value", 0)
        self.battery.setInvertedAppearance(False)
        self.battery.setObjectName("battery")
        self.speedometer = QtWidgets.QLCDNumber(self.centralwidget)
        self.speedometer.setGeometry(QtCore.QRect(1090, 600, 111, 41))
        self.speedometer.setObjectName("speedometer")
        self.ButtonToUp = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonToUp.setGeometry(QtCore.QRect(90, 530, 50, 50))
        self.ButtonToUp.setMinimumSize(QtCore.QSize(50, 50))
        self.ButtonToUp.setMaximumSize(QtCore.QSize(75, 75))
        self.ButtonToUp.setObjectName("ButtonToUp")
        self.ButtonToBeck = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonToBeck.setGeometry(QtCore.QRect(90, 590, 50, 50))
        self.ButtonToBeck.setMinimumSize(QtCore.QSize(50, 50))
        self.ButtonToBeck.setMaximumSize(QtCore.QSize(75, 75))
        self.ButtonToBeck.setObjectName("ButtonToBeck")
        self.ButtonToLeft = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonToLeft.setGeometry(QtCore.QRect(30, 590, 50, 50))
        self.ButtonToLeft.setMinimumSize(QtCore.QSize(50, 50))
        self.ButtonToLeft.setMaximumSize(QtCore.QSize(75, 75))
        self.ButtonToLeft.setObjectName("ButtonToLeft")
        self.ButtonToRight = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonToRight.setGeometry(QtCore.QRect(150, 590, 50, 50))
        self.ButtonToRight.setMinimumSize(QtCore.QSize(50, 50))
        self.ButtonToRight.setMaximumSize(QtCore.QSize(75, 75))
        self.ButtonToRight.setObjectName("ButtonToRight")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 60, 121, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonToUp.setText(_translate("MainWindow", "PushButton"))
        self.ButtonToBeck.setText(_translate("MainWindow", "PushButton"))
        self.ButtonToLeft.setText(_translate("MainWindow", "PushButton"))
        self.ButtonToRight.setText(_translate("MainWindow", "PushButton"))
