# NKU_WLAN 登录脚本
旨在使用脚本一键登录南开大学校园网`NKU_WLAN`。

## 使用方法
首先，将脚本之中的 `username` 和 `passwd`变量改为自己的学号、密码，比如
```
username = '123456'
passwd = 'qwerty'
```
### 有 Python 环境
最新的 Linux 系统默认带有python环境，windows系统需要自行安装 Python
#### 对于 Linux 系统的PC或笔记本：
```shell
python3 login.py
```
#### 对于 windows 系统的PC或者笔记本
```shell
python login-windows.py
```
### 无 Python 环境
注意，此类脚本未经过严格测试，如有问题请询问ChatGPT修改。
#### 对于 windows 系统的PC或者笔记本
```shell
# 请先赋予权限，比如：
# chmod +x ./login.sh
# 然后
./login.sh
```
#### 对于 windows 系统的PC或者笔记本
```shell
# 在cmd之中
login.bat
```
## 其他网络
对于其他校园中的网络，原理类似，请自行使用 Wireshark 或者 BurpSuite 等软件抓包后仿照写出脚本。