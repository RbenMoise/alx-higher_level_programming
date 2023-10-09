#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)

    if lena < 2 or lena == 0:
        tuple_a += (0,0)
    if lenb  < 2 or lenb ==0:
        tuple_b += (0,0)
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (result)
