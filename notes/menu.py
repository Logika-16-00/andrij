from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from notes import Ui_MainWindow
import json


import json
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_notes)
        self.ui.list_1.itemClicked.connect(self.show_note)

    def add_notes(self):
        note_name,ok = QInputDialog.getText(self, "назву замітки","додати замітку")
        if ok and note_name != "":
            notes[note_name] = {"теги":[],"текст":""} 
            self.ui.list_addIteam (note_name)
        self.write_to_file()

    def add_tag(self):
        if self.ui.list_I.currentIteam():
            tag_name, ok = QInputDialog.getText(self,"Add Tag","Tag Name")
            note_name = self.ui.list_I.currentIteam().text()
            if ok and tag_name!= "":
                if tag_name not in notes[note_name]["text"]:
                    self.ui.list_I.currentIteam(tag_name)
                    notes[note_name]["text"].append(tag_name)
                self.write_to_file()

    def delete_notes(self):
        if self.ui.list_1.currentIteam():
            note_name = self.ui.list_1.currentIteam().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()
        

    def delete_tag(self):
        if self.ui.list_1.currentIteam():
            note_name = self.ui.list_1.currentIteam().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()
        

    # def show_note(self,item):
    #     self.ui.list_1.clear()
    #     self.ui.list_2.clear()
    #     self




    def write_to_file(self):
        with open("notes.json","w",encoding="utf-8") as file:
            json.dump(notes,file, ensure_ascii=False,indent=4)yhjopeyuk;jhiu



with open("notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)
print("notes")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()