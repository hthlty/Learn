#coding=utf-8

#获取亚马逊图书排名

from atexit import register
from re import compile
from threading import Thread
from urllib.request import urlopen
from time import ctime

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNS = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Devlopment with Django',
    '0137143419':'Python Fundamentals'
}

def getRanking(isbn):
    page = urlopen('%s%s' %(AMZN,isbn))
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0],'utf-8')
def _showRanking(isbn):
    print('- %r ranked %s' %(ISBNS[isbn],getRanking(isbn)))

def _main():
    print('At',ctime(),'on Amazon...')
    for isbn in ISBNS:
        #_showRanking(isbn)
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def  _atexit():
    print('all done at:',ctime())

if __name__ == '__main__':
    _main()