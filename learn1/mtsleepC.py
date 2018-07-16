#conding=tf-8

#使用threading模块
import threading
from time import ctime,sleep

loops = [4,2]

def loop(nloop,nsec):
    print('start loop nloop at:',ctime())
    sleep(nsec)
    print('loop nloop done at:',ctime())

def main():
    print('starting at:',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()  #star threads

    for i in nloops:        #wait for all threads to finish
        threads[i].join()

    print('all done at:',ctime())

if __name__ == '__main__':
    main()

