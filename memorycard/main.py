from PyQt5.QtWidgets import QWidget
from card import*
from menu import*
from data import*

from app import App
win_card = QWidget()
win_menu = QWidget()

def set_card():
    win_card.resize(600,500)
    win_card.setWindowTitle("Memory Card")
    win_card.move(0,0)
    win_card.setLayout(main_line)

def set_menu():
    win_menu.resize(1000,500)
    win_menu.setWindowTitle("Memory Card")
    win_menu.move(0,0)
    win_menu.setLayout(main_menu_line)

def back_to_menu():
    win_card.hide()
    win_menu.show()

btn_menu.clicked.connect(back_to_menu)

set_card()
set_menu()
win_card.show()
App.exec_()