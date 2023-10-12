#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new = my_list[:]
    for item, n in enumerate(new):
        if n == search:
            new[item] = replace
        return (new)
