#!/usr/bin/env python
# encoding: utf-8
'''
@author: 尹田农
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ip_spiders.py
@time: 2019/1/31 10:46
@desc:
'''
import json
import uuid

def get_data_from_params(params):
    data = {}
    for line in params.split('\n'):
        data.update({line.split(':')[0].strip(): line.split(':')[1].strip()})
    return data

import scrapy
class ip_pool(scrapy.Spider):
    name = 'ip'
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
    #headers=get_data_from_params(headers)
    def start_requests(self):
        url='https://www.xicidaili.com/nn'
        yield scrapy.Request(url,headers=self.headers)
    def parse(self, response):
        ip=response.xpath('//tr[@class="odd"]/td[2]/text()').extract()
        port=response.xpath('//tr[@class="odd"]/td[3]/text()').extract()
        kind=response.xpath('//tr[@class="odd"]/td[6]/text()').extract()
        next=response.xpath('//a[@class="next_page"]/@href').extract()[0]
        url2='https://www.xicidaili.com'+next
        yield scrapy.Request(url=url2,headers=self.headers,callback=self.parse)
        for i in range(len(ip)):
            headers={''}
            url='http://httpbin.org/ip'
            proxy = kind[i].lower() + '://' + str(ip[i]) + ':' + str(port[i])
            meta={'proxy':proxy}
            yield scrapy.Request(url=url,meta=meta,callback=self.parse1,dont_filter=True)
    def parse1(self,response):
        dict1=json.loads(response.text)
        print(dict1['origin'],response.meta['proxy'],'--==============================================')