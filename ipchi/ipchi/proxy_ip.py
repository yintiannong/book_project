#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: proxy_ip.py
@time: 2019/4/15 17:41
@desc:
'''
import requests as r
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

response=r.session().get('https://www.xicidaili.com/nn',headers=headers)
html=etree.HTML(response.text)
ip=html.xpath('//tr[@class="odd"]/td[2]/text()')
port=html.xpath('//tr[@class="odd"]/td[3]/text()')
kind=html.xpath('//tr[@class="odd"]/td[6]/text()')
for i in range(len(ip)):
    url = 'http://httpbin.org/ip'
    proxy = kind[i].lower() + '://' + str(ip[i]) + ':' + str(port[i])
    meta = {'proxy': proxy}
    response=etree.HTML(r.session().get(url,headers=headers,proxies=meta).text)
    print(response)

