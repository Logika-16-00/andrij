from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image, ImageFilter, ImageEnhance
import os

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = None
        self.workdir = None
        self.ui.btn_left.clicked.connect(self.rotate_left)
        self.ui.btn_right.clicked.connect(self.rotate_right)
        self.ui.btn_flip.clicked.connect(self.flip_image)
        self.ui.btn_bw.clicked.connect(self.bw_image)
        self.ui.btn_sharp.clicked.connect(self.sharpen_image)
        self.ui.btn_dir.clicked.connect(self.show_files)
        self.ui.listWidget.itemClicked.connect(self.show_pictures)

    def update_image(self, image=None):
        self.ui.label.hide()
        pixmap = QPixmap(image)
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pixmap.scaled(w, h)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()

    def rotate_left(self):
        self.image = self.image.rotate(90)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def rotate_right(self):
        self.image = self.image.rotate(-90)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def flip_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def bw_image(self):
        self.image = self.image.convert("L")
        self.image.save("copy.png")
        self.update_image("copy.png")

    def sharpen_image(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.image.save("copy.png")
        self.update_image("copy.png")

    def choose_dir(self):
        self.workdir = QFileDialog.getExistingDirectory(self)
        if not self.workdir:
            QMessageBox.warning(self, "Увага", "Директорію не вибрано!")

    def filter(self, files, ext):
        res = []
        for file in files:
            if any(file.lower().endswith(e.lower()) for e in ext):
                res.append(file)
        return res

    def show_files(self):
        ext = ["png", "jpg", "jpeg", "bmp", "gif"]
        self.choose_dir()
        if self.workdir:
            all_files = os.listdir(self.workdir)
            filter_files = self.filter(all_files, ext)
            self.ui.listWidget.clear()
            for file in filter_files:
                self.ui.listWidget.addItem(file)

    def show_pictures(self):
        #перевіряємо чи є картинки в списку
        if self.ui.listWidget.currentRow() != -1:
            #отримуємо назву картинки
            name = self.ui.listWidget.currentItem().text()
            #отримуємо шлях до картинки з директорі��
            path = os.path.join(self.workdir, name)
            #відкриваємо картинку з шляху
            self.image = Image.open(path)
            #виводимо картинку на екран
            self.update_image(path)

    def save_image(self):
        if self.image:
            save_path, _ = QFileDialog.getSaveFileName(
                self, "Зберегти файл", self.workdir, "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
            )
            if save_path:
                self.image.save(save_path)
                QMessageBox.information(self, "Успіх", "Зображення успішно збережено!")
            else:
                QMessageBox.warning(self, "Увага", "Файл для зображення не вибрано.")
        else:
            QMessageBox.warning(self, "Увага", "Немає зображення для збереження.")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
