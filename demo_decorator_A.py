# -*- coding: utf-8 -*-
def deco(func):
    print("-before myfunc() called.")
    func()
    print("-after myfunc() called.")
    return func


@deco
def myfunc():
    print(" myfunc() called.")


def myfunc_normal():
    print(" myfunc_normal() called.")


# 1.之所以说装饰器是语法糖就是因为它是为了简洁，
#   下面的语句可以达到和@deco一样的效果。
myfunc_normal = deco(myfunc_normal)
# ------------------------------------------------
print '===='
myfunc()
myfunc_normal()
# 2. 存在一个问题，即修饰器函数第二次调用时就没有运行了
#   使用内嵌包装函数来确保每次新函数都被调用，内嵌包装
#   函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
print '===='
myfunc()
myfunc_normal()


def deco_new(func):
    print func.__name__

    def _deco(a, b):
        """
        _deco
        """
        print("before {0} called.".format(func.__name__))
        ret = func(a, b)
        print("after {0} called.".format(func.__name__))
        # 不需要返回func，实际上应返回原函数的返回值
        return ret

    return _deco


@deco_new
def myfunc_new(a, b):
    """
    myfunc_new
    """
    print('myfunc_new(%s, %s) called' % (a, b))
    return a, b


@deco_new
def another_func(a, b):
    print('another_func(%s, %s) called' % (a, b))
    return a, b


# 3. The function `myfunc_new' here is actually a `_deco' function object(equals myfunc_new=deco_new(myfunc_new));
#   Can I understand like this: deco_new(myfunc_new)) generate a instance of deco_new, and it bind myfunc_new to the
#   instance. When we call myfunc(), we actually call deco_new._deco(), which has myfunc_new as a binded object.
#   So the myfunc_new.__doc__ also becomes to _deco.__doc__ (to solve this problem, try `functools' package).
myfunc_new(1, 2)
myfunc_new(3, 4)
print myfunc_new.__name__
print myfunc_new.__doc__

# 4. 这里的another_func其实也是一个`_deco'函数对象,
#   只不过它和上面`myfunc_new'所指向的并不是同一个对象
#   (可以从内存地址看出来). 似乎印证了第三点说的内容.
another_func(5, 6)

# >See demo_decorator_B.py to understand more!
