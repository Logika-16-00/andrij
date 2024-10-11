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
        self.ui.btn_make.clicked.connect(self.add_notes)
        self.ui.list_1.itemClicked.connect(self.show_note)
        for note in notes.keys():
            self.ui.list_1.addItem(note)
        self.ui.btn_delet.clicked.connect(self.delete_notes)
        self.ui.btn_add.clicked.connect(self.add_tag)
        self.ui.btn_detach.clicked.connect(self.delete_tag)
            

    def add_notes(self):
        note_name,ok = QInputDialog.getText(self, "назву замітки","додати замітку")
        if ok and note_name != "":
            notes[note_name] = {"теги":[],"текст":""} 
            self.ui.list_1.addItem (note_name)
        self.write_to_file()

    def add_tag(self):
        if self.ui.list_1.currentItem():
            tag_name, ok = QInputDialog.getText(self,"Add Tag","Tag Name")
            note_name = self.ui.list_1.currentItem().text()
            if ok and tag_name!= "":
                if tag_name not in notes[note_name]["теги"]:
                    self.ui.list_2.addItem(tag_name)
                    notes[note_name]["теги"].append(tag_name)
                self.write_to_file()

    def delete_notes(self):
        self.ui.list_2.clear()
        self.ui.textEdit.clear()

        if self.ui.list_1.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()
        

    def delete_tag(self):
        if self.ui.list_1.currentItem() and self.ui.list_2.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            tag_name = self.ui.list_2.currentItem().text()
            self.ui.list_2.takeItem(self.ui.list_2.currentRow())
            notes[note_name]["теги"].remove(tag_name)
        self.write_to_file()


    def show_note(self,item):
       self.ui.list_2.clear()
       notes_name = item.text()
       if notes_name in notes:
           self.ui.list_2.addItems(notes[notes_name]["теги"])
           self.ui.textEdit.setText(notes[notes_name]["текст"])





    def write_to_file(self):
        with open("notes/notes.json","w",encoding="utf-8") as file:
            json.dump(notes,file, ensure_ascii=False,indent=4)



with open("notes/notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)
print("notes")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()