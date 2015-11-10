__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we create three toggle buttons.
They will control the background color of a
QtGui.QFrame.

author: Jan Bodnar
website: zetcode.com
last edited: August 2011
"""

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.col = QtGui.QColor(0, 0, 0)
        grid = QtGui.QGridLayout()

        redb = QtGui.QPushButton('Red')
        redb.setCheckable(True)
        grid.addWidget(redb, 0, 0)
        redb.clicked[bool].connect(self.setColor)

        greenb = QtGui.QPushButton('Green')
        greenb.setCheckable(True)
        grid.addWidget(greenb, 1, 0)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QtGui.QPushButton('Blue')
        blueb.setCheckable(True)
        grid.addWidget(blueb, 2, 0)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame()
        grid.addWidget(self.square, 0, 1, 3, 1)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        self.setLayout(grid)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
