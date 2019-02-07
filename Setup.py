#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

from BookCraeler.Search import Search
from BookCraeler.GetChapter import GetChapters
from BookCraeler.GetContent import GetContent


def SearchFun():
    Search()

def GetChapterFun():
    url = input('Please input book chapters url : ' )
    GetChapters(url)

def GetContentFun():
    url = input('Pleasr input book content url : ')
    text = GetContent(url)
    for paragraph in text:
        print(paragraph)

def cmd(flag):
      

    switch = {
        '1':SearchFun,
        '2':GetChapterFun,
        '3':GetContentFun,
        '4':exit
    }

    return switch.get(flag,'Error Input !')

def main():
    print( '<<<' +  '-'*25 + '[ 首 页 ]' +  '-'*25  +  '>>>' \
           '\n \t\t Hello , Welocome boquge ! Please goto......\n \
           \n \t\t author : 范儿 \
           \n \t\t Email  : soul.seule@qq.com \
           \n \t\t [1] -> 搜索 \
           \n \t\t [2] -> 提供书本URL链接以查看章节 \
           \n \t\t [3] -> 提供章节URL查看内容 \
           \n \t\t [4] -> 退出程序')
    while True:
        flag = input('\n \t\t[请输入功能键] >>>')

        fun = cmd(flag)
        if type(fun) == type('Error Input !'):
            print('\n \t\t' + fun)
        else:
            fun()

        print( '<<<' +  '-'*70  +  '>>>' \
                '\n \t\t [1] -> 搜索 \
                \n \t\t [2] -> 提供书本URL链接以查看章节 \
                \n \t\t [3] -> 提供章节URL查看内容 \
                \n \t\t [4] -> 退出程序')
    
if __name__ == '__main__':

    main()
