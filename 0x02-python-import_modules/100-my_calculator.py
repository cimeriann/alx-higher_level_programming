#!/usr/bin/python3


def calculator():
    from sys import argv
    operators = ["+", "-", "*", "/"]
    num_of_args = len(argv) - 1
    if num_of_args == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "-":
            result = int(argv[1]) - int(argv[3])
            print("{:d} - {:d} = {:d}".format(a, b, result))
            exit(0)
        elif argv[2] == "+":
            result = int(argv[1]) + int(argv[3])
            print("{:d} + {:d} = {:d}".format(a, b, result))
            exit(0)
        elif argv[2] == "*":
            result = int(argv[1]) * int(argv[3])
            print("{:d} * {:d} = {:d}".format(a, b, result))
            exit(0)
        elif argv[2] == "/":
            result = int(argv[1]) * int(argv[3])
            print("{:d} / {:d} = {:d}".format(a, b, result))
            exit(0)
        elif argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)


if __name__ == "__main__":
    calculator()
