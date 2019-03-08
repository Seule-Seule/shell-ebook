#!/usr/bin/env python3
#coding=utf-8
# Author : faner
# Email  : soul.seule@gmail.com

import os
from BookCraeler.Search import Search
from BookCraeler.Search import Get_Table
from BookCraeler.Search import Get_Search_One
from BookCraeler.Chapter import GetChapters


def main():
    if os.sep == '/':
        clean = 'clear'
    else:
        clean = 'cls'

    os.system(clean)  # 清除屏幕
    os.system(r'echo  "\033[?25l"') # 隐藏光标 
    
    Bar = ['[ Home ]','','','']

    Print_Bar =  "\n" + "%s>%s>%s>%s"

    Print_Help = "\n\tNumber -> Enter recommendation. \
                  \n\t  s    -> Enter Serach. \
                  \n\t  q    -> Enter exit."

    while True:
        
        while True:

            Default_Page = Get_Table('道君',0)
            os.system(clean)
            print(Default_Page)
            print(Print_Help)
            print(Print_Bar % (Bar[0],Bar[1],Bar[2],Bar[3]),end = '')
            cmd = input()
            if cmd.isdigit():
                Choose = Get_Search_One('道君',int(cmd))
                GetChapters(Choose[5])
            elif cmd == 's':
                    Search()
            elif cmd == 'q':
                os.system(clean)
                os.system(r'echo  "\033[?25h"')
                exit()


if __name__ == '__main__':

    main()
