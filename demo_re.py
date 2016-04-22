import re

if __name__ == '__main__':
    pattern = re.compile('\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}')
    print pattern.match('www  12 22:33:33')
    print pattern.match('ww!  12 22:33:33')
