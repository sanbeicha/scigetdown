# -*- coding: utf-8 -*-
################################################################################
## 博航纳影sci文献下载软件
## 版权所有 @2024 博航纳影科技有限公司
## 作者：博航纳影科技有限公司
## 日期：2024-08-28
###############################################################################

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
import os
import PySide6

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path

from modules.index_module.index import Index


class Main(QMainWindow):
    def __init__(self) -> None:
        super(Main, self).__init__()
        # 将所有的界面做集合
        self.index_ui = Index(self)
        self.setWindowIcon(QIcon("./icon.ico"))
        # 初始化登录界面
        self.index_ui.index_win.show()


if __name__ == "__main__":
    app = QApplication()
    QApplication.setStyle(QStyleFactory.create("Fusion"))  # 设置界面风格
    main = Main()
    app.exec()
