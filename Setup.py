#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

from BookCraeler.Search import Search
from BookCraeler.GetChapter import GetChapters
from BookCraeler.GetContent import GetContent


def SearchFun():
    keyword = input('Please input Keyword : ')
    SearchList = Search(keyword)
    for message in SearchList:
        print(message)

def GetChapterFun():
    url = input('Please input book chapters url : ' )
    GetChapters(url)

def GetContentFun():
    url = input('Pleasr input book content url : ')
    text = GetContent(url)
    print(text)

def cmd(flag):
      

    switch = {
        '0':SearchFun,
        '1':GetChapterFun,
        '2':GetContentFun,
        '3':exit
    }

    return switch.get(flag,'Error Input !')

def main():
    print( '<<<' +  '-'*70  +  '>>>' \
           '\n \t\t Hello , Welocome boquge ! Please goto......\n \
           \n \t\t author : 范儿 \
           \n \t\t Email  : soul.seule@qq.com \
           \n \t\t [0] -> 搜索 \
           \n \t\t [1] -> 提供书本URL链接以查看章节 \
           \n \t\t [2] -> 提供章节URL查看内容 \
           \n \t\t [3] -> 退出程序')
    while True:
        flag = input('\n \t\t Please Choose:')

        fun = cmd(flag)
        if type(fun) == type('Error Input !'):
            print(fun)
        else:
            fun()

        print( '<<<' +  '-'*70  +  '>>>' \
                '\n \t\t [0] -> 搜索 \
                \n \t\t [1] -> 提供书本URL链接以查看章节 \
                \n \t\t [2] -> 提供章节URL查看内容 \
                \n \t\t [3] -> 退出程序')
    
if __name__ == '__main__':

    main()
