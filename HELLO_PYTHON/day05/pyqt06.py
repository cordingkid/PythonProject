import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myClick)
        self.le1.returnPressed.connect(self.myClick)
        
    def myClick(self):
        a = self.le1.text()
        strr = ""
        res = ""
        if random()>0.5:
            strr = "홀"
        else:
            strr = "짝"
        self.le2.setText(strr)
        if a == strr:
            res = "승리"
        else:
            res = "패배"
        
        self.le3.setText(res)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    


