#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif n == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(n))  
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))