#!/usr/bin/python3
for char_code in range(ord('z'), ord('A') - 1, -1):
    char = chr(char_code)
    if char.islower():
        print("{}".format(char), end="")
    elif char.isupper():
        print("{}".format(char), end="")
