import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from game_calculate import GameCalculate
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

d = [
    [{'Item': None, 'Number': 0}, {'Item': None, 'Number': 0}, {'Item': None, 'Number': 0}, {'Item': None, 'Number': 0}],
    [{'Item': None, 'Number': 0}, {'Item': "A", 'Number': 16}, {'Item': None, 'Number': 0}, {'Item': None, 'Number': 0}],
    [{'Item': "A", 'Number': 8}, {'Item': "A", 'Number': 8}, {'Item': None, 'Number': 0}, {'Item': None, 'Number': 0}],
    [{'Item': "A", 'Number': 2}, {'Item': "A", 'Number': 2}, {'Item': "A", 'Number': 4}, {'Item': "A", 'Number': 2}]
]
c = GameCalculate(d)
c.calculate(4)
d = c.data
for d in d:
    print(d)

app.exec_()
