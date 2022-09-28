#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    conclusion = my_list[:]
    for status, i in enumerate(my_list):
        if i % 2 == 0:
            conclusion[status] = True
        else:
            conclusion[status] = False
    return conclusion
