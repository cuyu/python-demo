# -*- coding: utf-8 -*-

class decoratorWithoutArguments(object):
    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print "Inside __init__()"
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print "Inside __call__()"
        self.f(*args)
        print "After self.f(*args)"


@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "argument", "list")
print "After first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "After second sayHello() call"

# --------------------------------------------------------------
print '---------------------------------------------------------'


class decoratorWithArguments(object):
    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print "Inside __call__()"

        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args)
            print "After f(*args)"

        return wrapped_f


@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "argument", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"

# --------------------------------------------------------------
print '---------------------------------------------------------'


# Get same effect using functions instead of classes.
# Notice the difference between decorator without args(in demo_decorator_A.py) and this one!
def decoratorFunctionWithArguments(arg1, arg2, arg3):

    def wrap(f):
        print "Inside wrap()"

        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", arg1, arg2, arg3
            f(*args)
            print "After f(*args)"

        return wrapped_f

    return wrap


@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "argument", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"


# 综上,可以猜测decorator的实现机制为(以上面的例子为例):
# 若decorator不含有参数:
# 1.在编译时，执行temp=decoratorWithoutArguments(sayHello)
# 2.执行sayHello=temp
# 3.在实际调用sayHello(*args)时,实际调用的是decoratorWithoutArguments的一个instance(即执行了其中的__call__(*args)方法);
#   换个角度,实际相当于调用的是decoratorWithoutArguments(sayHello)(*args)
# 若decorator含有参数(设为arg1,arg2,arg3):
# 1.在编译时，执行temp=decoratorWithArguments(arg1,arg2,arg3)
# 2.执行sayHello=temp(sayHello)(即执行temp.__call__(sayHello))
# 3.在实际调用sayHello(*args)时,实际调用的是decoratorWithArguments的一个instance生成的一个instance(连环调用);
#   换个角度,实际相当于调用的是decoratorWithArguments(arg1,arg2,arg3)(sayHello)(*args). -_-
#   这也是为啥有参数没参数实现decorator会不一致,如果一致的话没参数应该是decoratorWithoutArguments()(sayHello)(*args)
#   但显然如果一致了,确实便于理解了,但不便于写代码啊~
