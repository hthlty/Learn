#coding=utf-8

from html.parser import HTMLParser
from io import StringIO
from urllib import request

from bs4 import BeautifulSoup,SoupStrainer
from html5lib import parse,treebuilders

URLs = ('http://python.org','http://google.com',)

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url,f):
    'simpleBS() -use BeautifulSoup to parse all tags to get anchors'
    output(request.urljoin(url,x['href']) for x in BeautifulSoup(f).findAll('a'))

def fasterBS(url,f):
    'fasterBS() -use BeautifulSoup to parse only anchor tags'
    output(request.urljoin(url,x['href']) for x in BeautifulSoup(
        f,parseOnlyThese = SoupStrainer('a')
    ))

def htmlparser(url,f):
    'htmlparser() -use HTMLParser to parse anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self,'data'):
                self.data = []
            for attr in attrs:
                self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(request.urljoin(url,x) for x in parser.data)

def html5libparse(url,f):
    'html5libparse()-use html5lib to parse anchor tags'
    output(request.urljoin(url,x.attributes['href'])\
           for x in parse(f) if isinstance(x,treebuilders.simpletree.Element)\
           and x.name == 'a')

def process(url,data):
    print('\n *** simple BS')
    simpleBS(url,data)
    data.seek(0)
    print('\n *** faster BS')
    fasterBS(url.data)
    data.seek(0)
    print('\n*** HTMLParser')
    htmlparser(url,data)
    data.seek(0)
    print('\n*** HTML5lib')
    html5libparse(url,data)


def main():
    for url in URLs:
        f  = request.urlopen(url)
        data = StringIO(f.read())
        f.close()
        process(url,data)


if __name__ == '__main__':
    main()