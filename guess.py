import random
from PySide6.QtGui import QFont

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        
        self.ui = loader.load('6.ui', None)
        ta = QFont()
        self.setFont(QFont('Arial', 20))
        tb = QLineEdit()
        tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.textbox.setText('please enter your guess number:')
        self.ui.setWindowTitle('guesses GAME :')
        self.ui.btn_check.clicked.connect(self.ckeck)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_new.clicked.connect(self.Newgame)

        self.ui.show()

    def Newgame(self):
        self.random = random.randint (0, 500)
        
    def ckeck(self):
        my_entry = self.ui.lineEdit.text()
        if int(my_entry) == self.random:
             msgBox = QMessageBox()
             msgBox.setText('you are winer')
             msgBox.exec()
           

        elif int(my_entry) > self.random:
            self.ui.textbox.setText('plz guess  lower number')

        elif int(my_entry) > self.random:
            self.ui.textbox.setText('plz guess uper number')

    def reset(self):
        self.ui.textbox.setText('')



    
app = QApplication([])
window = MainWindow()

app.exec_()

