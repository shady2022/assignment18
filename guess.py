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
        self.lineedit.setFont(QFont('Arial', 20))
        tb = QLineEdit()
        tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.textbox.setText('please enter your guess number:')
        self.ui.setWindowTitle('guesses GAME :')
        self.ui.btn_check.clicked.connect(self.checknum)
        self.ui.btn_reset.clicked.connect(self.resetnum)

        self.ui.show()

    def guessnumber(self, r):
        self.ui.textbox.setText(self.ui.textbox.text()+ r)
        r = random.randint(0,500)


       
    def ckecknum(self):
        if self.guessnumber == 'r':
            msgBox = QMessageBox()
            msgBox.setText('you are winer')
            msgBox.exec()
            self.sign = 'check'

        elif self.guessnumber > 'r':
            self.ui.textbox.setText('plz guess  lower number')

        elif self.guessnumber < 'r':
            self.ui.textbox.setText('plz guess uper number')

    def resetnum(self):
        self.ui.textbox.setText('')



    
app = QApplication([])
window = MainWindow()

app.exec_()

