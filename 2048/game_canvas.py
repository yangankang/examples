import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from number_rect import NumberRect


class GameCanvas(QLabel):
    # 只读的背景16个方格
    item_bgs = []
    # 背景16个方格的xy位置也是只读的
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

        self.setFocusPolicy(Qt.StrongFocus)
        self.set_item_bg()
        self.set_init_rect()

    def set_init_rect(self):
        self.random_rect_item()
        self.random_rect_item()

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
                ds.append({"Item": None, "Number": 0})
            self.item_bgs.append(bgs)
            self.item_bg_pos.append(pos)
            self.item_data.append(ds)

    def random_rect_item(self):
        zero_ds = []
        for i in range(0, 4):
            for j in range(0, 4):
                if self.item_data[i][j]["Number"] == 0:
                    zero_ds.append({"i": i, "j": j})

        if len(zero_ds) > 0:
            rnd = int(random.uniform(0, len(zero_ds)))
            k = int(random.uniform(0, 10))
            number = 2
            if k == 2 or k == 10:
                number = 4
            d = zero_ds[rnd]
            d["num"] = number
            d["x"] = self.item_bg_pos[d["i"]][d["j"]]["x"]
            d["y"] = self.item_bg_pos[d["i"]][d["j"]]["y"]

            rect = NumberRect(self.parent, self.rect_width, d)
            self.item_data[d["i"]][d["j"]]["Number"] = number
            self.item_data[d["i"]][d["j"]]["Item"] = rect
            rect.show()

            return self.item_data[d["i"]][d["j"]]
        return None

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Up:
            self.reset_rect(1)
        elif QKeyEvent.key() == Qt.Key_Down:
            self.reset_rect(2)
        elif QKeyEvent.key() == Qt.Key_Left:
            self.reset_rect(3)
        elif QKeyEvent.key() == Qt.Key_Right:
            self.reset_rect(4)

    def add_rect(self, i, j, k):
        print("")
        # if self.item_data[i][k]["Number"] == self.item_data[i][j]["Number"]:
        #     self.item_data[i][k]["Number"] = self.item_data[i][k]["Number"] + \
        #                                      self.item_data[i][j]["Number"]
        #     self.item_data[i][j]["Item"].destroy()
        #     self.item_data[i][j] = {"Item": None, "Number": 0}

    def reset_rect(self, direction):

        for i in range(0, 4):
            for j in range(0, 4):
                if direction == 3:
                    if self.item_data[i][j]["Number"] != 0:
                        if j != 0:
                            for k in range(0, j):
                                if self.item_data[i][k]["Number"] == 0:
                                    swap = self.item_data[i][k]
                                    self.item_data[i][k] = self.item_data[i][j]
                                    self.item_data[i][j] = swap
                                    break
                                else:
                                    self.add_rect(i, j, k)
                if direction == 4:
                    if self.item_data[i][3 - j]["Number"] != 0:
                        if 3 - j != 3:
                            for k in range(3, 3 - j, -1):
                                if self.item_data[i][k]["Number"] == 0:
                                    swap = self.item_data[i][k]
                                    self.item_data[i][k] = self.item_data[i][3 - j]
                                    self.item_data[i][3 - j] = swap
                                    break
                                else:
                                    self.add_rect(i, 3 - j, k)

                if direction == 1:
                    if self.item_data[j][i]["Number"] != 0:
                        if j != 0:
                            for k in range(0, j):
                                if self.item_data[k][i]["Number"] == 0:
                                    swap = self.item_data[k][i]
                                    self.item_data[k][i] = self.item_data[j][i]
                                    self.item_data[j][i] = swap
                                    break
                                else:
                                    self.add_rect(j, i, k)
                if direction == 2:
                    if self.item_data[3 - j][i]["Number"] != 0:
                        if 3 - j != 3:
                            for k in range(3, 3 - j, -1):
                                if self.item_data[k][i]["Number"] == 0:
                                    swap = self.item_data[k][i]
                                    self.item_data[k][i] = self.item_data[3 - j][i]
                                    self.item_data[3 - j][i] = swap
                                    break
                            else:
                                self.add_rect(3 - j, i, k)

        self.redraw_rect()
        self.random_rect_item()

    def redraw_rect(self):
        for i in range(0, 4):
            for j in range(0, 4):
                item = self.item_data[i][j]["Item"]
                if item:
                    x = self.item_bg_pos[i][j]["x"]
                    y = self.item_bg_pos[i][j]["y"]
                    ds = item.ds
                    ds["x"] = x
                    ds["y"] = y
                    item.refresh_ds(ds)
