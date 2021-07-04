# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'static_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 803)
        self.open_video = QAction(MainWindow)
        self.open_video.setObjectName(u"open_video")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_pause = QPushButton(self.widget_2)
        self.pb_pause.setObjectName(u"pb_pause")
        self.pb_pause.setMinimumSize(QSize(100, 100))
        font = QFont()
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.pb_pause.setFont(font)

        self.gridLayout.addWidget(self.pb_pause, 3, 0, 1, 1)

        self.pb_start = QPushButton(self.widget_2)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setMinimumSize(QSize(100, 100))
        self.pb_start.setFont(font)

        self.gridLayout.addWidget(self.pb_start, 2, 0, 1, 1)

        self.pb_down = QPushButton(self.widget_2)
        self.pb_down.setObjectName(u"pb_down")
        self.pb_down.setMinimumSize(QSize(100, 100))
        font1 = QFont()
        font1.setPointSize(80)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.pb_down.setFont(font1)

        self.gridLayout.addWidget(self.pb_down, 0, 2, 1, 1)

        self.pb_right = QPushButton(self.widget_2)
        self.pb_right.setObjectName(u"pb_right")
        self.pb_right.setMinimumSize(QSize(100, 100))
        self.pb_right.setFont(font)

        self.gridLayout.addWidget(self.pb_right, 1, 2, 1, 1)

        self.pb_left = QPushButton(self.widget_2)
        self.pb_left.setObjectName(u"pb_left")
        self.pb_left.setMinimumSize(QSize(100, 100))
        self.pb_left.setFont(font)

        self.gridLayout.addWidget(self.pb_left, 1, 0, 1, 1)

        self.pb_up = QPushButton(self.widget_2)
        self.pb_up.setObjectName(u"pb_up")
        self.pb_up.setMinimumSize(QSize(100, 100))
        self.pb_up.setFont(font)

        self.gridLayout.addWidget(self.pb_up, 0, 0, 1, 1)

        self.pb_end = QPushButton(self.widget_2)
        self.pb_end.setObjectName(u"pb_end")
        self.pb_end.setMinimumSize(QSize(100, 100))
        self.pb_end.setFont(font)

        self.gridLayout.addWidget(self.pb_end, 2, 2, 1, 1)

        self.pb_action3 = QPushButton(self.widget_2)
        self.pb_action3.setObjectName(u"pb_action3")
        self.pb_action3.setMinimumSize(QSize(100, 100))
        self.pb_action3.setFont(font)

        self.gridLayout.addWidget(self.pb_action3, 5, 0, 1, 1)

        self.pb_nosignal = QPushButton(self.widget_2)
        self.pb_nosignal.setObjectName(u"pb_nosignal")
        self.pb_nosignal.setMinimumSize(QSize(100, 100))
        self.pb_nosignal.setFont(font)

        self.gridLayout.addWidget(self.pb_nosignal, 5, 2, 1, 1)

        self.pb_back = QPushButton(self.widget_2)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setMinimumSize(QSize(100, 100))
        self.pb_back.setFont(font)

        self.gridLayout.addWidget(self.pb_back, 3, 2, 1, 1)

        self.pb_action1 = QPushButton(self.widget_2)
        self.pb_action1.setObjectName(u"pb_action1")
        self.pb_action1.setMinimumSize(QSize(100, 100))
        self.pb_action1.setFont(font)

        self.gridLayout.addWidget(self.pb_action1, 4, 0, 1, 1)

        self.pb_action2 = QPushButton(self.widget_2)
        self.pb_action2.setObjectName(u"pb_action2")
        self.pb_action2.setMinimumSize(QSize(100, 100))
        self.pb_action2.setFont(font)

        self.gridLayout.addWidget(self.pb_action2, 4, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 917, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.open_video)

        self.retranslateUi(MainWindow)
        self.pb_up.clicked.connect(MainWindow.set_up)
        self.pb_left.clicked.connect(MainWindow.set_left)
        self.pb_start.clicked.connect(MainWindow.set_start)
        self.pb_down.clicked.connect(MainWindow.set_down)
        self.open_video.triggered.connect(MainWindow.openVideo)
        self.pb_pause.clicked.connect(MainWindow.set_pause)
        self.pb_action3.clicked.connect(MainWindow.set_action3)
        self.pb_nosignal.clicked.connect(MainWindow.set_nosignal)
        self.pb_back.clicked.connect(MainWindow.set_back)
        self.pb_right.clicked.connect(MainWindow.set_right)
        self.pb_end.clicked.connect(MainWindow.set_end)
        self.pb_action1.clicked.connect(MainWindow.set_action1)
        self.pb_action2.clicked.connect(MainWindow.set_action2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_video.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u89c6\u9891", None))
        self.pb_pause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pb_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b", None))
        self.pb_right.setText(QCoreApplication.translate("MainWindow", u"\u53f3", None))
        self.pb_left.setText(QCoreApplication.translate("MainWindow", u"\u5de6", None))
        self.pb_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a", None))
        self.pb_end.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.pb_action3.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c3", None))
        self.pb_nosignal.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u4fe1\u53f7", None))
        self.pb_back.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.pb_action1.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c1", None))
        self.pb_action2.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
    # retranslateUi

