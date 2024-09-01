# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////
# 博航纳影sci文献下载软件
# 版权所有 @2024 博航纳影科技有限公司
# 作者：博航纳影科技有限公司
# 日期：2024-08-28
# 本模块提供首页展示
# v2.0
# ///////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QLineEdit,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

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

        # 创建一个自定义的菜单栏容器
        # menu_bar_widget = QWidget()
        # menu_bar_layout = QHBoxLayout(menu_bar_widget)
        # menu_bar_layout = QHBoxLayout()
        # menu_bar_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        init_menu(self.menubar)
        # menu_bar_layout.addWidget(self.menubar)
        # self.setMenuBar(self.menubar)

        # 创建水平布局用于输入框和按钮
        # input_layout = QHBoxLayout()
        self.input_fields = []
        # self.add_input_field(input_layout)
        input_layout = self.addInputFields()

        self.addButtons(input_layout)

        # 创建增加输入框按钮
        self.search_button = QPushButton("添加")
        # self.search_button.clicked.connect(self.add_more_fields)
        self.search_button.clicked.connect(self.addInputBox)
        input_layout.addWidget(self.search_button)

        # 创建检索按钮
        self.search_button = QPushButton("检索")
        self.search_button.clicked.connect(self.perform_search)
        input_layout.addWidget(self.search_button)

        # 创建文本区域用于显示结果
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        # 将布局添加到主布局
        self.verticalLayout.addLayout(input_layout)
        self.verticalLayout.addWidget(self.output_area)

        # 设置主布局
        self.setLayout(self.verticalLayout)
        # self.setLayout(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def add_input_field(self, layout):
        # 创建一个新的输入框并添加到布局中
        input_field = QLineEdit()
        layout.addWidget(input_field)
        self.input_fields.append(input_field)

    def perform_search(self):
        # 获取所有输入框的文本并组合显示在输出框中
        search_terms = " ".join([field.text() for field in self.input_fields if field.text().strip()])
        self.output_area.setText(search_terms)

    def add_more_fields(self):
        # 动态增加输入框
        self.add_input_field(self.layout())

    def addInputBox(self):
        if len(self.input_fields) < 5:
            # 动态添加新的输入框
            newInput = QLineEdit()
            self.input_fields.append(newInput)
            # self.verticalLayout.insertWidget(self.verticalLayout.indexOf
            # (self.verticalLayout.itemAt(self.verticalLayout.count() - 3)),
            # newInput)
            self.verticalLayout.addWidget(newInput)
            # self.inputLayout.insertWidget(self.inputLayout.indexOf
            # (self.inputLayout.itemAt(self.inputLayout.count() - 3)),
            # newInput)
        else:
            # 如果输入框数量已经达到5个，则弹出提示框
            QMessageBox.warning(None, "提醒", "已达最大输入框数量限制。")

    def search(self):
        # 获取所有输入框的文本并组合
        keywords = [input.text().strip() for input in self.keywordInputs if input.text().strip()]
        if keywords:
            result = ", ".join(keywords)
            self.resultLabel.setText(f"检索词组合: {result}")
        else:
            self.resultLabel.setText("没有输入任何关键词。")

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "SciHub文献下载", None))
        self.statusbar.showMessage(
            QCoreApplication.translate(
                "MainWindow",
                "欢迎使用博航纳影™开发的SciHub文献批量下载软件",
                None,
            )
        )
