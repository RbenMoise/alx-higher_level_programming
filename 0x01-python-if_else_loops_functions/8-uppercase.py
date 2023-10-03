#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= str <= 'z':
           char = chr(ord(char)-32)
        print("{}".format(char), end="")
    print("")
