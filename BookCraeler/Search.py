#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com


import requests
from bs4 import BeautifulSoup

def SearchRequests(key = '道君'):
    
    param = {'keyword':key}
    SearchUrl = 'https://www.boquge.com/search.htm?'
    
    # 请求头 
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }
    try:
        # 请求页面 
        r = requests.get(url = SearchUrl,params = param,timeout = 5,headers = headers)

        # 收集错误信息
        r.raise_for_status()

        # 修改text编码
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return ""

def SearchList(shtml):

    mlist = []
    slist = []

    Search_soup = BeautifulSoup(shtml,'lxml')
    for li in Search_soup('li',{'class':'list-group-item'}):
        mlist.append(li)

    for i in mlist[:-1]:
        s = BeautifulSoup(str(i),'lxml')
        brand = s.find('div',{'class':'col-xs-1'})
        name  = s.find('div',{'class':'col-xs-3'})
        new   = s.find('div',{'class':'col-xs-4'})
        auother = s.find('div',{'class':'col-xs-2'})
        try:
            BookUrl = s.a.get('href')
            
        except:
            BookUrl = '链接信息'

        SearchOne = str(name.string) + ',' + \
                          str(auother.string) + ','+ \
                          str(brand.string) + ','+ \
                          str(new.string) + ','+ \
                          BookUrl

        slist.append(SearchOne.split(","))

    return slist


def Search():
    while True:
        slist= []


        print("\t\t\t[搜索] \
              \n\t\t")
        SearchHtml = SearchRequests(key = SearchKey)
        slist = SearchList(SearchHtml)

if __name__ == '__main__':

    default = '道君'
    Search(default)

