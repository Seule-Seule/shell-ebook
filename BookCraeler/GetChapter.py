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
    while True:
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
            print('\n \t\t[页面请求错误，正在尝试重新请求 ！]')
        

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

    print('\n \t\t正在读取章节列表 ......')
    
    # 目录URl信息写入 ChaptersList.csv 文件
    ChapterList2 = []

    for info in ulist[2:-1]:
        info_soup = BeautifulSoup(str(info),'lxml')
        chapter_name = info_soup.a.string
        chapter_url  = 'https://www.boquge.com' + info_soup.a.get('href')
        with open(path,'a') as chapters_list:
            writer = csv.writer(chapters_list)
            writer.writerow(chapter_name.split("\n") + chapter_url.split("\n"))
        ChapterList2.append(chapter_name.split(",") + chapter_url.split(","))
    print('\n \t\t章节列表读取成功，相关信息储存在 ChaptersList.csv 中 !')

    return ChapterList2

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

def GetChapters():
    while True:
        print('<<<' +  '-'*25 + '[ 章 节 ]' +  '-'*25  +  '>>>' \
             "\n \t\t [1] -> 输入章节URL链接 \
              \n \t\t [2] -> 退出查看 ")
        
        flag = input('\n \t\t[请输入功能键] >>>')
        if flag == '2':
            return

        objecturl = input("\n \t\t[请输入链接] >>>")

        objecthtml = ChaptersRequsts(objecturl)
        urllist =  ChapterList(objecthtml)

        ChapterNumber = 0

        for i in urllist:

            ChapterNumber += 1

            print("|%-5s|%-s|%-s"
                   %(ChapterNumber
                   , Displiay(i[0],15)
                   , Displiay(i[1],30)))

def GetChapters2(url):
    objecthtml = ChaptersRequsts(url)
    urllist =  ChapterList(objecthtml)

    return urllist
    



if __name__ == '__main__':

    GetChapters()

