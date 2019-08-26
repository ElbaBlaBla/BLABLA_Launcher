# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Launcher.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os
import platform


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        Launcher.setObjectName("Launcher")
        Launcher.resize(560, 326)
        font = QtGui.QFont()
        font.setPointSize(30)
        Launcher.setFont(font)
        self.BLABLA_Launcher = QtWidgets.QWidget(Launcher)
        self.BLABLA_Launcher.setObjectName("BLABLA_Launcher")
        self.label = QtWidgets.QLabel(self.BLABLA_Launcher)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Runexe = QtWidgets.QPushButton(self.BLABLA_Launcher)
        self.Runexe.setGeometry(QtCore.QRect(410, 280, 113, 32))
        self.Runexe.setObjectName("Runexe")
        self.label_2 = QtWidgets.QLabel(self.BLABLA_Launcher)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.mac_download = QtWidgets.QPushButton(self.BLABLA_Launcher)
        self.mac_download.setGeometry(QtCore.QRect(410, 120, 113, 32))
        self.mac_download.setObjectName("mac_download")
        self.label_3 = QtWidgets.QLabel(self.BLABLA_Launcher)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.win_download = QtWidgets.QPushButton(self.BLABLA_Launcher)
        self.win_download.setGeometry(QtCore.QRect(410, 180, 113, 32))
        self.win_download.setObjectName("win_download")
        self.status_label = QtWidgets.QLabel(self.BLABLA_Launcher)
        self.status_label.setGeometry(QtCore.QRect(90, 230, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        Launcher.setCentralWidget(self.BLABLA_Launcher)

        self.retranslateUi(Launcher)
        QtCore.QMetaObject.connectSlotsByName(Launcher)

    def retranslateUi(self, Launcher):
        _translate = QtCore.QCoreApplication.translate
        Launcher.setWindowTitle(_translate("Launcher", "Launcher"))
        self.label.setText(_translate("Launcher", "BLABLA Launcher"))
        self.Runexe.setText(_translate("Launcher", "실행"))
        self.label_2.setText(_translate("Launcher", "Mac OS 용 BLABLA"))
        self.mac_download.setText(_translate("Launcher", "다운로드"))
        self.label_3.setText(_translate("Launcher", "Windows 용 BLABLA"))
        self.win_download.setText(_translate("Launcher", "다운로드"))
        self.status_label.setText(_translate("Launcher", "상태 표시 라벨"))

        self.Run()
        
    def Run(self):
        self.mac_download.clicked.connect(self.Mac_downloader)
        self.win_download.clicked.connect(self.Win_downloader)
        self.Runexe.clicked.connect(self.EXE)

    def Mac_downloader(self): # 맥용 프로그램 다운로드    
        try:
            os.system("rm -rf BLABLA_mac") # 기존 디렉토리 삭제
            # 새로 다운로드
            os.system(
                "git clone https://github.com/ElbaBlaBla/BLABLA_mac.git")
            self.status_label.setText("다운로드 완료!")
        except Exception:
            self.status_label.setText("다시 다운로드 해주세요")                

    def Win_downloader(self):
        try:
            os.system("rm -rf BLABLA_windows")
            os.system(
                "git clone https://github.com/ElbaBlaBla/BLABLA_windows.git")
            self.status_label.setText("다운로드 완료!")
        except Exception:
            self.status_label.setText("다시 다운로드 해주세요")

    def EXE(self):
        if platform.system() == 'Darwin': # 맥일때
            os.system("open BLABLA_mac/BLABLA.app")
            print('실행!')
        elif platform.system() == 'Windows': # 윈도우 일떄
            os.system("BLABLA_windows/BLALBA.exe")                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Launcher = QtWidgets.QMainWindow()
    ui = Ui_Launcher()
    ui.setupUi(Launcher)
    Launcher.show()
    sys.exit(app.exec_())
