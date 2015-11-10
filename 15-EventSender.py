__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

Testing of grid layout

author: Daniel Miller
"""

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # btn1 = QtGui.QPushButton("Button 1", self)
        # btn1.move(30, 50)
        # btn2 = QtGui.QPushButton("Button 2", self)
        # btn2.move(150, 50)
        grid = QtGui.QGridLayout()
        btn1 = QtGui.QPushButton("Button 1")
        btn2 = QtGui.QPushButton("Button 2")

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        grid.addWidget(btn1, 1, 1)
        grid.addWidget(btn2, 1, 2)
        grid.addWidget(QtGui.QLabel("This is a test"), 0, 0)

        # Because this is a QMainWindow we have to set a central Widget because Layouts only work on Widgets
        # They don't actually work on QMainWindows.
        self.statusBar()
        wid = QtGui.QWidget()
        wid.setLayout(grid)
        self.setCentralWidget(wid)

        # self.setGeometry(300, 300, 290, 150)
        self.move(300, 300)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
