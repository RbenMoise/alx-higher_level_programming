#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    numbers = sys.argv[1:]

    for i in numbers:
        sum += int(i)
    print("{}".format(sum))
