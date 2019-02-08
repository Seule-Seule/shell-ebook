#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
import Search
import GetChapter
import GetContent


def Download(BookName,BookUrl):
    path = os.getcwd() + os.sep + BookName + os.sep

    if not os.path.isdir(path):
        os.mkdir(path)
    
    objecthtml = GetChapter.ChaptersRequsts(BookUrl)
    ChapterList = GetChapter.ChapterList(objecthtml)
    for chapter in ChapterList:
        
        ChapterPath = path + chapter[0] + '.md'
        
        with open(ChapterPath,'a') as ContentFile:
            ContentFile.writelines('# ' + chapter[0] + '\n***\n')
            
        ContentHtml = GetContent.ContentRequests(chapter[1])
        ContentList = GetContent.ContentText(ContentHtml)

        for content in ContentList:
            content.strip("") \
                    .strip('\r\n').replace(u'\u3000', u'') \
                    .replace(u'\xa0', u' ')
            with open(ChapterPath,'a') as ContentFile:
                ContentFile.writelines(content)
                ContentFile.writelines('\n\n')
        

        with open(ChapterPath,'a') as ContentFile:
            ContentFile.writelines('\n***\n制作:范儿\n\n邮箱:soul.seule@qq.com\n***\n')

        print("%-4s%-20s%-10s" %('章节',chapter[0],'下载成功 ！'))




if __name__ == '__main__':

    Download('道君','https://www.boquge.com/book/42126/')
