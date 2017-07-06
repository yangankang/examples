import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from game_canvas import GameCanvas
from number_rect import NumberRect


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.setWindowTitle("2048")
        self.resize(540, 540)

        self.set_main_canvas()

    def set_main_canvas(self):
        game = GameCanvas(self)


app = QApplication(sys.argv)
dialog = MainDialog()
dialog.show()

app.exec_()
