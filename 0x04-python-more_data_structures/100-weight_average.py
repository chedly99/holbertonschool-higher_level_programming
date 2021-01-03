#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    listix = []
    listy = []
    for x, j in my_list:
        listix.append(x*j)
    for x, j in my_list:
        listy.append(j)
    return(sum(listix)/sum(listy))
