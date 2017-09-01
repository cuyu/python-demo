'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 6/13/16
'''
import multiprocessing
import time
from multiprocessing.queues import Queue


class MyList(list):
    def __init__(self):
        super(MyList, self).__init__()
        print 'my list inited'

    def __getstate__(self):
        print 'got pickled'
        return self.__dict__

    def __setstate__(self, state):
        print 'got unpickled'
        self.__dict__.update(state)


class MyQueue(Queue):
    def __init__(self):
        super(MyQueue, self).__init__()
        print 'my queue inited'

    def __new__(cls, *args):
        print 'my queue new'
        return Queue.__new__(cls, *args)

    def __getstate__(self):
        print 'my queue getstate'
        return Queue.__getstate__(self)

    def __setstate__(self, state):
        print 'my queue setstate'
        return Queue.__setstate__(self, state)


A = MyList()
Q = MyQueue()


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        A.append(self.name)
        print A
        Q.put(self.name)


if __name__ == '__main__':
    p1 = MyProcess()
    p2 = MyProcess()
    p1.start()
    p2.start()
    time.sleep(1)
    print '------------'
    print A
    print Q.get()
    print Q.get()
    p1.join()
    p2.join()

    print '------------'
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=q.put, args=(A,))
    p.start()
    print q.get()
    p.join()
