from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    
        self.image = Image.open("example.jpg")
        self.image.show()
        self.update_image()

    def updata_image(self):
        self.ui.label.hide()
        self.image.save("temp_image.jpg")
        pixmap = QPixmap("temp_image.jpg")
        w, h = self.ui.label.width(), self.ui.label.height()
        pixmap = pimap.scaled(h, w)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.show()

    
    
        

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()