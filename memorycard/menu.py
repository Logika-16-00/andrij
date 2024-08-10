from PyQt5.QtWidgets import QLineEdit,QPushButton
line_ans = QLineEdit("")
line_correct = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")

form = QFormLayout()
form.addRow("ведіть запитання:", line_ans)
form.addRow("ведіть запитання:1", line_correct)
form.addRow("ведіть запитання:2", line_false1  )
form.addRow("ведіть запитання:3", line_false2)
form.addRow("ведіть запитання:4", line_false3)

list_q = QListView()

btn_add = QPushButton("додати запитання")
btn_clear = QPushButton("очистити")
btn_back = QPushButton("назат")

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)
line1 =QVBoxLayout("")
line2 =QVBoxLayout("")
line3 =QVBoxLayout("")
line4 =QVBoxLayout("")
main_menu_line = QHBoxLayout()

line1 = QHBoxLayout()
line1.addWidget(list_q)
line1.addWidget(btn_add)

line2 = QHBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(btn_clear)

line4 = QHBoxLayout()
line4.addWidget(btn_back, stretch = 2 )

main_menu_line = QHBoxLayout()
main_menu_line.addLayout(line3)
main_menu_line.addLayout(line4)


