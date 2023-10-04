#!/usr/bin/python3
for ast in range(ord('a'),ord('z')+1):
    if chr(ast) not in ('e', 'q'):
        print("{}".format(chr(ast)), end="")
