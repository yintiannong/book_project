# !/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ip_pool.py
@time: 2019/2/2 14:59
@desc:
'''
import json

import requests
from lxml import etree


class Ip_pool(object):
    num = 1
    def __init__(self):
        self.ip_list = []

    def get_ip(self):
        for i in range(100):
            try:
                url = 'https://www.xicidaili.com/nn/' + str(self.num)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
                content = requests.get(url=url, headers=headers)
                a = etree.HTML(content.text)
                print(a)
                ip0 = a.xpath('//tr[@class="odd"]/td[2]/text()')
                port = a.xpath('//tr[@class="odd"]/td[3]/text()')
                kind = a.xpath('//tr[@class="odd"]/td[6]/text()')
                print(ip0)
                for i in range(len(ip0)):
                    ip = {kind[i].lower(): ip0[i] + ':' + port[i]}
                    url1 = 'http://httpbin.org/ip'
                    content1 = requests.get(url=url1, headers=headers, proxies=ip)
                    dict1 = json.loads(content1.text)
                    ip1 = dict1['origin']
                    print(ip)
                    if ip1 == ip0[i]:
                        self.ip_list.append(ip1)
            except:
                pass
            self.num += 1
        return self.ip_list

ip=Ip_pool()
print(ip.get_ip())
