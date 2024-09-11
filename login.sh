#!/bin/bash

# 校园网的IP地址是10开头的，获取第一个匹配的IP
ip=$(ip a | grep "inet 10" | awk '{print $2}' | cut -d'/' -f1 | head -n 1)

username="xxxxxx"
passwd="xxxxxxx"
url="http://202.113.18.106:801/eportal/?c=ACSetting&a=Login&loginMethod=1&protocol=http%3A&hostname=202.113.18.106&port=&iTermType=1&wlanuserip=${ip}&wlanacip=null&wlanacname=jn1_&redirect=null&session=null&vlanid=0&mac=00-00-00-00-00-00&ip=${ip}&enAdvert=0&jsVersion=2.4.3&DDDDD=${username}&upass=${passwd}&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login="

echo "connect to"
echo "$url"

# 使用curl发出GET请求
curl -s "$url"
