#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)-1
    if number == 0:
        print("0 argments.")
    else:
        print("{} argument{}:".format(number, 's' if number > 1 else ''))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
