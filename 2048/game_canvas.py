import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from number_rect import NumberRect


class GameCanvas(QLabel):
    item_bgs = []
    item_bg_pos = []
    item_data = []

    parent_x = 20
    parent_y = 20
    split_width = 16
    rect_width = 105

    def __init__(self, parent):
        super(GameCanvas, self).__init__(parent)
        self.parent = parent

        self.resize(500, 500)
        self.move(self.parent_x, self.parent_y)
        self.setStyleSheet("QLabel{background-color:#bbada0;color:#bbada0;border-radius:6}")

        self.set_item_bg()

        self.set_init_rect()

    def set_init_rect(self):
        d1 = self.random_number()
        d2 = self.random_number()
        rect1 = NumberRect(self.parent, self.rect_width, d1)
        rect2 = NumberRect(self.parent, self.rect_width, d2)

    def set_item_bg(self):
        for i in range(1, 5):
            bgs = []
            pos = []
            ds = []
            for j in range(1, 5):
                x = self.parent_x + self.split_width * j + self.rect_width * (j - 1)
                y = self.parent_y + self.split_width * i + self.rect_width * (i - 1)
                label = QLabel(self.parent)
                label.resize(self.rect_width, self.rect_width)
                label.move(x, y)
                label.setStyleSheet("QLabel{background-color:#cdc1b4;color:#cdc1b4;border-radius:3}")
                bgs.append(label)
                pos.append({"x": x, "y": y})
                ds.append(0)
            self.item_bgs.append(bgs)
            self.item_bg_pos.append(pos)
            self.item_data.append(ds)

    def random_number(self):
        zero_ds = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.item_data[i][j] == 0:
                    zero_ds.append({"i": i, "j": j})

        rnd = int(random.uniform(0, len(zero_ds)))
        k = int(random.uniform(0, 10))
        number = 2
        if k == 2 or k == 10:
            number = 4
        d = zero_ds[rnd]
        d["num"] = number
        d["x"] = self.item_bg_pos[d["i"]][d["j"]]["x"]
        d["y"] = self.item_bg_pos[d["i"]][d["j"]]["y"]

        self.item_data[d["i"]][d["j"]] = number

        return d
