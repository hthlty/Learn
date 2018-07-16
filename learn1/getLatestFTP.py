#coding=utf-8

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    #创建FTP对象，并链接到FTP服务器，若发生错误则退出
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('ERROR：cannot reach "%s"' %HOST)
        return
    print('***Connected to host "%s"' %HOST)

    #尝试用anonymous登录，不行就结束
    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR:cannot login anonymous')
        f.quit()
        return
    print('***Logged in as "anonymous"')

    #进入发布目录并，切换失败则退出
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' %DIRN)
        f.quit()
        return
    print('***Changed to "%s"' %DIRN)

    #下载文件
    try:
        f.retrbinary('RETR %s' %FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' %FILE)
        os.unlink(FILE)
    else:
        print('***Downloaded "%s" to CD' %FILE)
    f.quit()

if __name__ == '__main__':
    main()