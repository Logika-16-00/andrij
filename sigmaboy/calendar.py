import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)

        url = QMediaContent(QUrl.fromLocalFile("sigmaboy.avi"))
        self.media.setMedia(url)
        self.media.play()

    def configure(self):
        ...

    def get_date(self):
        ...

    def media_play(self):
        ...

    def media_stop(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())