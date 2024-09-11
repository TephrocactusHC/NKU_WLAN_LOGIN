#!/usr/bin/env python
# coding=utf-8
import requests
import os
import re

if __name__ == '__main__':
    # 校园网的ip地址是10开头的
    line = os.popen('ip a | grep "inet 10"').readline()
    base = line.find('10.')
    line = line[base:]
    ip = re.search('10\.\d+\.\d+\.\d+', line).group()
    username = 'xxxxxx'
    passwd = 'xxxxxxx'
    url = "http://202.113.18.106:801/eportal/?c=ACSetting&a=Login&loginMethod=1&protocol=http%3A&hostname=202.113.18.106&port=&iTermType=1&wlanuserip={0}&wlanacip=null&wlanacname=jn1_&redirect=null&session=null&vlanid=0&mac=00-00-00-00-00-00&ip={0}&enAdvert=0&jsVersion=2.4.3&DDDDD={1}&upass={2}&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=".format(ip, username, passwd)
    print('connect to \n', url)
    requests.get(url=url)
