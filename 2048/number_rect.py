import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class NumberRect(QLabel):
    animation = None

    color_dict = {"2": "#eee4da", "4": "#ede0c8", "8": "#f2b179", "16": "#f59563", "32": "#f67c5f",
                  "64": "#f65e3b", "128": "#edcf72", "256": "#edcc61", "512": "#EFCB52",
                  "1024": "#EFC739", "2048": "#EFC329", "4096": "#FF3C39"}

    font_color_dict = {"2": "#776e65", "4": "#776e65", "8": "#ffffff", "16": "#ffffff", "32": "#ffffff",
                       "64": "#ffffff", "128": "#ffffff", "256": "#776e65", "512": "#776e65",
                       "1024": "#776e65", "2048": "#776e65", "4096": "#ffffff"}

    def __init__(self, parent, width, ds):
        super(NumberRect, self).__init__(parent)
        self.ds = ds
        self.w = width

        self.resize(width, width)
        self.setFont(QFont("\"Clear Sans\", \"Helvetica Neue\", Arial, sans-serif", 55, QFont.Bold))
        self.setAlignment(Qt.AlignCenter)
        self.refresh_ds(ds)

    def refresh_ds(self, ds):
        self.ds = ds
        self.setText(str(ds["num"]))
        self.move(ds["x"], ds["y"])
        color = self.color_dict[str(ds["num"])]
        font_color = self.font_color_dict[str(ds["num"])]
        self.setStyleSheet("QLabel{background-color:" + color + ";color:" + font_color + ";border-radius:3}")

    def move_animation(self):
        self.animation = QPropertyAnimation(self, "pos".encode())
        self.animation.setDuration(150)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(300, 300))
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)

    def combine_animation(self):
        self.animation = QPropertyAnimation(self, "size".encode())
        self.animation.setDuration(150)
        self.animation.setStartValue(QSize(107, 107))
        self.animation.setEndValue(QSize(300, 300))
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.finished.connect(self.finish_com_anim)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)

    def finish_com_anim(self):
        self.animation = QPropertyAnimation(self, "size".encode())
        self.animation.setDuration(150)
        self.animation.setStartValue(QSize(300, 300))
        self.animation.setEndValue(QSize(107, 107))
        self.animation.setEasingCurve(QEasingCurve.Linear)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)
