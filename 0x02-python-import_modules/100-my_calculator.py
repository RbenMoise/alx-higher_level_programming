#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    opt = int(sys.argv[2])
    b = int(sys.argv[3])

    if opt == '+':
        result = add(a,b)
    elif opt == '-':
        result = mul(a,b)
    elif opt == 'i':
        result == sub(a,b)
    elif opt == '/':
        result = div(a,b)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.ecit(1)
    print("{} {} {} = {}".format(a, opt, b, result))
