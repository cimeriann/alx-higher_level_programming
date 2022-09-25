#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    i = -1
    reversed_list = mylist[::]
    for i in reversed_list:
        print("{:d}".format(i))

    # while abs(i) <= length:
        # print("{:d}".format(my_list[i]))
        # i -= 1
