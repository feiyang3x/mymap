#!/usr/bin/python3
#--*--coding:utf-8--*--

import urllib
import urllib.request
import json
import os
import re
import webbrowser
import sys
import argparse
import checkip

api_ip = 'http://api.map.baidu.com/location/ip?'
api_static = 'http://api.map.baidu.com/staticimage/v2?'
ak = 'ak=B66dd1027d70bd9a0cd3dfca610bcdac&'
coor = 'coor=bd09ll'

def test(argv):
    if len(sys.argv) == 1:
        arg_ip = api_ip + ak + coor
        get_addr(arg_ip)
    elif (checkip.check_ip(sys.argv[1]) == True):
        ip_v4 = 'ip='+sys.argv[1]+'&'
        arg_ip = api_ip + ip_v4 + ak + coor
        get_addr(arg_ip)
    else:
        print(sys.argv[0] + ' usage:')
        print(sys.argv[0] + ': 将定位本计算机位置')
        print(sys.argv[0] + ' IP: 将定位指定IP的位置')

def get_addr(arg_ip):
    
    try:
        r_data = urllib.request.urlopen(arg_ip).read()

        data=eval(r_data)
        print(data['address'])
        print(data['content']['address'])
        print(data['content']['address_detail']['city'])
        print(data['content']['address_detail']['city_code'])
        print(data['content']['address_detail']['district'])
        print(data['content']['address_detail']['province'])
        print(data['content']['address_detail']['street'])
        print(data['content']['address_detail']['street_number'])
        print(data['content']['point']['x'])
        print(data['content']['point']['y'])
        print(data['status'])

        center = 'center=' + data['content']['point']['x'] + ',' + data['content']['point']['y'] + '&'
        markers = 'markers=' + data['content']['point']['x'] + ',' + data['content']['point']['y'] + '&'
        arg_static = api_static + ak + center + '&width=300&height=200&zoom=18'

        fp = open('mymap.html', 'r+', encoding='UTF-8')
        open('distmap.html', 'w', encoding='UTF-8').write(re.sub(r'center=\d{3}.\d{8},\d{2}.\d{8}\&markers=\d{3}.\d{8},\d{2}.\d{8}\&', center + markers, fp.read()))

        webbrowser.open('distmap.html')
    except:
        print('定位失败')

if __name__ == '__main__':
    test(sys.argv)
