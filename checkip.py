#!/usr/bin/python3
#--*--coding:utf-8--*--

def check_ip(ipaddr):
    import sys
    addr=ipaddr.strip().split('.')  #切割IP地址为一个列表
    if len(addr) != 4:  #切割后列表必须有4个参数
        return False
    for i in range(4):
        try:
            addr[i]=int(addr[i])  #每个参数必须为数字，否则校验失败
        except:
            return False
        if addr[i]<=255 and addr[i]>=0:    #每个参数值必须在0-255之间
            pass
        else:
            return False
            i+=1
    else:
        return True
