#!/usr/bin/env python3
# coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os 
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from .GetContent import GetContent 


def ChaptersRequsts(ChapterUrl):
    
    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'    
    
    }

    WhileEnd = 0
    while True:
        WhileEnd += 1
        try:
            # 请求页面
            r = requests.get(url = ChapterUrl,timeout = 5,headers = headers)
                         
            # 收集错误信息
            r.raise_for_status()
            
            # 修改text编码
            if r.encoding == 'ISO-8859-1':
                r.encoding = r.apparent_encoding

            # 检查页面请求是否成功
            if r.status_code == 200:
                return r.text
        except:
            continue 
        
        if WhileEnd == 4:
            break

def ChapterList(html):
    # 获取目录URL信息
    html_soup = BeautifulSoup(html,"lxml")
    ulist = list(html_soup.find('ul',{'id':'chapters-list'}))
    # 目录URl信息写入 ChaptersList.csv 文件
    ChapterList2 = []
    Chapter_N = 1
    for info in ulist[2:-1]:
        info_soup = BeautifulSoup(str(info),'lxml')
        chapter_name = info_soup.a.string
        chapter_url  = 'https://www.boquge.com' + info_soup.a.get('href')
        ChapterList2.append(str(Chapter_N).split(',') + chapter_name.split(",") + chapter_url.split(","))
        Chapter_N += 1
    return ChapterList2

def GetTable(url):
    objecthtml = ChaptersRequsts(url)
    urllist =  ChapterList(objecthtml)

    tb = PrettyTable()
    ChapterNumber = 1
    for i in urllist:
        if ChapterNumber == 1:
            tb.field_names = ['序号','章节名称','章节链接']
        tb.add_row(i)
        ChapterNumber += 1
        if ChapterNumber == 31:
            break

    return tb

def Ge_CHapter_One(url,flag):
    number = 1
    objecthtml = ChaptersRequsts(url)
    urllist =  ChapterList(objecthtml)
    for i in urllist:
        if (number -1 ) == flag:
            return i
        number += 1

def GetChapters(url):

    if os.sep == '/':
        clean = 'clear'
    else:
        clean = 'cls'

    Bar = ['[ Home  ]','[ GetChapters ]','','']

    Print_Bar =  "\n" + "%s>%s>%s>%s"

    Print_Help = '\n\tNumber -> Enter recommendation. \
            \n\t  q    -> Enter exit. \
            \n\t'

    while True:
        os.system(clean)
        table = GetTable(url)
        print(table)
        print(Print_Help)
        print(Print_Bar % (Bar[0],Bar[1],Bar[2],Bar[3]),end = '')
        cmd = input()
        if cmd.isdigit():
            Choose = Ge_CHapter_One(url,int(cmd))
            GetContent(Choose[1],Choose[2])
        elif cmd == 'q':
            return



if __name__ == '__main__':
    
    url = 'https://www.boquge.com/book/44491/'
    GetChapters(url)

