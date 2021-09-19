import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtWidgets
import res_image

# UI
form_class = uic.loadUiType("esxLoginForm.ui")[0]
global vmInfo


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        window = QPalette()
        window.setColor(QPalette.Background, QColor(20, 20, 40))
        self.setAutoFillBackground(True)
        self.setPalette(window)
        self.setupUi(self)

    def selectJSONFile(self):
        global vmInfo
        vmInfo = QtWidgets.QFileDialog.getOpenFileName(self, 'open file')

    def submitLogin(self):
        QtCore.QCoreApplication.instance().quit()
        return self.textedit_esx_ip.toPlainText(), self.textedit_esx_id.toPlainText(), self.lineedit_esx_pw.text(), self.checkbox_saveinfo.isChecked(), vmInfo
