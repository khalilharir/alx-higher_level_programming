#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    L = []
    for elt in my_list:
        L.append(True if not elt % 2 else False)
    return L
