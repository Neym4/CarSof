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


    def pushStop(self):
        self.objServer.stop()

    def run(self):
        self._view.show()
        return self._app.exec_()

    def moveUp(self):
        if self.objServer.run_up() == 0:
            self._view.Error_Connection
        else:
            print('Движение вперед')

    def moveRight(self):
        if self.objServer.run_right() == 0:
            self._view.Error_Connection()

        else:
            print('Движение вправо')


    def moveLeft(self):
        if self.objServer.run_left() == 0:
            self._view.Error_Connection()
        else:
            print('Движение влево')


    def moveBack(self):
        if self.objServer.run_back() == 0:
            self._view.Error_Connection()
        else:
            print('Движение назад')


