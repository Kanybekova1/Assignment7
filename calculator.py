import os 
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow,QLineEdit, QPushButton
from model_calc import CalculatorModel


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 600)


        ui_path=os.path.join(os.path.dirname(__file__),'calc.ui')
        uic.loadUi(ui_path,self)

        self.calculator=CalculatorModel()

        self.button0.clicked.connect(lambda: self.on_button_click('0'))
        self.button1.clicked.connect(lambda: self.on_button_click('1'))
        self.button2.clicked.connect(lambda: self.on_button_click('2'))
        self.button3.clicked.connect(lambda: self.on_button_click('3'))
        self.button4.clicked.connect(lambda: self.on_button_click('4'))
        self.button5.clicked.connect(lambda: self.on_button_click('5'))
        self.button6.clicked.connect(lambda: self.on_button_click('6'))
        self.button7.clicked.connect(lambda: self.on_button_click('7'))
        self.button8.clicked.connect(lambda: self.on_button_click('8'))
        self.button9.clicked.connect(lambda: self.on_button_click('9'))

        self.button_plus.clicked.connect(lambda: self.on_button_click('+'))
        self.button_minus.clicked.connect(lambda: self.on_button_click('-'))
        self.button_multiply.clicked.connect(lambda: self.on_button_click('*'))
        self.button_divide.clicked.connect(lambda: self.on_button_click('/'))
        self.button_decimal.clicked.connect(lambda: self.on_button_click('.'))

        self.clear_btn.clicked.connect(self.on_button_clear)   
        self.button_back.clicked.connect(self.on_button_back)     
        self.equals_btn.clicked.connect(self.on_button_equal)   
        self.button_sign.clicked.connect(self.on_button_sign)  

    def on_button_click(self, char):
        self.calculator.add_to_expression(char)
        self.lineEdit.setText(self.calculator.get_expression())

    def on_button_equal(self):
        result = self.calculator.calculate()
        self.lineEdit.setText(result)

    def on_button_clear(self):
        self.calculator.clear_expression()
        self.lineEdit.clear()

    def on_button_back(self):
        self.calculator.remove_last_character()
        self.lineEdit.setText(self.calculator.get_expression())

    def on_button_sign(self):
        expr = self.calculator.get_expression()
        if expr and expr[0] == '-':
            self.calculator.expression = expr[1:]  
        else:
            self.calculator.expression = '-' + expr  
        self.lineEdit.setText(self.calculator.get_expression())