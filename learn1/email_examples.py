#coding=utf-8

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text  = MIMEText('Hello world \r\n','plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello world!</h4>'
        '</body></html>','html'
    )
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn,'r')
    data = f.read()
    f.close()
    email = MIMEImage(data,name=fn)
    email.add_header('Content-Dispositon','attachment:filename "%s"' %fn)
    return email

def sendmsg(fr,to,msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr,to,msg)
    s.quit()

if __name__ == '__main__':
    print('sending multipart alternative msg....')
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['to'] = ''.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    sendmsg(SENDER,RECIPS,msg.as_string())

    print('sending image msg.....')
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = ''.join(RECIPS)
    msg['Subject'] = 'image file test'
    sendmsg(SENDER,RECIPS,msg.as_string())
