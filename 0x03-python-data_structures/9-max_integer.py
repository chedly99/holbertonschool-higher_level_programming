#!/usr/bin/python3
def max_integer(my_list=[]):
    c = my_list[0]
    if my_list == 0:
        return None
    for x in my_list:
        if x > c:
            c = x
    return(c)
