#!/usr/bin/python3


def no_c(my_string):
    cp_string = ""

    for i in my_string:
        if i != "c" and i != "C":
            cp_string += i
    return cp_string
