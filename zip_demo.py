import zlib
s = b'witch which has which witches wrist watch'
print(s)
print(len(s))
t = zlib.compress(s)
print(t)
print(len(t))