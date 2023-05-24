import functools
import sys

from PyQt5 import uic, QtGui
from PyQt5.Qt import QObject, pyqtSignal, QEvent, QIcon, QSize
from PyQt5.QtWidgets import *
from jedi.plugins.stdlib import functools_partial
from qtawesome import icon

form_class = uic.loadUiType("my_omok03_19.ui")[0]


class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flagDol = True
        self.flagOver = False
        self.arr2d = [
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                                                                         
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                                                                         
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
                                                                         
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0, 0,  0, 0, 0, 0] 
        ]
        self.pbs = []
        self.bd = QIcon("1.png")
        self.wd = QIcon("2.png")
        self.nd = QIcon("0.png")
        
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d[i])):
                temp = QPushButton("", self)
                temp.setToolTip("{},{}".format(i, j))
                temp.setIcon(self.nd)
                temp.setIconSize(QSize(40, 40))
                temp.setGeometry(j * 40, 40 * i, 40, 40)
                temp.clicked.connect(self.myClick)
                self.pbs.append(temp)
        
        self.myRender()
        self.pbReset.clicked.connect(self.myReset)
        
    def myRender(self):
        size = len(self.arr2d)
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d[i])):
                if self.arr2d[i][j] == 0:
                    self.pbs[i * size + j].setIcon(self.nd)
                elif self.arr2d[i][j] == 1:
                    self.pbs[i * size + j].setIcon(self.bd)
                elif self.arr2d[i][j] == 2:
                    self.pbs[i * size + j].setIcon(self.wd)
    
    def checkUP(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDW(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRI(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRU(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLU(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRD(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLD(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if j < 0:
                    return cnt
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def myClick(self):
        if self.flagOver:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(',')
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] != 0:
            return
        
        stone = -1
        
        if self.flagDol:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
        
        up = self.checkUP(i, j, stone)
        dw = self.checkDW(i, j, stone)
        le = self.checkLE(i, j, stone)
        ri = self.checkRI(i, j, stone)
        ru = self.checkRU(i, j, stone)
        lu = self.checkLU(i, j, stone)
        rd = self.checkRD(i, j, stone)
        ld = self.checkLD(i, j, stone)
        
        logic1 = up + dw + 1
        logic2 = le + ri + 1
        logic3 = ru + ld + 1
        logic4 = lu + rd + 1
        
        self.myRender()
        
        if (logic1 == 5) or (logic2 == 5) or (logic3 == 5) or (logic4 == 5):
            self.flagOver = True
            if self.flagDol:
                QMessageBox.about(self, 'Win', "##  축하합니다  ##\n\n흑돌 승리~!!")
            else:
                QMessageBox.about(self, 'Win', "##  축하합니다  ##\n\n백돌 승리~!!")
            
        self.flagDol = not self.flagDol
        
        
    def myReset(self):
        self.flagOver = False
        self.flagDol = True
        for i in range(len(self.arr2d)):
            for j in range(len(self.arr2d[i])):
                self.arr2d[i][j] = 0

        self.myRender()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

