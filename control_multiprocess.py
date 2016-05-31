'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 5/31/16
'''

from multiprocessing import Process, Value, Array, Manager
import time


def solution_one_func(n, a):
    # As stdout is print on this process and we cannot see, we use a file to display outputs.
    with open('/tmp/solution_one.txt', 'w') as f:
        for i in xrange(20):
            time.sleep(1)
            f.write(str(n.value))
            f.write(a[0])
            f.write('\n')


def solution_one_main():
    num = Value('d', 1.1)
    arr = Array('u', ['a'])
    p = Process(target=solution_one_func, args=(num, arr))
    p.start()
    time.sleep(10)
    arr[0] = 'c'
    num.value = 2.2
    print arr[0]
    p.join()


def solution_two_func(d, l):
    with open('/tmp/solution_two.txt', 'w') as f:
        for i in xrange(20):
            time.sleep(1)
            f.write(d['a'])
            f.write(str(l[1]))
            f.write('\n')


def solution_two_main():
    manager = Manager()
    d = manager.dict()
    d['a'] = 'AAA'
    l = manager.list([1, 2, 3])
    p = Process(target=solution_two_func, args=(d, l))
    p.start()
    time.sleep(10)
    d['a'] = 'BBB'
    l[1] = 8
    p.join()


if __name__ == '__main__':
    # Refer: https://docs.python.org/2/library/multiprocessing.html#sharing-state-between-processes
    solution_one_main()
    solution_two_main()
