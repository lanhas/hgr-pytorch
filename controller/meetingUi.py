# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 23))
        self.menubar.setObjectName("menubar")
        self.menuoperation = QtWidgets.QMenu(self.menubar)
        self.menuoperation.setObjectName("menuoperation")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionswitchCamera = QtWidgets.QAction(MainWindow)
        self.actionswitchCamera.setObjectName("actionswitchCamera")
        self.action_openDir = QtWidgets.QAction(MainWindow)
        self.action_openDir.setObjectName("action_openDir")
        self.action_openImg = QtWidgets.QAction(MainWindow)
        self.action_openImg.setObjectName("action_openImg")
        self.actiontorch = QtWidgets.QAction(MainWindow)
        self.actiontorch.setObjectName("actiontorch")
        self.actionrotate = QtWidgets.QAction(MainWindow)
        self.actionrotate.setObjectName("actionrotate")
        self.actionmove_left = QtWidgets.QAction(MainWindow)
        self.actionmove_left.setObjectName("actionmove_left")
        self.actionmove_right = QtWidgets.QAction(MainWindow)
        self.actionmove_right.setObjectName("actionmove_right")
        self.actionzoom = QtWidgets.QAction(MainWindow)
        self.actionzoom.setObjectName("actionzoom")
        self.actionexpension = QtWidgets.QAction(MainWindow)
        self.actionexpension.setObjectName("actionexpension")
        self.actioncapture = QtWidgets.QAction(MainWindow)
        self.actioncapture.setObjectName("actioncapture")
        self.actionback = QtWidgets.QAction(MainWindow)
        self.actionback.setObjectName("actionback")
        self.actionscreen_shot = QtWidgets.QAction(MainWindow)
        self.actionscreen_shot.setObjectName("actionscreen_shot")
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuoperation.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuoperation.setTitle(_translate("MainWindow", "??????"))
        self.menuFile.setTitle(_translate("MainWindow", "??????"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.actionswitchCamera.setText(_translate("MainWindow", "??????/???????????????"))
        self.action_openDir.setText(_translate("MainWindow", "???????????????"))
        self.action_openImg.setText(_translate("MainWindow", "????????????(*.pptx)"))
        self.actiontorch.setText(_translate("MainWindow", "??????"))
        self.actionrotate.setText(_translate("MainWindow", "????????????"))
        self.actionmove_left.setText(_translate("MainWindow", "?????????"))
        self.actionmove_right.setText(_translate("MainWindow", "?????????"))
        self.actionzoom.setText(_translate("MainWindow", "????????????"))
        self.actionexpension.setText(_translate("MainWindow", "????????????"))
        self.actioncapture.setText(_translate("MainWindow", "????????????"))
        self.actionback.setText(_translate("MainWindow", "??????"))
        self.actionscreen_shot.setText(_translate("MainWindow", "??????"))

