#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    X = 0
    for x in my_list:
        if x > X:
            X = x
    return X
