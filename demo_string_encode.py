a = 'a'
print repr(a)
encode_a = a.encode('UTF-16')
print encode_a
print repr(encode_a)
decode_a = encode_a.decode('UTF-16')
print decode_a
print repr(decode_a)
# Concusion: defualt string is ascii encoded (in Python 2), after decoding, it
# transforms to utf-8 encoded.
