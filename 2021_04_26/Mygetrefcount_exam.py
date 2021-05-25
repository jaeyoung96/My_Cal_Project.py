import sys
a = 65
print(a)
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
b = 'test'
print(sys.getrefcount(a))