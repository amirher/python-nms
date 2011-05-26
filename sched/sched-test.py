#!/usr/bin/env python

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def scheduler_1min(name):
        print 'EVENT:', time.time(), name
def scheduler_5min(name):
	print 'EVENT:', time.time(), name
def scheduler_15min(name):
	print 'EVENT:', time.time(), name
def scheduler_rt(name):
	print 'EVENT:', time.time(), name


print 'START:', time.time()

scheduler.enter(1, 1, scheduler_1min, ('1',))
scheduler.enter(5, 1, scheduler_5min, ('5',))
scheduler.enter(15,1, scheduler_15min, ('15',))
scheduler.enter(1,1, scheduler_rt, ('rt',))
scheduler.run() ## Blocks until all finish!
