"""
This main module complex softwares for marked char from file jpg
start 20/11/2021
Author Gansior Alexandr mail - gansior@gansior.ru tel - +79173383804
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from Dialog import Ui_Main_Wind
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = QWidget()

    ui = Ui_Main_Wind()
    ui.setupUi(wnd)

    #QtCore.QObject.connect(ui.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)

    wnd.show()
    sys.exit(app.exec_())
    main_window()
