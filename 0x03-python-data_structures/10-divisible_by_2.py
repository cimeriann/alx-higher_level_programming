#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    conclusion = []
    for i in my_list:
        if i % 2 == 0:
            conclusion.append(True)
        else:
           conclusion.append(False)
    return conclusion
