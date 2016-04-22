class TestDestructor:

    def __init__(self, val):
        self.val = val
        print 'initializing..' + self.val

    def __del__(self):
        print 'destructing..' + self.val

if __name__ == '__main__':
    aaa = TestDestructor('aaa')
    if 1:
        bbb = TestDestructor('bbb')
        print('---')
