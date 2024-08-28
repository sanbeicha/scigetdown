# -*- coding: utf-8 -*-

###############################################################################
## Form generated from reading UI file 'indexLzbUvM.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
## DATE: 2024/8/28
## V1.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow
import re
import warnings

# from scholarly import scholarly
# from scihub_cn.scihub import SciHub

from .index_ui import Ui_MainWindow


class Index(QMainWindow, Ui_MainWindow):
# class Index(QWidget):
    def __init__(self, main) -> None:
        super(Index, self).__init__()
        self.main = main
        self.index_win = QMainWindow()
        self.setupUi(self.index_win)
        # self.pushButton.clicked.connect(self.index_login_show)
        # 禁止窗口拉伸、禁用最大化按钮
        self.index_win.setFixedSize(self.index_win.width(),
                                    self.index_win.height())

    def index_login_show(self) -> None:
        self.index_win.close()
        # self.main.login_ui.login_win.show()

    def getscidown(self) -> None:
        pass
    """
        keyword = 'Mixed Reality Surgery'

        # search = scholarly.search_pubs(keyword)
        search = ""
        scihub = SciHub()

        downloaded, total = 0, 20
        while downloaded < total:
            try:
                paper = next(search)

                title = paper['bib']['title']
                title = re.sub(r'[\\ /:"*?<>|]+', ' ', title)

                pub_year = paper['bib']['pub_year']

                num_citations = paper['num_citations']
                num_citations = '{:>{width}}'.format(num_citations, width=5)

                filename = f'{pub_year}_{title}_{num_citations}.pdf'

                url = scihub.search(paper['pub_url'])
                scihub.download(url, keyword, filename)

                downloaded += 1
                print(f'{downloaded + 1}/{total}', filename)
            except Exception as e:
                warnings.warn(str(e))
    """
