from multiprocessing.pool import ThreadPool

import time


def foo(bar, baz):
    print 'hello {0}'.format(bar)
    time.sleep(5)
    return 'foo' + baz


if __name__ == '__main__':
    # Try different processes.
    pool = ThreadPool(processes=1)

    async_result = pool.apply_async(foo, ('world', 'foo'))  # tuple of args for foo

    async_result2 = pool.apply_async(foo, ('123', 'asd'))
    # do some other stuff in the main process

    return_val = async_result.get()  # get the return value from your function.
    return_val2 = async_result2.get()
