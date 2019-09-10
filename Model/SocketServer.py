#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
from threading import Thread

from tune_up.settings import Settings

def ControlConnection(Settings: Settings):
    while True:
        RPI = Settings.settings
        time.sleep(5)
        for i in RPI:
            if RPI[i][1] != None:
                try:
                    RPI[i][1].send(b"Test")  # отправляем любые данные
                    print("Дошло", RPI[i])
                    Settings.updateSettings(RPI)
                except BaseException:
                    print('connection timed out', RPI[i])  # соединение разорвано
                    RPI[i][1] = None


class Server(Thread):

    def __init__(self, Settings: Settings):
        Thread.__init__(self)
        self.Settings = Settings
        self.sock = socket.socket()
        self.sock.bind(('', 9090))
        self.sock.listen(1)
        self.n = 0
        self.RPI = self.Settings.settings


    def run(self):
        while True:
            self.conn, self.addr = self.sock.accept()
            for i in self.RPI:
                print(self.RPI[i][0])
                if self.RPI[i][0] == self.addr[0]:
                    self.RPI[i][1] = self.conn
                    print(self.RPI[i][1])
                    self.Settings.updateSettings(self.RPI)
                    print(self.RPI)

    # --------------------------------------------------------------
    def stop(self):
        print("stop EXHIBITION")
        self.terminate()


    def run_up(self):
            try:
                self.conn = self.RPI["Car"][1]
                if not self.conn is None:
                    self.conn.send(b"run_up")
                else:
                    return 1 #!!!!!!!!!!!!!!!!!!!!!!!!!
            except socket.error as e:
                print('error', str(e))
                return 0
            return 1



    def run_right(self):
            try:
                self.conn = self.RPI["Car"][1]
                if not self.conn is None:
                    self.conn.send(b"run_rigth")
                else:
                    return 1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            except socket.error as e:
                print('error', str(e))
                return 0
            return 1


    def run_left(self):
            try:
                self.conn = self.RPI["Car"][1]
                if not self.conn is None:
                    self.conn.send(b"run_left")
                else:
                    return 1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            except socket.error as e:
                print('error', str(e))
                return 0
            return 1


    def run_back(self):
            try:
                self.conn = self.RPI["Car"][1]
                if not self.conn is None:
                    self.conn.send(b"run_back")
                else:
                    return 1 #!!!!!!!!!!!!!!!!!!!!!!!!!!!
            except socket.error as e:
                print('error', str(e))
                return 0
            return 1

