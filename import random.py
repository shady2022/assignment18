import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('sodoco.ui')

        self.game = [[None for i in range(9)]for j in range(9)]
        

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 20px')
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                
                self.game[i][j] = tb 
                
                self.ui.my_grid_2.addWidget(tb, i, j) 

        self.ui.show() 
        
        self.ui.btn_new_game.clicked.connect(self.new_game)
        self.ui.btn_check.clicked.connect(self.check_game)
        self.ui.checkbox.clicked.connect(self.Dark)
        self.ui.btn_reset.clicked.connect(self.Reset)


    def check_game(self):
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j  and self.game[row][i].text() != "":
                        self.game[row][i].setStyleSheet('font-size: 20px; color: blue; background-Color: pink')


        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != "":
                        self.game[i][col].setStyleSheet('font-size: 20px; color: blue; background-Color: pink')




        cel1=[]
        for i in range(0, 3):
            for j in range(0, 3):
                cel1.append(self.game[i][j].text())
        cel2=[]
        for i in range(0, 3):
            for j in range(3, 6):
                cel2.append(self.game[i][j].text())
        cel3=[]
        for i in range(0, 3):
            for j in range(6, 9):
                cel3.append(self.game[i][j].text())
        cel4=[]
        for i in range(3, 6):
            for j in range(0, 3):
                cel4.append(self.game[i][j].text())
        cel5=[]
        for i in range(3, 6):
            for j in range(3, 6):
                cel5.append(self.game[i][j].text())
        cel6=[]
        for i in range(3, 6):
            for j in range(6, 9):
                cel6.append(self.game[i][j].text())
        cel7=[]
        for i in range(6, 9):
            for j in range(0, 3):
                cel7.append(self.game[i][j].text())
        cel8=[]
        for i in range(6, 9):
            for j in range(3, 6):
                cel8.append(self.game[i][j].text())
        cel9=[]
        for i in range(6, 9):
            for j in range(6, 9):
                cel9.append(self.game[i][j].text())
        all_cel = [cel1,cel2,cel3,cel4,cel5,cel6,cel7,cel8,cel9]
        for i in range(9): # allcel count
            for j in range(9): # cell count
                for z in range(9):
                    if all_cel[i][j]==all_cel[i][z] and j!=z and all_cel[i][j]!='':
                        self.game[(int(i/3))*3+int(z/3)][(int(i%3))*3+(z%3)].setStyleSheet('font-size: 12; background-color: pink;')
                        flag=False

        for i in range(9): # check empty
            for j in range(9):
                if all_cel[i][j]=='':
                    flag=False
        if flag:
            msgBox = QMessageBox()
            msgBox.setText('Hooray! You did it! press New Game. ^^')
            msgBox.exec()
                
        

    def new_game(self):
        for i in range(9):
                for j in range(9):
                    self.game[i][j].setText('')
        r = random.randint(1, 6)
        file_path = f'data/s{r}.txt'
        
        f =open (file_path, 'r')
        big_text = f.read()

        
        rows = big_text.split('\n')

        for i in range(9):
            
            numbers = rows[i].split(" ")
            for j in range(9):
                if numbers[j] != '0':
                    self.game[i][j].setStyleSheet('font-size: 20px; color: blue ')
                    self.game[i][j].setText(numbers[j])
                  
                else:
                    self.game[i][j].setStyleSheet('font-size: 20px; color: red ')

    def Reset(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')


    def Dark(self):
        if self.ui.checkbox.isChecked():
            self.ui.setStyleSheet('background-color: black')
        else:
            self.ui.setStyleSheet('background-color: white')






app = QApplication([])
window = MainWindow()

app.exec_()

