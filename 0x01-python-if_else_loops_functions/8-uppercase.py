#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if(ord(x) in range(ord('a'), ord('z') + 1)):
            x = chr(ord(x) - 32)
        print("{:s}".format(x), end='')
    print('')
