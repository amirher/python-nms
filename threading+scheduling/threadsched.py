#! /usr/bin/env python

import sched
import threading
import time
import signal
import sys

"""
step
risk_factor
"""

def thread_1m():
    exec_time=time.time()
    lock.acquire()
    print "1m"
    lock.release()
    cur_time=time.time()
    step=1.0
    risk_factor=0.7
    exceded = exec_time + risk*step - cur_time 
    if exceded > 0:
        print "Taking too long"
    scheduler_1m.enter(exec_time+1-cur_time,1,thread_1m,())
    scheduler_1m.run()
    
def thread_5m():
    exec_time=time.time()
    lock.acquire()
    print "5m"
    lock.release()
    scheduler_5m.enter(exec_time+2-time.time(),1,thread_5m,())
    scheduler_5m.run()
    
def thread_15m():
    exec_time =time.time()
    lock.acquire()
    print "15m"
    lock.release()
    scheduler_15m.enter(exec_time+5-time.time(),1,thread_15m,())
    scheduler_15m.run()

scheduler_1m = sched.scheduler(time.time, time.sleep)
scheduler_5m = sched.scheduler(time.time, time.sleep)
scheduler_15m = sched.scheduler(time.time, time.sleep)

signal.signal(signal.SIGINT, exit)

threads = []
lock = threading.Lock()

t = threading.Thread(target=thread_1m, args=())
threads.append(t)
t.start()
t = threading.Thread(target=thread_5m, args=())
threads.append(t)
t.start()
t = threading.Thread(target=thread_15m, args=())
threads.append(t)  
t.start()
