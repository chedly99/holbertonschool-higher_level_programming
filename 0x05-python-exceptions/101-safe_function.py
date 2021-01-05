#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except Exception as op:
        print("Exception: {}".format(op), file=sys.stderr)
        return None
