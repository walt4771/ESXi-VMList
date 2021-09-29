# VMWare ESXi VMList Viewer

- update json file via python 
	> If the login information is not saved in the json file, the login page appears.  
I recommend saving login information during login.
  > You have to update the json file manually.
I'm developing the update button on the web page.

- refresh react web

<br>
# Preview 

### vmList-updater preview  <br> ( on Ubuntu 20.04.3 ) 
![sshot](https://github.com/walt4771/ESXi-VMList_React/blob/main/preview-vmList-updater-v.210929.PNG)

### vmList-server_react preview  <br> ( Windows 10 LTSC 1809 )
![sshot](https://github.com/walt4771/ESXi-VMList_React/blob/main/preview-vmList-server_react.png)


# JSON File Structure
### LoginInfo.json

|Key						|Value
|---------------|------------------------------------
|`ip`						|ESX host ip (string)
|`isLoginInfoSaved`			|save login information (boolean)
|`id`						|ESX host id (string)
|`pw`						|ESX host pw (string)
|`jsonFile`					|location of `vmlist.json` (string)

### vmlist.json

|Key						|Value
|---------------|------------------------------------
|`VMID`			|ESX VM ID (string)
|`VMName`		|ESX VM Name (string)
|`isPoweredOn`	|is VM Powered on (string)

<br>
# Changelogs
### v.210929
- add window drag
- add window close button
- minor layout fix on Linux 
  > - `Server IP` section font size 11 -> 12
  > - all section height 30 -> 32

<br><br>
# References

[Powering on a virtual machine from command line](https://kb.vmware.com/s/article/1038043)
<br><br>
[React 기초 입문 프로젝트 – 흔하디 흔한 할 일 목록 만들기](https://velopert.com/3480)
<br><br>
[[React 리팩토링 #2] JSX에서 조건문 사용해 렌더링하기](https://velog.io/@hidaehyunlee/React-%EB%A6%AC%ED%8C%A9%ED%86%A0%EB%A7%81-2-JSX%EC%97%90%EC%84%9C-%EC%A1%B0%EA%B1%B4%EB%AC%B8-%EC%82%AC%EC%9A%A9%ED%95%B4-%EB%A0%8C%EB%8D%94%EB%A7%81%ED%95%98%EA%B8%B0)
<br><br>
[PyQt5 -- layout 관리 주의사항](https://freeprog.tistory.com/326)
