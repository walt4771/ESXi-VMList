# SSH
import paramiko
import time
# JSON
import json
# UI
import sys
from PyQt5.QtWidgets import QApplication
import mainUI


def openJSONFile(file):
    with open(file, encoding='UTF8') as f:
        data = json.load(f)
    return data


def writeJSONFile(file, data, key: str, value: str):
    data[key] = value
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent="\t")


def getVMState(ip, id, pw, vminfofile):
    vmInfo = openJSONFile(vminfofile)
    powerState = [0 for i in range(5)]
    # SSH
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    for i in range(0, 5):
        cmd = vmInfo[i].get("VMID")
        cli.connect(ip, username=id, password=pw)
        # ->, <-
        stdin, stdout, stderr = cli.exec_command("vim-cmd vmsvc/power.getstate " + cmd)
        output = stdout.readlines()
        # print(''.join(output))
        if output[1].find('Powered on') == -1:
            powerState[i] = "Powered off"
        else:
            powerState[i] = "Powered on"
        cli.close()
    return powerState


loginjson = "LoginInfo.json"
ip = ''
id = ''
pw = ''
filelocation = ''
if not openJSONFile(loginjson)['isLoginInfoSaved']:
    app = QApplication(sys.argv)
    myWindow = mainUI.MyWindow()
    myWindow.show()
    app.exec_()
    a = myWindow.submitLogin()

    ip = a[0]
    id = a[1]
    pw = a[2]
    filelocation = a[4][0]

    if a[3]:  # save login info
        logininfo = openJSONFile(loginjson)
        writeJSONFile(loginjson, logininfo, "ip", a[0])
        writeJSONFile(loginjson, logininfo, "id", a[1])
        writeJSONFile(loginjson, logininfo, "pw", a[2])
        writeJSONFile(loginjson, logininfo, "jsonFile", a[4][0])  # vm파일경로
        writeJSONFile(loginjson, logininfo, "isLoginInfoSaved", True)
else:
    a = openJSONFile(loginjson)
    ip = a["ip"]
    id = a["id"]
    pw = a["pw"]
    filelocation = a["jsonFile"]

result = getVMState(ip, id, pw, filelocation)
target = openJSONFile(filelocation)
for i in range(0, 5):
    target[i]['isPoweredOn'] = result[i]
with open(filelocation, 'w', encoding='utf-8') as f:
    json.dump(target, f, indent="\t")

# writeJSONFile(file, data, key: str, value: str):
# openJSONFile(file)
