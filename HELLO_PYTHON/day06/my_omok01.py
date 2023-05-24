import functools
import sys

from PyQt5 import uic, QtGui
from PyQt5.Qt import QObject, pyqtSignal, QEvent, QIcon, QSize
from PyQt5.QtWidgets import *
from jedi.plugins.stdlib import functools_partial
from qtawesome import icon

form_class = uic.loadUiType("my_omok01.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flagDol = True
        self.bd = QIcon("1.png")
        self.wd = QIcon("2.png")
        self.nd = QIcon("0.png")
        
        for i in range(10): 
            for j in range(10):
                temp = QPushButton("", self)
                temp.setIcon(self.nd)
                temp.setIconSize(QSize(40, 40))
                temp.setGeometry(j * 40, 40 * i, 40, 40)
                temp.clicked.connect(self.myClick)
        
    def myClick(self):
        if self.flagDol:
            self.sender().setIcon(self.bd)
        else:
            self.sender().setIcon(self.wd)
        
        self.flagDol = not self.flagDol
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

