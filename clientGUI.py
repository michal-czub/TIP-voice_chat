# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDate, QTime
from PyQt5.QtWidgets import QLabel
import threading

from client import Client


class Ui_MainWindow(object):
    client = Client()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ChatRoom")
        MainWindow.resize(498, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 30, 141, 61))
        self.pushButton.setObjectName("pushButton_connect")
        self.pushButton.setFont(QtGui.QFont("Bahnschrift", 12))
        self.pushButton.setToolTip("<h3>Connect to the server</h3>")
        self.pushButton.setToolTipDuration(1500)
        self.pushButton.clicked.connect(self.connect_button_clicked)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 140, 141, 61))
        self.pushButton_2.setObjectName("pushButton_disconnect")
        self.pushButton_2.setFont(QtGui.QFont("Bahnschrift", 12))
        self.pushButton_2.setToolTip("<h3>Disconnect from the server</h3>")
        self.pushButton_2.setToolTipDuration(1500)
        # self.pushButton_2.clicked.connect(self.disconnect_button_clicked)

        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setFont(QtGui.QFont("Bahnschrift", 25))
        self.label8.setGeometry(70, 120, 150, 50)
        self.label8.setStyleSheet('color : brown')
        timer = QTimer(self.centralwidget)
        timer.timeout.connect(self.clock_fun)
        timer.start(1000)

        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setFont(QtGui.QFont("Bahnschrift", 15))
        self.label9.setGeometry(50, 175, 200, 50)
        date = QDate.currentDate().toString('dddd, MMM yyyy')

        # print(QLocale(QLocale.English, QLocale.UnitedStates).toString(self, "MMMM dd, yyyy"))

        self.label9.setText(date)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connect_button_clicked(self):
        Ui_MainWindow.client.connect()

    #def disconnet_button_clicked(self):

    def clock_fun(self):
        current_time = QTime.currentTime()
        display_time = current_time.toString('hh:mm:ss')
        self.label8.setText(display_time)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatRoom"))
        self.pushButton.setText(_translate("MainWindow", "CONNECT"))
        self.pushButton_2.setText(_translate("MainWindow", "DISCONNECT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
