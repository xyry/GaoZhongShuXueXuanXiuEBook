#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/2/8 9:31
# @Author  : YPL
# @FileName: download_textbook.py
# @Software: PyCharm
import urllib.request
if __name__ =='__main__':
    link = "http://www.shuxue9.com/pep/gzxuanxiu12/ebook/"
    # 059到072
    # 左开右闭
    for i in range(59,73):
        s = '0'+str(i)+'.jpg'
        urllib.request.urlretrieve(link+s, 'images/'+s)
        print("图片"+str(i)+'下载完成')
