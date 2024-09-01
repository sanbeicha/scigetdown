# ///////////////////////////////////////////////////////////////
#
# BY: liumian
# PROJECT MADE WITH: Qt Designer and PySide6
# DATE: 2024/8/28
# V: 1.0.0
#
# 用来设置菜单栏。
#
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenu

from .help_menu import (
    on_about_develop_clicked,
    on_about_soft_clicked,
    on_update_soft_clicked,
)


def init_menu(self) -> None:
    # help_menu = QMenu("&Help", self)
    self.help_menu = QMenu("&Help", self)

    # help_menu
    about_soft = QAction("软件版本", self)
    self.on_about_soft_clicked = on_about_soft_clicked.__get__(self)
    about_soft.triggered.connect(self.on_about_soft_clicked)
    self.help_menu.addAction(about_soft)

    about_develop = QAction("软件说明", self)
    self.on_about_develop_clicked = on_about_develop_clicked.__get__(self)
    about_develop.triggered.connect(self.on_about_develop_clicked)
    self.help_menu.addAction(about_develop)

    about_help = QAction("帮助文件", self)
    self.help_menu.addAction(about_help)

    update_soft = QAction("更新软件", self)
    self.on_update_soft_clicked = on_update_soft_clicked.__get__(self)
    update_soft.triggered.connect(self.on_update_soft_clicked)
    self.help_menu.addAction(update_soft)

    self.addMenu(self.help_menu)

    # retranslateUi(self)


def retranslateUi(self) -> None:
    # 更新菜单项文本
    # self.menubar.clear()  # 清除现有菜单项
    # self.file_menu.setText(QCoreApplication.translate("MainWindow", "文件", None))
    self.help_menu.setText(QCoreApplication.translate("MainWindow", "帮助", None))
