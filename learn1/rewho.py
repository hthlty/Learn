#coding=utf-8
from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

# f = open('whodata.txt','r')
# for eachLine in f:
#     print(re.split(r'\s\s+',eachLine))    #\s\s+ 表示至少拥有两个以上的空白符
# f.close()
# with os.popen('tasklist','r') as f:
#     for eachLine in f:
#         print(re.split(r'\s\s+|\t',eachLine.strip()))

# llen = random.randrange(4,8)
# print(llen)
#
# dtint = random.randrange(sys.maxsize)
# print(dtint)
#
# dtstr = time.ctime()
# print(dtstr)


tlds = ('com','edu','org','gov')

for i in range(5,11):
    dtint = randrange(maxsize)
    dtstr = ctime()
    llen = randrange(4,8)
    login = ''.join(choice(lc))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc))
    for j in range(dlen):
        print('/s::/s@/s./s::/d-/d-/d' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen))