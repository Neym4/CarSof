from PyQt5 import QtCore, QtWidgets
from vievs.MainForm import Ui_softForCar

from vievs.video import videoThread


class View(QtWidgets.QMainWindow, Ui_softForCar):
    onClick = QtCore.pyqtSignal()

    ButtonToRightSignal = QtCore.pyqtSignal()  # Выключить пректор
    ButtonToLeftSignal = QtCore.pyqtSignal()  # Открыть параметры
    ButtonToBeckSignal = QtCore.pyqtSignal()  # Отправить Дмитрию сообщение
    ButtonToUpSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''
        self.text1 = ''
        self.initUi()

        # ico = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay) # Иконка в трее
        # self.sys_tray = QtWidgets.QSystemTrayIcon(ico, self)  #
        #
        # self.sys_tray.setToolTip("MonitorManagment")  # Текст выходящий при наведении на иконку в трее
        #
        # self.sys_tray.activated.connect(self.on_activated)
        #
        # self.sys_tray.messageClicked.connect(self.on_messageClicked)
        # self.sys_tray.show()
        #
        # self.on_create_context_menu()

    def initUi(self):
        self.Video = videoThread('192.168.1.101')
        self.Video.start()

        self.graphicsSceneImage = QtWidgets.QGraphicsScene()
        self.ButtonToRight.clicked.connect(self.ButtonToRightSignal)
        self.ButtonToLeft.clicked.connect(self.ButtonToLeftSignal)
        self.ButtonToBeck.clicked.connect(self.ButtonToBeckSignal)
        self.ButtonToUp.clicked.connect(self.ButtonToUpSignal)

        self.Video.frameSignal.connect(self.showGraphicsViewImage, QtCore.Qt.QueuedConnection)

    def showGraphicsViewImage(self, pixMap):
        self.graphicsSceneImage.clear()
        self.graphicsSceneImage.addPixmap(pixMap)
        self.graphicsView.setScene(self.graphicsSceneImage)

    def Error_Connection(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText('Не все клиенты(Raspberry) подключились!')
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.exec_()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_W:
            self.ButtonToUpSignal.emit()
        if e.key() == QtCore.Qt.Key_D:
            self.ButtonToRightSignal.emit()
        if e.key() == QtCore.Qt.Key_S:
            self.ButtonToBeckSignal.emit()
        if e.key() == QtCore.Qt.Key_A:
            self.ButtonToLeftSignal.emit()






    # def on_create_context_menu(self):
    #     self.menuSystemTray = QtWidgets.QMenu("&SystemTray")
    #     self.actShowHide = QtWidgets.QAction("&Отобразить или скрыть окно", None)
    #     self.actShowHide.triggered.connect(self.on_show_hide)
    #     self.menuSystemTray.addAction(self.actShowHide)
    #     self.menuSystemTray.addSeparator()
    #     self.actQuit = QtWidgets.QAction("&Выход", None)
    #
    #     self.actQuit.triggered.connect(QtWidgets.qApp.quit)
    #     self.actQuit.triggered.connect(self.stopSignal)
    #
    #     self.menuSystemTray.addAction(self.actQuit)
    #     self.sys_tray.setContextMenu(self.menuSystemTray)

    # def closeEvent(self, e):
    #     self.hide()
    #     e.ignore()
    #
    # def on_clicked(self):
    #     self.sys_tray.showMessage("Название", "Текст сообщения", msecs=2000)
    #
    # def on_show_hide(self):
    #     if self.isVisible():
    #         self.hide()
    #     else:
    #         self.show()
    #         self.activateWindow()
    #
    # def on_activated(self, st):
    #     print("on_activated", st)
    #
    # def on_messageClicked(self):
    #     print("on_messageClicked")
    #
