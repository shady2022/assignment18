import math 
import PySide6

from PySide6.QtWidgets import *
from functools import partial
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from math import *
from unit_converter.converter import converts


class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui.btn_covert.clicked.connect(self.convert)
        self.ui.comboBox_convert.currentTextChanged.connect(self.unit_change)

        self.ui.setWindowTitle('Microsoft Mathematics unit Converter')
        
        
        self.ui = loader.load('8.ui', None)
        self.ui.show()

    def unit_change(self):
        self.ui.from_groupBox.clear()
        self.ui.to_groupBox_2.clear()

        if self.ui.comboBox_convert.currentText() == 'Mass':
            self.ui.from_groupBox.addItems(['gr','kg','ton','pond'])
            self.ui.to_groupBox_2.addItems(['kg','gr','pond','ton'])

        elif self.ui.comboBox_convert.currentText() == 'Length':
            self.ui.from_groupBox.addItems(['cm','m','km','mm'])
            self.ui.to_groupBox_2.addItems(['m','cm','mm','km'])

        elif self.ui.comboBox_convert.currentText() == 'Temperture':
            self.ui.from_groupBox.addItems(['c','f','k'])
            self.ui.to_groupBox_2.addItems(['c','f','k'])


        elif self.ui.comboBox_convert.currentText() == 'Value':
            self.ui.from_groupBox.addItems(['bit','byte','kbyte','gbyte','tbyte'])
            self.ui.to_groupBox_2.addItems(['byte','bit','kbyte','tbyte','gbyte'])

    def convert(self):
     
        quantity = self.ui.input_textBox.text()
        current_unit = self.ui.fromUnit_comboBox.currentText()
        desired_unit = self.ui.toUnit_comboBox.currentText()
        result = converts(quantity=quantity+current_unit, desired_unit=desired_unit)
        self.ui.output_textBox.setText(str(round(float(result), 2)))

        
        
    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.new)
        self.fileMenu.addAction(self.open)
        self.fileMenu.addAction(self.save)
        self.fileMenu.addSeparator();
        self.fileMenu.addAction(self.exit)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.about)
        self.helpMenu.addAction(self.aboutQt)


app = QApplication([])
window = Converter()

app.exec()




  