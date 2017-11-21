# !/usr/bin/env python3

def displayNumType(num):
    print(str(num) + ' is', end='')
    if isinstance(num, (int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all!!')

displayNumType(-69)
displayNumType(12.1)
displayNumType(2+3j)
displayNumType('aaa')
