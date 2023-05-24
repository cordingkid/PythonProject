import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myClick)
        self.le1.returnPressed.connect(self.myClick)
        
    def myClick(self):
        a= int(self.le1.text())
        strr = ""
        for i in range(1,9+1):
            strr += str(a)+" x "+ str(i) + " = "+str(a*i)+"\n"
        
        self.pte.setPlainText(strr)
           
       
       
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    


