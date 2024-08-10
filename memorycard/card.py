from app import App
from PyQt5.QtWidgets import QRadioButton,QLabel,QSpinBox,QPushButton,QGroupBox,QHBoxLayout,QVBoxLayout,QButtonGroup
from PyQt5.QtCore import Qt


btn_sleep = QPushButton("Відпочити")
box_min = QSpinBox()
box_min.setValue(5)
lb_min = QLabel("Хвилини")
btn_menu = QPushButton("Меню")
btn_ans = QPushButton("Відповісти")
lb_ans = QLabel("Запитання")

btn_ans1= QRadioButton("1")
btn_ans2= QRadioButton("2")
btn_ans3= QRadioButton("3")
btn_ans4= QRadioButton("4")

AnswersGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()

RadioGroup.addButton(btn_ans1)
RadioGroup.addButton(btn_ans2)
RadioGroup.addButton(btn_ans3)
RadioGroup.addButton(btn_ans4)

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(1)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lb_min)

line_btn_ans1 = QVBoxLayout()
line_btn_ans2 = QVBoxLayout()

line_btn_ans1.addWidget(btn_ans1)
line_btn_ans1.addWidget(btn_ans2)
line_btn_ans2.addWidget(btn_ans3)
line_btn_ans2.addWidget(btn_ans4)


mainline_btn_ans=QHBoxLayout()
mainline_btn_ans.addLayout(line_btn_ans1)
mainline_btn_ans.addLayout(line_btn_ans2)

AnswersGroupBox.setLayout(mainline_btn_ans)

main_line = QVBoxLayout()
main_line.addLayout(line1)




ResGroupBox = QGroupBox("Результат")
lb_res = QLabel("Правильність")
lb_corect = QLabel("Правильна відповідь")
line_res = QVBoxLayout()
line_res.addWidget(lb_res)
line_res.addWidget(lb_corect)
ResGroupBox.setLayout(line_res)
main_line.addWidget(lb_ans)

main_line.addWidget(AnswersGroupBox,stretch = 8)
main_line.addWidget(ResGroupBox,stretch = 8)
ResGroupBox.hide()
main_line.addWidget(btn_ans)

def show_res():
    if btn_ans.text() == "Відповісти":
        AnswersGroupBox.hide()
        ResGroupBox.show()
        btn_ans.setText("Наступне питання")
def show_ans():
    AnswersGroupBox.show()
    ResGroupBox.hide()
    btn_ans.setText("Відповісти")
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
btn_ans.clicked.connect(show_res)