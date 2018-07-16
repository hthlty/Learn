#coding=utf-8

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSERV = ''  #发送邮件服务器
POP3SERV = ''  #接收邮件服务器

who = ''
body = '''\
From:%(who)s
To:%(who)s
Subject:test msg
Hello world!''' %{'who':who}

sendserv = SMTP(SMTPSERV)
errs = sendserv.sendmail(who,[who],origMsg)
sendserv.quit()

recvserv = POP3(POP3SERV)
recvserv.user('')
recvserv.pass_('')
rsp,msg,siz = recvserv.retr(recvserv.stat()[0])
sep = rsp.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody
