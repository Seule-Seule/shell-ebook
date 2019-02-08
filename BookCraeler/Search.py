#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
import csv
import requests
from bs4 import BeautifulSoup

def SearchRequests(key = '道君'):
    
    param = {'keyword':key}
    SearchUrl = 'https://www.boquge.com/search.htm?'
    
    # 请求头 
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }
    while True:
        try:
            # 请求页面 
            r = requests.get(url = SearchUrl,params = param,timeout = 5,headers = headers)

            # 收集错误信息
            r.raise_for_status()

            # 修改text编码
            if r.encoding == 'ISO-8859-1':
                r.encoding = r.apparent_encoding
        
            if r.status_code == 200:
                return r.text
        except:
            print('\n \t\t[页面请求错误，正在尝试重新请求 ！]')

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
            href = s.a.get('href')
            BookUrl = 'https://www.boquge.com/book/' + href[4:-10]

        except:
            BookUrl = '链接信息'


        SearchOne = str(name.string) + ',' + \
                          str(auother.string) + ','+ \
                          str(brand.string) + ','+ \
                          str(new.string) + ','+ \
                          BookUrl

        slist.append(SearchOne.split(","))

    return slist

def Displiay(string,length = 0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string, str):
        placeholder = u'  '
    else:
        placeholder = ' '
    while slen < length:
        re += placeholder
        slen += 1

    return re

def Search():
    path = os.getcwd() + os.sep + 'Search.csv'
    if os.path.isfile('Search.csv'):
        os.remove(path)

    while True:

        print('<<<' +  '-'*25 + '[ 搜 索 ]' +  '-'*25  +  '>>>' \
              "\n \t\t [1] -> 输入搜索作者/书名 \
              \n \t\t [2] -> 退出搜索 ")
        flag = input('\n \t\t[请输入功能键] >>>')
        if flag == '2':
            return 

        SearchKey = input("\n \t\t[请输入关键字] >>>")

        SearchHtml = SearchRequests(key = SearchKey)
        slist = SearchList(SearchHtml)
        
        SearchNumber = 0

        for i in slist:
            
            SearchNumber += 1
            print("|%-3s|%-s|%-s|%-s|%-s" 
                %(SearchNumber
                , Displiay(i[0],10) 
                , Displiay(i[1],8) 
                , Displiay(i[2],4)
                , Displiay(i[3],15)))
           

            with open(path,'a',newline='') as search:
                writer = csv.writer(search)
                writer.writerow(i[0].split('\n') \
                                + i[1].split('\n')  \
                                + i[2].split('\n') \
                                + i[3].split('\n') \
                                + i[4].split('\n') ) 
                
        print("\n \t\t共搜索到" + str(SearchNumber) + "条结果 ！\n\n")

if __name__ == '__main__':

    Search()

