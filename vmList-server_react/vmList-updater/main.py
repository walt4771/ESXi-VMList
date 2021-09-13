# UI info
# json 파일 위치
# esx 로그인 정보, ip (저장또는 일회용)

# Logic
# Info o
# json 새로고침 o
# VMName, VMID o
# On/Off 정보 o
# 새로고침 웹상에서 대기 x

import paramiko
import time
import json


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
    cli.connect(ip, username=id, password=pw)
    # 새로운 interactive shell session 생성
    channel = cli.invoke_shell()
    # 명령 송신
    channel.send(cmd + "\n")
    time.sleep(1.0)
    # 결과 수신
    output = channel.recv(65535).decode("utf-8")
    cli.close()
    return output


# Init
loginInfo = getLoginInfo()
vmInfo = getVmList(loginInfo.get("jsonFile"))

# SSH
connect_SSH_ip = str(loginInfo.get('ip'))
connect_SSH_id = str(loginInfo.get('id'))
connect_SSH_pw = str(loginInfo.get('pw'))
connect_SSH_VMID = str(loginInfo.get('VMID'))

powerState = [0 for i in range(5)]
for i in range(0, 5):
    cmd = vmInfo[i].get("VMID")
    powerState[i] = connect_SSH(
        connect_SSH_ip,
        connect_SSH_id,
        connect_SSH_pw,
        "vim-cmd vmsvc/power.getstate " + cmd
    )
    if powerState[i].find('Powered on') == -1:
        powerState[i] = "Powered off"
    else:
        powerState[i] = "Powered on"
    vmInfo[i]['isPoweredOn'] = powerState[i]

    with open(loginInfo.get("jsonFile"), 'w', encoding='utf-8') as f:
        json.dump(vmInfo, f, indent="\t")
