import paramiko
import time
import json

import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtWidgets
import res_image

esx_id = ""
esx_pw = ""
esx_ip = ""
saveinfo = False

# UI
form_class = uic.loadUiType("esxLoginForm.ui")[0]


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
        vmInfo = QtWidgets.QFileDialog.getOpenFileName(self, 'open file')
        vmInfo = vmInfo[0]

    def submitLogin(self):
        saveinfo = self.checkbox_saveinfo.isChecked()
        esx_ip = self.textedit_esx_ip.toPlainText()
        esx_id = self.textedit_esx_id.toPlainText()
        esx_pw = self.lineedit_esx_pw.text()
        print(esx_pw + esx_id + esx_ip)
        QMessageBox.about(self, "message", "login")
        QtCore.QCoreApplication.instance().quit()


# Login/SSH Logic
def getLoginInfo():
    with open('LoginInfo.json') as f:
        data = json.load(f)
    return data


def getVmList(jsonLocation):
    with open(jsonLocation) as f:
        data = json.load(f)
    return data


def connect_SSH(ip, id, pw, cmd):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    print(type(ip))
    cli.connect(hostname=ip, username=id, password=pw)
    # 세션
    channel = cli.invoke_shell()
    print("connected")
    # ->
    channel.send(cmd + "\n")
    time.sleep(1.0)
    # <-
    output = channel.recv(65535).decode("utf-8")
    cli.close()
    return output


def getVMState(id, ip, pw):
    connect_ssh_VMID = str(loginInfo.get('VMID'))
    print("vmstate")
    powerState = [0 for i in range(5)]
    for i in range(0, 5):
        cmd = vmInfo[i].get("VMID")
        powerState[i] = connect_SSH(
            ip,
            id,
            pw,
            "vim-cmd vmsvc/power.getstate " + cmd
        )
        if powerState[i].find('Powered on') == -1:
            powerState[i] = "Powered off"
        else:
            powerState[i] = "Powered on"
        vmInfo[i]['isPoweredOn'] = powerState[i]

        with open(loginInfo.get("jsonFile"), 'w', encoding='utf-8') as f:
            json.dump(vmInfo, f, indent="\t")


# Exec
# Init
loginInfo = getLoginInfo()
vmInfo = getVmList(loginInfo.get("jsonFile"))

print(loginInfo.get('isLoginInfoSaved'))
if loginInfo.get('isLoginInfoSaved') == "yes":
    getVMState(esx_ip, esx_id, esx_pw)
else:
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

    loginInfo["isLoginInfoSaved"] = 'yes'
    with open(loginInfo.get("jsonFile"), 'w', encoding='utf-8') as f:
        json.dump(vmInfo, f, indent="\t")
    getVMState(esx_ip, esx_id, esx_pw)
