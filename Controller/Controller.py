import sys
from PyQt5 import QtWidgets

from vievs.viev import View
from Model.SocketServer import Server
from Model.SocketServer import ControlConnection
from tune_up.settings import Settings
import threading


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        pathSettings = r'tune_up/settings'
        self.testSettings = Settings(pathSettings)
        self._view = View()
        self.objServer = Server(self.testSettings)
        self.objServer.start()
        thread = threading.Thread(target=ControlConnection, args=(self.testSettings,))
        thread.start()
        self.init()

    def init(self):
        self._view.ButtonToUpSignal.connect(self.moveUp)
        self._view.ButtonToLeftSignal.connect(self.moveLeft)
        self._view.ButtonToBeckSignal.connect(self.moveBack)
        self._view.ButtonToRightSignal.connect(self.moveRight)


    def pushButtonOn(self):
        if self.objServer.run_projector() == 0:
            self._view.Error_Connection()
        else:
            print("Проектор включён")


    def pushButtonOff(self):
        if self.objServer.stop_projector() == 0:
            self._view.Error_Connection()
        else:
            print("Проектор выключен")

    def pushButtonM1Yes(self):
        if self.objServer.run_monitor1() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №1 включён")

    def pushButtonM1No(self):
        if self.objServer.stop_monitor1() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №1 выключен")

    def pushButtonM2Yes(self):
        if self.objServer.run_monitor2() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №2 включён")

    def pushButtonM2No(self):
        if self.objServer.stop_monitor2() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №2 выключен")


    def pushButtonM3Yes(self):
        if self.objServer.run_monitor3() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №3 включён")


    def pushButtonM3No(self):
        if self.objServer.stop_monitor3() == 0:
            self._view.Error_Connection()
        else:
            print("Монитор №3 выключен")

    def pushButtonAllMOn(self):
        if self.objServer.run_video() == 0:
            self._view.Error_Connection()
        else:
            print("Все мониторы включены")


    def pushButtonAllMOff(self):
        if self.objServer.stop_video() == 0:
            self._view.Error_Connection()
        else:
            print("Все мониторы выключены")

    def pushStop(self):
        self.objServer.stop()

    def run(self):
        self._view.show()
        return self._app.exec_()

    def moveUp(self):
        print('Движение вперед')

    def moveRight(self):
        print('Движение вправо')

    def moveLeft(self):
        print('Движение влево')

    def moveBack(self):
        print('Движение назад')

