__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we dispay an image
on the window.

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
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('resources/redrock.jpg')

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 380, 270)
        self.setWindowTitle('Red Rock')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
