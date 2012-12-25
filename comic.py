# comic.py is a tool to detect whether the comic had been updated
# coding=UTF-8
import urllib
import os
import re
import sys

def detect(url):
  """detect the url"""
  #f = urllib.urlopen(url)      
  
  path = os.path.abspath(os.path.join('.', 'comic.html'))
  if os.path.exists(path):
    f = open(path)
    for line in f:
      line = line.decode('gb2312')
     # print line
      match = re.search(u"(\u66f4\u65b0\u65f6\u95f4)：(\d+-\d+-\d+)", line)
      if match:
	print match.group(1)
	print match.group(2)
    f.close()
  else:  
    urlliburlretrieve(url, "comic.html")
  #print f.read()

def main():
  detect("http://imanhua.com/comic/1832/")

if __name__ == '__main__':
  main()
  print sys.getdefaultencoding()
