'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 5/26/16
'''


def use_yield():
    print 'one'
    yield 1
    print 'two'
    yield 2
    print 'over'


def use_return():
    return 1


if __name__ == '__main__':
    print use_return()

    one_generator = use_yield()
    print next(one_generator)
    print next(one_generator)
    try:
        print next(one_generator)
    except StopIteration:
        print 'StopIteration'

    for i in use_yield():
        print i
