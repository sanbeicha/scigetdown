# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'indexLzbUvM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
## DATE: 2024/8/28
## V1.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QMenuBar, QPushButton, QStatusBar, QWidget, QVBoxLayout
from ..utils.init_menu import init_menu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.pushButton = QPushButton(self.centralwidget)
        # self.pushButton.setObjectName(u"pushButton")
        # self.pushButton.setGeometry(QRect(730, 0, 60, 22))
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 730, 22))

        init_menu(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "博航纳影™", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", "退出登录", None))
        self.statusbar.showMessage(QCoreApplication.translate("MainWindow", "欢迎使用博航纳影™的这款软件", None))
