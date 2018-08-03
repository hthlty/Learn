#coding=utf-8

from urllib import request,error,parse

LOGIN = 'wesley'
PASSWD = "you'll Never Guess"
URL = 'http://localhost'
REALM = 'Secure Archive'

def handler_version(url):
    from urllib import parse
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM,
                      parse.urlparse(url)[1],LOGIN,PASSWD)
    opener = request.build_opener(hdlr)
    request.install_opener(opener)
    return url

def request_version(url):
    from base64 import encodestring
    req = request.Request(url)
    b64str =encodestring(bytes('%s:%s' %(LOGIN,PASSWD),'utf-8')) [:1]
    req.add_header('Authorization','Basic %s' %b64str)
    return req

for funcType in ('handler','request'):
    print('*** Using %s:' %funcType.upper())
    url = eval('%s_version' %funcType)(URL)
    f = request.urlopen(url)
    print(str(f.readline(),'utf-8'))
    f.close()