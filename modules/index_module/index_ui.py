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
from PySide6.QtWidgets import QMenuBar, QPushButton, QStatusBar, QVBoxLayout, QWidget

from ..utils.init_menu import init_menu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # 创建一个按钮
        # 使用翻译后的文本
        button_text = QCoreApplication.translate("MainWindow", "点击下载", None)
        button = QPushButton(button_text)

        # 将按钮添加到布局中
        self.verticalLayout.addWidget(button)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")

        init_menu(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "SciHub文献下载", None))
        self.statusbar.showMessage(QCoreApplication.translate("MainWindow", "欢迎使用SciHub文献批量下载软件.", None))
