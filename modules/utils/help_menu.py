# -*- coding: utf-8 -*-

# ///////////////////////////////////////////////////////////////
#
# BY: liumian
# PROJECT MADE WITH: Qt Designer and PySide6
# DATE: 2024/8/28
# V: 1.0.0
#
# 用来展示帮助菜单栏下的内容。
# 重要的是提供了关于本软件、开发人员、更新等内容的展示。
#
# ///////////////////////////////////////////////////////////////


from PySide6.QtWidgets import QMessageBox, QDialog, QTextEdit, QPushButton, QVBoxLayout
import version

from .. import update_module as 自动更新模块

全局_项目名称 = "sanbeicha/scigetdown"
全局_应用名称 = "my_app.app"
全局_当前版本 = version.version
全局_官方网址 = "https://github.com/sanbeicha/scigetdown"

def on_about_soft_clicked(self) -> None:
    # 创建一个 QMessageBox 对话框
    msg_box = QMessageBox(self)
    msg_box.setWindowTitle("关于本软件")
    msg_box.setText(f"""
软件版本：{全局_当前版本}.
最新版本：.
发布日期：2024/08/28
适用环境：Window及MacOS操作系统.
版权归属：上海博航纳影信息科技有限公司.
联系方式：.
""")
    msg_box.exec()


def on_about_develop_clicked(self) -> None:
    long_text = """
    本软件基于python、pyside6开发。
    用于提供scihub文章批量下载功能。
    """

    msg_log = QDialog(self)
    msg_log.setWindowTitle("关于开发")
    # 创建一个文本编辑器控件，设置为只读
    msg_log.text_edit = QTextEdit()
    msg_log.text_edit.setReadOnly(True)

    # 设置文本编辑器的文本
    msg_log.text_edit.setText(long_text)

    # 创建一个垂直布局
    layout = QVBoxLayout()
    layout.addWidget(msg_log.text_edit)

    # 创建一个关闭按钮
    close_button = QPushButton("关闭")
    close_button.clicked.connect(msg_log.accept)

    # 将关闭按钮添加到布局中
    layout.addWidget(close_button)

    # 设置布局到对话框
    msg_log.setLayout(layout)
    msg_log.exec()


def on_update_soft_clicked(self) -> None:
    self.winUpdate = 自动更新模块.窗口_更新软件(Github项目名称=全局_项目名称,
                                        应用名称=全局_应用名称,
                                        当前版本号=全局_当前版本,
                                        官方网址=全局_官方网址)
    self.winUpdate.show()
