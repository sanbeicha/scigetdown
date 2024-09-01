# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////
# 博航纳影sci文献下载软件
# 版权所有 @2024 博航纳影科技有限公司
# 作者：博航纳影科技有限公司
# 日期：2024-08-28
# 本模块提供首页展示
# v3.0
# ///////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QMdiArea,
    QMdiSubWindow,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
)

# from ..utils.init_menu import init_menu


class Ui_MainWindow(object):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        # 设置窗口标题和初始大小
        MainWindow.setWindowTitle("检索关键词应用")
        MainWindow.setGeometry(100, 100, 800, 600)

        # 创建菜单栏
        menu_bar = MainWindow.menuBar()
        file_menu = menu_bar.addMenu("文件")
        file_menu.addAction("退出", self.close)

        # 创建状态栏
        statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(statusbar)

        # 创建MDI区域
        self.mdi_area = QMdiArea()
        MainWindow.setCentralWidget(self.mdi_area)

        # 创建一个子窗口并添加到MDI区域
        self.create_sub_window()

    def create_sub_window(self):
        # 创建子窗口
        sub_window = QMdiSubWindow()
        self.mdi_area.addSubWindow(sub_window)
        sub_window.showMaximized()

        # 创建子窗口内部的布局
        layout = QVBoxLayout()

        # 创建输入框和检索按钮
        input_layout = QHBoxLayout()
        self.input_fields = [QLineEdit()]
        input_layout.addWidget(self.input_fields[0])

        self.search_button = QPushButton("检索")
        self.search_button.clicked.connect(self.perform_search)
        input_layout.addWidget(self.search_button)

        # 创建文本区域用于显示结果
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        # 将布局添加到子窗口
        layout.addLayout(input_layout)
        layout.addWidget(self.output_area)
        sub_window.setLayout(layout)

    def perform_search(self):
        # 获取所有输入框的文本并组合显示在输出框中
        search_terms = " ".join([field.text() for field in self.input_fields if field.text().strip()])
        self.output_area.setText(search_terms)

    def add_more_fields(self):
        # 动态增加输入框
        input_field = QLineEdit()
        self.input_fields.append(input_field)
        self.input_layout.insertWidget(len(self.input_fields) - 1, input_field)

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "SciHub文献下载", None))
        self.statusbar.showMessage(
            QCoreApplication.translate(
                "MainWindow",
                "欢迎使用博航纳影™开发的这款SciHub文献批量下载软件.",
                None,
            )
        )
        # self.search_button.setText(QCoreApplication.translate
        # ("MainWindow", "检索", None))
