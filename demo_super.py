'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 6/7/16
'''


class T(object):
    b = 'b'

    def __init__(self):
        print 'Enter T'
        self.a = 0
        print 'Leave T'


class A(T):
    def __init__(self):
        print 'Enter A'
        super(A, self).__init__()
        self.a = 1
        print 'Leave A'


class B(T):
    b = 'B'

    def __init__(self):
        print 'Enter B'
        super(B, self).__init__()
        self.a = 2
        print 'Leave B'


class C(A, B):
    def __init__(self):
        super(C, self).__init__()


class D(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


def What_super_do(cls, inst):
    """
    super will get the next class of the input cls from the MRO of the input inst.
    """
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]


if __name__ == '__main__':
    a = A() # The super(A, self).__init__() in class A will call class T's __init__ method.
    print '------'
    c = C() # The super(A, self).__init__() in class A will call class B's __init__ method.
    print '------'
    d = D() # Watch out to mix use super and cls.__init__! (class T and B are inited twice here!)
    print '------'
    # The MRO(Method Resolution Order) of c is [C, A, B, T, object]
    print c.a
    print c.b
    print type(super(C, c))
    print super(C, c).b
    print super(B, c).b
    print super(A, c).b  # It looks strange here, but super(A, c) represents class B!
    print '------'
    print What_super_do(A, c)
