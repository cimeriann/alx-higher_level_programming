#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    copy = []
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    for i in range(len(my_list)):
        if i != idx:
            copy.append(my_list[i])
    my_list = copy
    return my_list
