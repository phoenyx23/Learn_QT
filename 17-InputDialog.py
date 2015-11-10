__author__ = 'Phoenyx'
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we receive data from
a QtGui.QInputDialog dialog.

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
        # self.btn = QtGui.QPushButton('Dialog', self)
        self.btn = QtGui.QPushButton('Dialog')
        # self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        # self.le = QtGui.QLineEdit(self)
        self.le = QtGui.QLineEdit()
        # self.le.move(130, 22)
        grid.addWidget(self.btn, 0, 0)
        grid.addWidget(self.le, 0, 1)
        self.setLayout(grid)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def showDialog(self):
        # QInputDialog.getText returns (text, bool) tuple
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

