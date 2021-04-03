import cv2
import sys
import time
import numpy as np
from PIL import ImageGrab
from pathlib import Path
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from controller.mainUi import Ui_MainWindow as mainWindow
from controller.playerUi import Ui_MainWindow as operateWindow
from pred.play_hands_results import Player
from PyQt5.QtCore import pyqtSignal,Qt


class MyMainWindow(QtWidgets.QMainWindow):
    back_operate = pyqtSignal()
    """对QDialog类重写，实现一些功能"""

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出界面？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        self.back_operate.emit()


class mainDecoration(QMainWindow, mainWindow):
    switch_operate = pyqtSignal()
    def __init__(self, parent=None):
        super(mainDecoration, self).__init__(parent)  
        self.setupUi(self)

    '''
        槽函数:作用为信号函数传递信号之后所进行的操作
    '''

    def play(self):
        self.switch_operate.emit()

    # open the image folder
    def openimg(self):
        imgDir = QFileDialog.getExistingDirectory(self,
                  "选取文件夹",
                  str(Path.home()))
        self.imgs = Path(imgDir).iterdir()
        for i, v in enumerate(self.imgs):
            print(v)

    # open the carema
    def test(self):
        pl = Player()
        pl.play_custom_video(None)


class PictureOperation(MyMainWindow, operateWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PictureOperation, self).__init__(parent)
        self.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)
        self.screenImg_dir = Path.home() / 'MgrScreenImg'
        self.screenImg_dir.mkdir(parents=True, exist_ok=True)
        self.imgs_path = []
        self.zoomscale = 1
        # self.updateImg()
        self.count_now = 0
        self.img=cv2.imread("controller/bianmu.png")                                      #读取图像
        # self.updateImg()
       
    def play_hands(self):
        self.hands_player = Player()
        self.hands_player.hands_singal.connect(self.hands_controller)
        self.hands_player.show_camera = False
        self.hands_player.play_custom_video(None)

    def updateImg(self):
        img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)                #转换图像通道
        x = img.shape[1]                                                        #获取图像大小
        y = img.shape[0]
        # self.zoomscale=scale_zoom                                                      #图片放缩尺度
        frame = QImage(img, x, y,x*3,QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item=QGraphicsPixmapItem(pix)                              #创建像素图元
        self.item.setScale(self.zoomscale)
        self.scene=QGraphicsScene()                                       #创建场景
        self.scene.addItem(self.item)
        self.graphicsView.setScene(self.scene)                                #将场景添加至视图

    def openImg(self):
        pass
    
    def hands_controller(self, hands):
        print(hands)
        if hands == 1:
            pass
        elif hands == 2:
            self.rotate()
        elif hands == 3:
            self.move_left()
        elif hands == 4:
            self.move_right()
        elif hands == 5:
            self.zoom()
        elif hands == 6:
            self.expension()
        elif hands == 7:
            pass
        elif hands == 8:
            self.back()
        elif hands == 9:
            self.screen_shot()

    def switch_camera(self):
        if self.hands_player.show_camera == False:
            self.hands_player.show_camera = True
        else:
            self.hands_player.show_camera = False

    def openDir(self):
        self.hands_player.show_camera = False
        imgDir = QFileDialog.getExistingDirectory(self,
                  "选取文件夹",
                  str(Path.home() / 'Pictures'))
        files = Path(imgDir).iterdir()
        for i,v in enumerate(files):
            self.imgs_path.append(str(v))
        self.img = cv2.imread(self.imgs_path[0])
        self.updateImg()

 
    def torch(self):
        pass

    def rotate(self):
        self.img = cv2.transpose(self.img)
        self.img = cv2.flip(self.img, 0)
        self.updateImg()
    
    def move_left(self):
        if self.count_now > 0:
            self.count_now -=1
        self.img = cv2.imread(self.imgs_path[self.count_now])
        print(self.count_now)
        self.updateImg()
    
    def move_right(self):
        if self.count_now < len(self.imgs_path) - 1:
            self.count_now +=1
        self.img = cv2.imread(self.imgs_path[self.count_now])
        print(self.count_now)
        self.updateImg()
    
    def zoom(self):
        self.zoomscale=self.zoomscale-0.2
        if self.zoomscale<=0:
           self.zoomscale=0.2
        self.updateImg()
    
    def expension(self):
        self.zoomscale=self.zoomscale+0.2
        if self.zoomscale>=1.8:
            self.zoomscale=1.8
        self.updateImg()
    
    def capture(self):
        pass
    
    def back(self):
        cv2.destroyAllWindows()

    def screen_shot(self):
        screenImg = ImageGrab.grab()
        time_now = time.strftime("%Y%m%d-%H:%M", time.localtime())
        screen_path = str(self.screenImg_dir / Path(str(time_now).split(':')[0] + '-' + str(time_now).split(':')[1] + '.jpg'))
        screenImg.save(screen_path)
        temp_img = cv2.imread(screen_path)
        cv2.imshow('screen_shot', temp_img)
        # screenImg.show()
        
