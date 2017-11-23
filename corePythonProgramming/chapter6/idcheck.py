# !/usr/bin/env python3

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to Identifier Checker v1.0')
print('Testees must be at least 2 chars long.')
myInput = input('Identifier to test?')

if len(myInput) > 1:

    if myInput[0] not in alphas:
        print('invalid: first symbol must be alphabetic')
    else:
        alphnums = alphas + nums
        for otherChar in myInput[1:]:

            if otherChar not in alphnums:
                print('invalid: remaining symblos must be alphanumberic')
                break
        else:
            print('okay as an identifier')
