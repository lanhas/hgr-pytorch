# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meetingUi.ui'
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
        MainWindow.resize(1147, 899)
        self.actionswitchCamera = QAction(MainWindow)
        self.actionswitchCamera.setObjectName(u"actionswitchCamera")
        self.action_openDir = QAction(MainWindow)
        self.action_openDir.setObjectName(u"action_openDir")
        self.action_openImg = QAction(MainWindow)
        self.action_openImg.setObjectName(u"action_openImg")
        self.actiontorch = QAction(MainWindow)
        self.actiontorch.setObjectName(u"actiontorch")
        self.actionrotate = QAction(MainWindow)
        self.actionrotate.setObjectName(u"actionrotate")
        self.actionmove_left = QAction(MainWindow)
        self.actionmove_left.setObjectName(u"actionmove_left")
        self.actionmove_right = QAction(MainWindow)
        self.actionmove_right.setObjectName(u"actionmove_right")
        self.actionzoom = QAction(MainWindow)
        self.actionzoom.setObjectName(u"actionzoom")
        self.actionexpension = QAction(MainWindow)
        self.actionexpension.setObjectName(u"actionexpension")
        self.actioncapture = QAction(MainWindow)
        self.actioncapture.setObjectName(u"actioncapture")
        self.actionback = QAction(MainWindow)
        self.actionback.setObjectName(u"actionback")
        self.actionscreen_shot = QAction(MainWindow)
        self.actionscreen_shot.setObjectName(u"actionscreen_shot")
        self.actionconvert = QAction(MainWindow)
        self.actionconvert.setObjectName(u"actionconvert")
        self.actiondocuments = QAction(MainWindow)
        self.actiondocuments.setObjectName(u"actiondocuments")
        self.actionreleaseNote = QAction(MainWindow)
        self.actionreleaseNote.setObjectName(u"actionreleaseNote")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_3.addWidget(self.graphicsView)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1147, 23))
        self.menuoperation = QMenu(self.menubar)
        self.menuoperation.setObjectName(u"menuoperation")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuoperation.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menuoperation.addAction(self.actionswitchCamera)
        self.menuoperation.addAction(self.actiontorch)
        self.menuoperation.addAction(self.actionrotate)
        self.menuoperation.addAction(self.actionmove_left)
        self.menuoperation.addAction(self.actionmove_right)
        self.menuoperation.addAction(self.actionzoom)
        self.menuoperation.addAction(self.actionexpension)
        self.menuoperation.addAction(self.actioncapture)
        self.menuoperation.addAction(self.actionback)
        self.menuoperation.addAction(self.actionscreen_shot)
        self.menuFile.addAction(self.action_openImg)
        self.menuFile.addAction(self.action_openDir)
        self.menuFile.addAction(self.actionconvert)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actiondocuments)
        self.menu_2.addAction(self.actionreleaseNote)
        self.menu_2.addAction(self.actionabout)

        self.retranslateUi(MainWindow)
        self.action_openDir.triggered.connect(MainWindow.openDir)
        self.action_openImg.triggered.connect(MainWindow.openImg)
        self.actiontorch.triggered.connect(MainWindow.torch)
        self.actionrotate.triggered.connect(MainWindow.rotate)
        self.actionmove_left.triggered.connect(MainWindow.move_left)
        self.actionzoom.triggered.connect(MainWindow.zoom)
        self.actioncapture.triggered.connect(MainWindow.capture)
        self.actionback.triggered.connect(MainWindow.back)
        self.actionexpension.triggered.connect(MainWindow.expension)
        self.actionmove_right.triggered.connect(MainWindow.move_right)
        self.actionscreen_shot.triggered.connect(MainWindow.screen_shot)
        self.actionswitchCamera.triggered.connect(MainWindow.switch_camera)
        self.actionconvert.triggered.connect(MainWindow.convert_form)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionswitchCamera.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a/\u9690\u85cf\u6444\u50cf\u5934", None))
        self.action_openDir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.action_openImg.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\uff08.pptx\uff09", None))
        self.actiontorch.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.actionrotate.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u5185\u5bb9", None))
        self.actionmove_left.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.actionmove_right.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.actionzoom.setText(QCoreApplication.translate("MainWindow", u"\u7f29\u5c0f\u5185\u5bb9", None))
        self.actionexpension.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5927\u5185\u5bb9", None))
        self.actioncapture.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u5185\u5bb9", None))
        self.actionback.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.actionscreen_shot.setText(QCoreApplication.translate("MainWindow", u"\u622a\u5c4f", None))
        self.actionconvert.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.actiondocuments.setText(QCoreApplication.translate("MainWindow", u"\u6587\u6863", None))
        self.actionreleaseNote.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u7b14\u8bb0", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menuoperation.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

