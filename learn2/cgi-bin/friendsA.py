#coding=utf-8

import cgi


reshtml = '''Content-Type:text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamin screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><P>
You have <B>%s</B>friends.
</BODY></HTML>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['homany'].value
print(reshtml %(who,who,howmany))