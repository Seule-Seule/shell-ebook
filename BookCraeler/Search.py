#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
import csv
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from .Chapter import GetChapters

def SearchRequests(key = '道君'):
    
    param = {'keyword':key}
    SearchUrl = 'https://www.boquge.com/search.htm?'
    
    # 请求头 
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'
    }
    

    WhileEnd = 0
    while True:
        WhileEnd += 1
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
            continue
        
        if WhileEnd == 4:
            break

def SearchList(shtml):

    mlist = []
    slist = []

    Search_soup = BeautifulSoup(shtml,'lxml')
    for li in Search_soup('li',{'class':'list-group-item'}):
        mlist.append(li)

    index = 0
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
            BookUrl = '目录页链接'

          
        SearchOne = str(index) + ',' + str(name.string) + ',' + \
                    str(auother.string) + ','+ str(brand.string) + ','+ \
                    str(new.string) + ','+ BookUrl

        slist.append(SearchOne.split(","))

        index += 1

    return slist
        
def Get_Table(key,Search_Page):
    SearchHtml = SearchRequests(key = key)
    slist = SearchList(SearchHtml)
    
    slist_History = slist

    tb = PrettyTable()
    SearchNumber = 0
    for i in slist:
        if SearchNumber == 0:
            i[0] = '推荐'
            if Search_Page == 1:
                i[0] = '搜索'
            tb.field_names = i
            SearchNumber += 1
            continue

        tb.add_row(i)
        SearchNumber += 1
        if SearchNumber == 35:
            break
    if SearchNumber < 35:
        for i in slist_History:
            if i[0] == '推荐' or i[0] == '搜索':
                continue
            SearchNumber += 1
            i[0] = SearchNumber
            tb.add_row(i)
            if SearchNumber == 35:
                break
    return tb

def Get_Search_One(key,flag):
    number = 1
    SearchHtml = SearchRequests(key = key)
    slist = SearchList(SearchHtml)
    for i in slist:
        if (number -1 ) == flag:
            return i
        number += 1



def Search():

    if os.sep == '/':
        clean = 'clear'
    else:
        clean = 'cls'

    os.system(clean)

    Bar = ['[ Home ]','[ Search ]','','']                # Search Commend
    
    Print_Bar =  "\n" + "%s>%s>%s>%s"

    Print_Help = '\n\tNumber -> Enter recommendation. \
                  \n\t  q    -> Enter exit. \
                  \n\t'

    while True:


        while True:

            Bar[2] = ''
            Bar[3] = ''
            Default_Page = Get_Table('道君',0)
            os.system(clean)
            print(Default_Page)
            print(Print_Help)
            print(Print_Bar % (Bar[0],Bar[1],Bar[2],Bar[3]),end = '')            
            cmd = input()
            if cmd.isdigit():
                Choose = Get_Search_One('道君',int(cmd))
                GetChapters(Choose[5]) 
            elif cmd == 'q':
                return
            else:
                SearchKey = cmd
                Bar[2] = '[ ' + SearchKey + ' ]'
                break
         
        
        Chapter_number = 1
        Search_Table = Get_Table(SearchKey,1)

        os.system(clean)
        print(Search_Table)
        print(Print_Help)
        print(Print_Bar % (Bar[0],Bar[1],Bar[2],Bar[3]),end = '')
        while True:
            cmd = input()
            if cmd == 'q':
                break
            elif cmd.isdigit():
                Choose = Get_Search_One(SearchKey,int(cmd))
                GetChapters(Choose[5])



if __name__ == '__main__':

    Search()

