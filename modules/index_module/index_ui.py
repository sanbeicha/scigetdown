# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////
# 博航纳影sci文献下载软件
# 版权所有 @2024 博航纳影科技有限公司
# 作者：博航纳影科技有限公司
# 日期：2024-08-28
# 本模块提供首页展示
# v4.0
# ///////////////////////////////////////////////////
from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QMessageBox,
    QStatusBar,
    QTextEdit,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QMenuBar,
    QHBoxLayout,
)

from ..utils.init_menu import init_menu


class Ui_MainWindow(object):
    MAX_INPUT_FIELDS = 10  # 定义最大输入框数量

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        init_menu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.input_fields = []  # 存储每个输入字段和下拉框的组合
        self.input_layouts = []  # 存储每个输入字段的布局
        self.condition_combos = []  # 存储条件组合框的引用
        input_layout = self.addInputFields()

        self.addButtons(input_layout)

        # 添加一个间隔，确保文本区域在输入框下方
        self.verticalLayout.addLayout(input_layout)
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addSpacerItem(spacer_item)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        # self.verticalLayout.addLayout(input_layout)
        self.verticalLayout.addWidget(self.output_area)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 直接设置窗口标题
        # MainWindow.setWindowTitle("SciHub文献下载")
        # 直接设置状态栏消息
        # self.statusbar.showMessage("欢迎使用SciHub文献批量下载软件")
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def addInputFields(self):
        layout = QHBoxLayout()
        self.add_input_field(layout)
        self.input_layouts.append(layout)  # 将布局添加到 input_layouts 列表
        # 初始添加一个输入框
        # for _ in range(1):
        #     self.add_input_field(layout)
        return layout

    def add_input_field(self, layout):
        combo_box = QComboBox()
        combo_box.addItems(["关键词", "作者", "论文标题", "发表年份", "DOI"])
        combo_box.currentIndexChanged.connect(self.update_input_logic)

        input_field = QLineEdit()
        input_field.setPlaceholderText("请输入" + combo_box.currentText())

        layout.addWidget(combo_box)
        layout.addWidget(input_field)

        # 检查是否是第一次添加输入字段
        if len(self.input_fields) > 0:
            delete_button = QPushButton("删除")
            delete_button.clicked.connect(self.delete_input_field)
            layout.addWidget(delete_button)
            # self.input_fields.append((layout, combo_box, None, input_field, delete_button))
        else:
            delete_button = None
            # self.input_fields.append((layout, combo_box, None, input_field, None))

        condition_combo = None
        if combo_box.currentText() == "发表年份":
            condition_combo = QComboBox()
            condition_combo.addItems(["等于", "大于", "小于"])
            layout.addWidget(condition_combo)

        self.input_fields.append((layout, combo_box, condition_combo, input_field, delete_button))

    def delete_input_field(self):
        # 获取发送事件的按钮
        delete_button = self.sender()
        # 遍历 input_fields 列表，找到对应的删除按钮
        for i, (layout, combo_box, condition_combo, input_field, button) in enumerate(self.input_fields):
            # for layout, combo_box, condition_combo, input_field, button in self.input_fields:
            if button == delete_button:
                if condition_combo is not None:
                    layout.removeWidget(condition_combo)
                    condition_combo.deleteLater()

                # 从布局中移除控件
                layout.removeWidget(combo_box)
                layout.removeWidget(input_field)
                layout.removeWidget(button)

                # 删除控件
                combo_box.deleteLater()
                input_field.deleteLater()
                button.deleteLater()

                self.input_fields.pop(i)

                # 从列表中移除对应的元素
                # self.input_fields.remove((layout, combo_box, condition_combo, input_field, button))
                # self.input_fields = [field for field in self.input_fields if field[1] != condition_combo]

                break

    # def update_input_logic(self):
    #     combo_box = self.sender()
    #     for layout, combo, condition_combo, input_field, _ in self.input_fields:
    #         if combo == combo_box:
    #             field_type = combo_box.currentText()
    #             if field_type == "发表年份":
    #                 if condition_combo is None:
    #                     condition_combo = QComboBox()
    #                     condition_combo.addItems(["等于", "大于", "小于"])
    #                     # 将条件组合框插入到 combo_box 和 input_field 之间
    #                     layout.insertWidget(1, condition_combo)
    #                     self.condition_combos.append(condition_combo)
    #                 condition = condition_combo.currentText()
    #                 input_field.setPlaceholderText(f"请输入{condition}年份")
    #                 validator = QIntValidator(1900, 2050)
    #                 input_field.setValidator(validator)  # 设置年份验证器
    #             else:
    #                 input_field.setPlaceholderText("请输入" + field_type)
    #                 input_field.setValidator(None)  # 清除验证器
    #                 if condition_combo is not None:
    #                     layout.removeWidget(condition_combo)
    #                     condition_combo.deleteLater()
    #                     condition_combo = None
    #                     self.input_fields[self.input_fields.index((layout, combo, condition_combo, input_field))] = (layout, combo, condition_combo, input_field)
    #             break

    def update_input_logic(self):
        combo_box = self.sender()
        for i, (layout, combo_box, condition_combo, input_field, button) in enumerate(self.input_fields):
            # if combo_box == combo_box:
            if combo_box == self.sender():
                field_type = combo_box.currentText()
                if field_type == "发表年份":
                    if condition_combo is None:
                        condition_combo = QComboBox()
                        condition_combo.addItems(["等于", "大于", "小于"])
                        layout.insertWidget(1, condition_combo)
                        self.input_fields[i] = (layout, combo_box, condition_combo, input_field, button)
                    # condition = condition_combo.currentText()
                    # input_field.setPlaceholderText(f"请输入{condition}年份")
                    input_field.setPlaceholderText("请输入年份")
                    condition_combo.currentIndexChanged.connect(lambda: self.update_condition_input(i))
                    validator = QIntValidator(1000, 9999)
                    input_field.setValidator(validator)
                else:
                    input_field.setPlaceholderText("请输入" + field_type)
                    input_field.setValidator(None)
                    if condition_combo:
                        layout.removeWidget(condition_combo)
                        condition_combo.deleteLater()
                        self.input_fields[i] = (layout, combo_box, None, input_field, button)
                break

    def update_condition_input(self, index):
        condition = self.input_fields[index][2].currentText()
        input_field = self.input_fields[index][3]
        input_field.setPlaceholderText(f"请输入{condition}年份")

    def addButtons(self, layout):
        add_button = QPushButton("添加")
        add_button.clicked.connect(self.addInputBox)
        layout.addWidget(add_button)

        search_button = QPushButton("检索")
        search_button.clicked.connect(self.perform_search)
        layout.addWidget(search_button)

    def addInputBox(self):
        if len(self.input_fields) < self.MAX_INPUT_FIELDS:
            new_layout = QHBoxLayout()
            self.add_input_field(new_layout)
            self.verticalLayout.addLayout(new_layout)
            self.input_layouts.append(new_layout)

            # # self.add_input_field(self.verticalLayout)
            # current_layout = self.verticalLayout.itemAt(self.verticalLayout.count() - 1).layout()
            # if isinstance(current_layout, QHBoxLayout):
            #     self.add_input_field(current_layout)
            #     # self.add_input_field(self.verticalLayout)
            # else:
            #     # 如果最后一个不是 QHBoxLayout，则默认添加到 input_layout
            #     self.add_input_field(self.input_fields[-1].parent().layout())
        else:
            QMessageBox.warning(None, "提醒", "已达最大输入框数量限制。")

    def perform_search(self):
        # search_terms = ' '.join([field[0].text() for field in self.input_fields if field[0].text().strip()])
        search_terms = " ".join(
            [input_field.text() for _, _, _, input_field, _ in self.input_fields if input_field.text().strip()]
        )
        self.output_area.setText(search_terms if search_terms else "没有输入任何关键词。")

    def retranslateUi(self, MainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "SciHub文献下载", None))
        self.statusbar.showMessage(QCoreApplication.translate("MainWindow", "欢迎使用SciHub文献批量下载软件", None))
