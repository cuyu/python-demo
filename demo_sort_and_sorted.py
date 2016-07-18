import time


def longer_than(a, b):
    a = str(a)
    b = str(b)
    if len(a) >= len(b):
        return 1
    else:
        # Note that must return -1, not 0 here. So return True or False is also not work for cmp function!
        return -1


def length(i):
    return len(str(i))


if __name__ == '__main__':
    a = [1, 232, 33, 12, 32, 2, 1342, 42, 122]
    t1 = time.time()
    print sorted(a, cmp=longer_than, reverse=True)
    t2 = time.time()
    print 'Time cost: {0}s'.format(t2 - t1)
    t1 = time.time()
    print sorted(a, key=length, reverse=True)
    t2 = time.time()
    print 'Time cost: {0}s'.format(t2 - t1)

    print '---------'
    b = list(a)
    t1 = time.time()
    a.sort(cmp=longer_than)
    t2 = time.time()
    print 'Time cost: {0}s'.format(t2 - t1)
    print a
    t1 = time.time()
    b.sort(key=length)
    t2 = time.time()
    print 'Time cost: {0}s'.format(t2 - t1)
    print b
