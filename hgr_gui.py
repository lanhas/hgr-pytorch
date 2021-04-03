import cv2
import sys 
from controller.windows import mainDecoration, PictureOperation
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from controller.controller import Controller

    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # default is to show the main window
    controller = Controller()
    controller.showMain()

    sys.exit(app.exec_())