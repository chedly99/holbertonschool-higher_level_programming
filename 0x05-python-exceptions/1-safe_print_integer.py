#!/usr/bin/python3
def safe_print_integer(v):
    try:
        print("{:d}".format(v))
        return True
    except Exception:
        return (False)
