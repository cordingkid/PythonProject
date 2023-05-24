import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myClick)
        self.le1.returnPressed.connect(self.myClick)
        
        
    def mylogic(self,a,b):
        str = "";
        for i in range(a,b+1):
            for j in range(0,i):
                str += "★"
            str += "\n"
        return str
    
    def myClick(self):
        a= int(self.le1.text())
        b= int(self.le2.text())
        self.te.setPlainText(self.mylogic(a,b))
       
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    


