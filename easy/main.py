from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PyQt5.QtWidgets import QFileDialog
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = None

        self.image = Image.open("images.jfif")
        self.update_image()
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_right.clicked.connect(self.rotate_right)
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_bw.clicked.connect(self.bw_image)
        self.ui.btn_sharp.clicked.connect(self.sharpen_image)


        self.ui.listWidget = i




    def update_image(self,image):
        self.ui.label.hide()
        if image:
            pixmap = QPixmap(image)
            self.image.save("pepe.jpg")
            pixmap = QPixmap("pepe.jpg")
            w,h =self.ui.label.width(),self.ui.label.height()
            pixmap = pixmap.scaled(w,h)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.show()

    
    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.update_image()

    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.update_image()

    def flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.update_image()

    def bw_image(self):
        self.image = self.image.convert('1')
        self.update_image()

    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)

    def choose_dir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory(self)

        print("workdir ") 

    
    def filter(self,files, ext):
        res = []
        for file in files:
            for e in ext:
                if file.endswith(e):
                    res.append(file)
        return res

    def show_fles(self):
        ext = ["png ", "jpg", "PNG","JPG" ]
        self.choose_dir()
        if workdir:
            all_fills = os.listdir(workdir)
            print(all_fills)
            filter_files = self.filter(all_fills, ext)
            print(filter_files)
            self.ui.listWidget.clear()
            for file in filter_files:
                self.ui.listWidget.addItem(file)

    def save_image(self):
        if self.image:
            save_part, = QFileDialog.getSaveFileName(self,"зберегти файл",workdir,"Images(*.png*jpeg*jpg.bmp*.gif)")
            if save_part:
                self.image.save(save_part)
                QMessageBox.information(self,"успіх","зображення успішно збережено")
            else:
                QMessageBox.information(self,"помилка","не вибрано місце збереження")
        else:
            QMessageBox.information(self,"Увага","Помилка зображення для зображення")

        



    

    

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()