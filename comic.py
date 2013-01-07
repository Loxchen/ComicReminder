# comic.py is a tool to detect whether the comic had been updated
# coding=UTF-8
import urllib
import os
import re
import sys

def detect(url):
    """detect the url"""
    content = urllib.urlopen(url).read()
    content = content.decode('gb2312')
    match = re.search(u"\u66f4\u65b0\u65f6\u95f4：(\d+-\d+-\d+)", content)
    match2 = re.search(u'<a href.* title="[\u4e00-\u9fa5]+(\d+)[\u4e00-\u9fa5]+" target="_blank" class="new">', content)
    if match and match2:
	return match.group(1) + u':\u7b2c' + match2.group(1) + u'\u8bdd'
    
def list(filename):
    """read the comic list from file"""
    comiclist = []
    f = open(filename, 'rU')
    for line in f:
	comiclist.append(line.split(' '))
    f.close()
    return comiclist

def peek(filename):
    """peek how are the comics"""
    comiclist = list(filename)
    for comic in comiclist:
	print comic[0],
	print detect(comic[1])
	

def main():
    #detect("http://imanhua.com/comic/55/")
    peek("comic_list.txt")

if __name__ == '__main__':
    main()
