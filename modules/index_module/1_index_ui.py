# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////
# 博航纳影sci文献下载软件
# 版权所有 @2024 博航纳影科技有限公司
# 作者：博航纳影科技有限公司
# 日期：2024-08-28
# 本模块提供首页展示
# v1.0
# ///////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMenuBar,
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

        # 第一个输入框
        # self.keywordInputs = [QLineEdit(placeholder="输入关键词")]
        self.keywordInputs = [QLineEdit()]
        self.keywordInputs[0].setPlaceholderText("输入关键词")
        self.verticalLayout.addWidget(self.keywordInputs[0])
        # self.verticalLayout.addWidget(self.keywordInputs[0])

        # 增加输入框按钮
        addButton_text = QCoreApplication.translate(
            "MainWindow", "增加输入框", None
        )
        self.addButton = QPushButton(addButton_text)
        self.addButton.clicked.connect(self.addInputBox)
        self.verticalLayout.addWidget(self.addButton)

        # 检索按钮
        searchButton_text = QCoreApplication.translate(
            "MainWindow", "检索", None
        )
        searchButton = QPushButton(searchButton_text)
        searchButton.clicked.connect(self.search)
        self.verticalLayout.addWidget(searchButton)

        # 将水平布局添加到主布局
        # self.MainWindow.addLayout(self.verticalLayout)

        # 结果标签
        self.resultLabel = QLabel("")
        self.verticalLayout.addWidget(searchButton)
        # self.MainWindow.addWidget(searchButton)

        # 创建文本区域用于显示结果
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        # 将布局添加到主布局
        # self.verticalLayout.addLayout(input_layout)
        # self.verticalLayout.addWidget(self.output_area)

        # 创建一个按钮
        # 使用翻译后的文本
        button_text = QCoreApplication.translate(
            "MainWindow", "点击下载", None
        )
        button = QPushButton(button_text)
        self.verticalLayout.addWidget(button)  # 将按钮添加到布局中

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")

        init_menu(self.menubar)

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
        search_terms = " ".join(
            [
                field.text()
                for field in self.input_fields
                if field.text().strip()
            ]
        )
        self.output_area.setText(search_terms)

    def add_more_fields(self):
        # 动态增加输入框
        self.add_input_field(self.layout())

    def addInputBox(self):
        # 动态添加新的输入框
        newInput = QLineEdit()
        self.keywordInputs.append(newInput)
        self.verticalLayout.insertWidget(
            self.verticalLayout.indexOf(
                self.verticalLayout.itemAt(self.verticalLayout.count() - 3)
            ),
            newInput,
        )

        # self.inputLayout.insertWidget(self.inputLayout.indexOf(
        # self.inputLayout.itemAt(self.inputLayout.count() - 3)), newInput)

    def search(self):
        # 获取所有输入框的文本并组合
        keywords = [
            input.text().strip()
            for input in self.keywordInputs
            if input.text().strip()
        ]
        if keywords:
            result = ", ".join(keywords)
            self.resultLabel.setText(f"检索词组合: {result}")
        else:
            self.resultLabel.setText("没有输入任何关键词。")

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "SciHub文献下载", None)
        )
        self.statusbar.showMessage(
            QCoreApplication.translate(
                "MainWindow",
                "欢迎使用博航纳影™开发的这款SciHub文献批量下载软件.",
                None,
            )
        )


"""
        # 第一个输入框
        # self.keywordInputs = [QLineEdit(placeholder="输入关键词")]
        self.keywordInputs = [QLineEdit()]
        self.keywordInputs[0].setPlaceholderText("输入关键词")
        self.verticalLayout.addWidget(self.keywordInputs[0])
        # self.verticalLayout.addWidget(self.keywordInputs[0])

        # 增加输入框按钮
        addButton_text =
            QCoreApplication.translate("MainWindow", "增加输入框", None)
        addButton = QPushButton(addButton_text)
        addButton.clicked.connect(self.addInputBox)
        self.verticalLayout.addWidget(addButton)

        # 检索按钮
        searchButton_text =
            QCoreApplication.translate("MainWindow", "检索", None)
        searchButton = QPushButton(searchButton_text)
        searchButton.clicked.connect(self.search)
        self.verticalLayout.addWidget(searchButton)

        # 将水平布局添加到主布局
        # self.MainWindow.addLayout(self.verticalLayout)

        # 结果标签
        self.resultLabel = QLabel("")
        self.verticalLayout.addWidget(searchButton)
        # self.MainWindow.addWidget(searchButton)

        # 创建文本区域用于显示结果
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)

        # 将布局添加到主布局
        layout.addLayout(input_layout)
        layout.addWidget(self.output_area)

        # 创建一个按钮
        # 使用翻译后的文本
        button_text = QCoreApplication.translate("MainWindow", "点击下载", None)
        button = QPushButton(button_text)
        self.verticalLayout.addWidget(button)  # 将按钮添加到布局中
"""
