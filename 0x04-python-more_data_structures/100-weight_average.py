#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t_s = 0
    t_w = 0
    for score, weight in my_list:
        t_s += score * weight
        t_w += weight
    return (t_s / t_w)
