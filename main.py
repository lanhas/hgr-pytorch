import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from controller.controller import Controller


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.showMain()
    sys.exit(app.exec_())
