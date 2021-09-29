import sys

from PyQt5.QtGui import QPalette, QColor, QCursor
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

    def exitUI(self):
        QtCore.QCoreApplication.instance().quit()
        return 0

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))  # Change mouse icon

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # Change window position
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))