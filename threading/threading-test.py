#! /usr/bin/env python
import threading
import time

def worker(num):
    """thread worker function"""
    time.sleep(1)
    lock.acquire()
    print 'Worker: %s' % num
    lock.release()
    return

threads = []
lock = threading.Lock()
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
