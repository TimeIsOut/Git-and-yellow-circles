import sys
from random import randint
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 380)
        self.push = QtWidgets.QPushButton(Form)
        self.push.setGeometry(QtCore.QRect(160, 330, 181, 31))
        self.push.setObjectName("push")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.push.setText(_translate("Form", "Нажимай"))


class YellowCircles(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r1, r2, r3 = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QtGui.QColor(r1, r2, r3))
        center = (250, 190)
        random = randint(1, 100)
        qp.drawEllipse(center[0] - random, center[1] - random, 2 * random, 2 * random)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = YellowCircles()
    w.show()
    sys.exit(app.exec())