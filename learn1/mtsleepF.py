#coding=utf-8
#线程锁

from atexit import register
from random import randrange
from threading import Thread,current_thread,Lock
from time import sleep,ctime

lock = Lock()

class CleanOutputSet(set):
    def __str__(self):
        return '.'.join(x for x in self)

loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = current_thread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' %(ctime(),myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' %(ctime(),myname,nsec))
    print('(remaining:%s)' %(remaining or 'NONE'))
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()


@register
def _atexit():
    print('all done at:',ctime())


if __name__ == '__main__':
    _main()