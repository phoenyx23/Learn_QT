__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we create a skeleton
of a calculator using a QGridLayout.

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
        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel("this is a test"), 0, 0)
        btn1 = QtGui.QPushButton("Button 1")
        grid.addWidget(btn1, 1, 1)
        btn2 = QtGui.QPushButton("Button 2")
        grid.addWidget(btn2, 1, 2)
        self.setLayout(grid)
        self.move(300, 300)
        self.setWindowTitle('Grid test')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
