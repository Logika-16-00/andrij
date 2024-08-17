from PyQt5.QtWidgets import QLineEdit,QPushButton,QFormLayout,QListWidget,QWidget,QVBoxLayout,QHBoxLayout
line_correct = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")
line_ans = QLineEdit("")

form = QFormLayout()
form.addRow("ведіть запитання:", line_ans)
form.addRow("ведіть запитання:1", line_correct)
form.addRow("ведіть запитання:2", line_false1  )
form.addRow("ведіть запитання:3", line_false2)
form.addRow("ведіть запитання:4", line_false3)

list_q = QListWidget()

btn_add = QPushButton("додати запитання")
btn_clear = QPushButton("очистити")
btn_back = QPushButton("назад")

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)

main_menu_line = QHBoxLayout()

line1 = QVBoxLayout()
line1.addWidget(list_q)
line1.addWidget(btn_add)

line2 = QVBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(btn_clear)

line2.addWidget(btn_back, stretch = 2 )

main_menu_line = QHBoxLayout()
main_menu_line.addLayout(line1)
main_menu_line.addLayout(line2)


