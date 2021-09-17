import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setWindowTitle("Login Info Preferences")
        window = QPalette()
        window.setColor(QPalette.Background, QColor(20, 20, 40))
        self.setAutoFillBackground(True)
        self.setPalette(window)

        pixmap = QPixmap('vmware.ico').scaled(150, 150)
        imglabel = QLabel()
        imglabel.setPixmap(pixmap)

        self.labelId = QLabel("ID : ")
        self.labelPw = QLabel("PW : ")
        self.lineEditId = QLineEdit()
        self.lineEditPw = QLineEdit()
        self.loginBtn = QPushButton("Save")
        self.fileSelect = QPushButton("Select JSON")

        self.lineEditPw.setEchoMode(QLineEdit.Password)  # 비밀번호
        self.labelId.setStyleSheet("Color : white")  # 다크테마
        self.labelPw.setStyleSheet("Color : white")  # 다크테마

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(imglabel, 0, 1)

        layout.addWidget(self.labelId, 1, 0)
        layout.addWidget(self.lineEditId, 1, 1)

        layout.addWidget(self.labelPw, 2, 0)
        layout.addWidget(self.lineEditPw, 2, 1)

        layout.addWidget(self.fileSelect, 3, 1)
        layout.addWidget(self.loginBtn, 4, 1)

        self.fileSelect.clicked.connect(self.fileSelect, self.selectJSONFile())


        self.setGeometry(300, 300, 250, 300)

    def selectJSONFile(self):
        # global jsonfile
        # jsonfile = QtWidgets.QFileDialog.getOpenFileName(self, 'open file')
        # print(jsonfile)
        QMessageBox.about(self, "message", "select")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
