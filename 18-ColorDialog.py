__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we select a colour value
from the QtGui.QColorDialog and change the background
colour of a QtGui.QFrame widget.

author: Jan Bodnar
website: zetcode.com
last edited: August 2011
"""

import sys
from PySide import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()
        col = QtGui.QColor(0, 0, 0)
        self.btn = QtGui.QPushButton('Dialog')
        # self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QtGui.QFrame()
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        grid.addWidget(self.btn, 0, 0)
        grid.addWidget(self.frm, 0, 1, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget {background-color: %s }" % col.name())


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
