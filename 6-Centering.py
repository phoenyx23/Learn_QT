__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

This program centers a window
on the screen.

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
        self.resize(250, 250)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # Creates a QT Rectangle object with the same dimensions as this Widget
        cp = QtGui.QDesktopWidget().availableGeometry().center()  # Center Point of the screen
        qr.moveCenter(cp)  # moves the center or the Rectangle to the center of the screen
        self.move(qr.topLeft())  # move the top left of the Widget to the same location as the top left of the Rectangle


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
