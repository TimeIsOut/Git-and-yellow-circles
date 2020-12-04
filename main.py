import sys
from random import randint
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class YellowCircles(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.push.clicked.connect(self.go)
        self.do_paint = False

    def go(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QtGui.QColor(255, 255, 0))
        center = (250, 190)
        random = randint(1, 100)
        qp.drawEllipse(center[0] - random, center[1] - random, 2 * random, 2 * random)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = YellowCircles()
    w.show()
    sys.exit(app.exec())