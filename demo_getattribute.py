class BaseA(object):

    def __init__(self, a):
        self.a = a

    def __getattribute__(self, item):
        print('get attr:' + item)
        # The input is str type, need to transform to actual type!
        attr = super(BaseA, self).__getattribute__(item)
        return attr


class A(BaseA):

    def __init__(self, a):
        super(A, self).__init__(a)
        self.b = 'b'

    def set_b(self, value):
        self.b = value


class C(object):

    def __init__(self, c):
        self.c = c

if __name__ == "__main__":
    a1 = A('a1')
    print '---'
    print a1.a
    print '---'
    print a1.b
    print '---'
    c1 = C('c1')
    print '---'
    a1.set_b(c1)
    print '---'
    print a1.b
    print '---'
    print a1.b.c
