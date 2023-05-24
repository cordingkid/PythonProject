import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt11.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.strr = ""
        
        self.setRnd()
        
        self.pb.clicked.connect(self.myClick)
        self.le1.returnPressed.connect(self.myClick)
        
    def setRnd(self):
        arr = list(range(1, 9 + 1))
        print(arr)
        for i in range(100):
            rnd = int(random() * 9)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
        
        for i in range(0, 3):
            self.strr += str(arr[i])
            
        print(self.strr)
        
    def myClick(self):
        mine = self.le1.text();
        
        s = 0
        b = 0
        
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = self.strr[0:1]
        c2 = self.strr[1:2]
        c3 = self.strr[2:3]
        
        if m1 == c1:
            s += 1
        if m2 == c2:
            s += 1
        if m3 == c3:
            s += 1
        
        if (c1 == m2) or (c1 == m3):
            b += 1
        if (c2 == m1) or (c2 == m3):
            b += 1
        if (c3 == m2) or (c3 == m1):
            b += 1
        
        ptestr = mine + "\t{}S {}B ".format(s, b)
        self.le1.setText("")
        self.pte.appendPlainText(ptestr)
        
        if s == 3: 
            QMessageBox.about(self, 'Win', "컴퓨터 숫자 " + self.strr + "\n 너가 이겻어")
            sys.exit(0)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

