''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from memorycard.app import app 

btn_ans1 = QRadioButton("1")
btn_ans2 = QRadioButton("2")
btn_ans3 = QRadioButton("3")
btn_ans4 = QRadioButton("4")

RadioGroup= QButtonGroup()
RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

