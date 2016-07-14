import time
from threading import Thread

def sleeper(i):
    time.sleep(100000)
    print("thread %d sleeps for 5 seconds" % i)
    print("thread %d woke up" % i)

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()