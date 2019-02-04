#!/usr/bin/env python3
# coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
import csv
import requests
from bs4 import BeautifulSoup

def ChaptersRequsts(ChapterUrl):
    
    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0(Linux;X11)'    
    
    }

    try:
        # 请求页面
        r = requests.get(url = ChapterUrl,timeout = 5,headers = headers)
                         
        # 收集错误信息
        r.raise_for_status()
        
        # 修改text编码
        if r.encoding == 'ISO-8859-1': 
            r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return ""

def ChapterList(html):

    # 目录文件存储路径
    path = os.getcwd() + os.sep +'ChaptersList.csv'
    if os.path.isfile('ChaptersList.csv'):
        os.remove(path)


    # 目录第一行  章节名称:章节URl链接
    with open(path,'a') as chapters_list:
        writer = csv.writer(chapters_list)
        writer.writerow(['章节名称','章节URL链接'])
    
    # 获取目录URL信息
    html_soup = BeautifulSoup(html,"lxml")
    ulist = list(html_soup.find('ul',{'id':'chapters-list'}))

    print('Read chapters list......')
    
    # 目录URl信息写入 ChaptersList.csv 文件
    for info in ulist[2:-1]:
        info_soup = BeautifulSoup(str(info),'lxml')
        chapter_name = info_soup.a.string
        chapter_url  = 'https://www.boquge.com' + info_soup.a.get('href')
        with open(path,'a') as chapters_list:
            writer = csv.writer(chapters_list)
            writer.writerow(chapter_name.split("\n") + chapter_url.split("\n"))
    print('Read chapters list success and save to ChaptersList.csv !')

def GetChapters(objecturl):
    urllist = []


    objecthtml = ChaptersRequsts(objecturl)
    urllist =  ChapterList(objecthtml)



if __name__ == '__main__':
    '''
    GetChapters can get chapters list of book that from objecturl.
        
        And GetChapters write chapters list to ChapterdList.csv.
    '''

    # 默认获取《道君》章节目录
    myurl = 'https://www.boquge.com/book/44491/'
    GetChapters(objecturl = myurl)

