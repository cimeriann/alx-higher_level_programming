#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    cp_list = []
    j = 0
    for item in my_list:
        cp_list.append(my_list[j])
        j += 1

    if idx > (len(my_list) - 1) or idx < 0:
        return cp_list
    cp_list[idx] = element
    return cp_list
