"""
If the writting content are only English, saving as 'utf-8' is same to 'ascii'.
So the file will be 'ascii' even if we encode the content to 'utf-8'.
"""
file_path = '/Users/CYu/Code/other code/Test.conf'
with open(file_path, 'w') as f:
    f.write('aaa'.encode('utf-16'))

with open(file_path, 'r') as f:
    for line in f.readlines():
        print line.decode('utf-16')

# ====================Test codecs module=====================
import codecs
content = codecs.open(file_path, 'r', 'utf-16').read()
print content
