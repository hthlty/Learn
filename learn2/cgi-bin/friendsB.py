#coding=utf-8

import cgi

header = 'Content-Type:text/html\n\n'

formhtml = '''<html><head><title>
Friends CGI Demo</title></head>
<body><h3>Friends list for:<I>NEW USER</i></h3>
<form action="/cgi-bin/friendsB.py">
<b>Enter your name:</b>
<input type=hidden name=action balue=edit>
<input type=text name=person value='NEW USER' size=15>
<p><b>How many firends do you have?</b>
%s
<p><input type=submit></from></body></html>'''

fradio = '<input type=radio name=howmany value="%s" %s>\n'

def showForm():
    friends = []

    for i in (0,10,25,50,100):
        checked = ''
        if i == 0:
            checked = 'CHECKED'
            friends.append(fradio %(str(i),checked,str(i)))

    print('%s%s' %(header,formhtml %''.join(friends)))

reshtml = '''
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamin screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><P>
You have <B>%s</B>friends.
</BODY></HTML>
'''
def doResults(who,howmany):
    print(header+reshtml %(who,who,howmany))

def process():
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form['person'].value
    else:
        who = 'NEW USER'

    if 'howmany' in form:
        howmany = form['howmany'].value
    else:
        howmany = 0

    if 'action' in form:
        doResults(who,howmany)
    else:
        showForm()


if __name__ == '__main__':
    process()