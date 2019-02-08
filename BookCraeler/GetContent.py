#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import requests
from bs4 import BeautifulSoup


def ContentRequests(Contenturl):

    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }
    while True:
        try:
            # 请求页面
            r = requests.get(url = Contenturl,timeout = 5,headers = headers)
        
            # 收集错误信息
            r.raise_for_status()

            # 修改text编码 
            if r.encoding == 'ISO-8859-1':
                r.encoding = r.apparent_encoding 
            
            if r.status_code == 200:
                return r.text
        except:
            print('\n \t\t[页面请求错误，正在尝试重新请求 ！]')

def ContentText(html):
    clist = []
    html_soup  = BeautifulSoup(html,'lxml')
    for Content in html_soup.find('div',{'id':'txtContent'}).children:
        if type(Content) != type(html_soup.div): 
            clist.append(Content.string)
    
    return clist

def GetContent():
    while True:
        
        print('<<<' +  '-'*25 + '[ 内 容 ]' +  '-'*25  +  '>>>' \
             "\n \t\t [1] -> 输入内容URL链接 \
              \n \t\t [2] -> 退出内容查看 ")
        flag = input('\n \t\t[请输入功能键] >>>')
        if flag == '2':
            return

        url = input("\n \t\t[请输入内容链接] >>>")

        ContentList = []
        ContentHtml = ContentRequests(url)
        ContentList =  ContentText(ContentHtml)
        
        for i in ContentList:
            print(i)

if __name__ == '__main__':

    GetContent()

