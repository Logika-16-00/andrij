from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Визначення переможця')
bt = QPushButton("Згенерувати")
text = QLabel("Натисніть на кнопку")
winner = QLabel("?")
line = QVBoxLayout()
main_win.resize(300,200)
line.addWidget(text)
line.addWidget(winner)
line.addWidget(bt)
main_win.setLayout(line)
def show_winner():
    num_win = randint(1,100)
    winner.setText(str(num_win))
    text.setText("Переможець: ")
bt.clicked.connect(show_winner)
main_win.show()
app.exec_()