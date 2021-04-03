'''
    To control windows jump to each other
'''
from controller.windows import *

class Controller:
    def __init__(self):
        pass

    #To show the mainwindow
    def showMain(self):
        self.main = mainDecoration()
        self.main.setWindowTitle('手势识别及控制系统')
        self.main.switch_operate.connect(self.showOperate)
        self.main.show()
    
    def showOperate(self):
        self.operate = PictureOperation()
        self.operate.setWindowTitle('动态手势识别演示系统')
        self.operate.back_operate.connect(self.showMain)
        self.main.close()
        self.operate.show()
        self.operate.play_hands()

if __name__ == "__main__":
    con = Controller()


