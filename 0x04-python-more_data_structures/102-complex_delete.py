#!/usr/bin/python3
def complex_delete(my_dict, value):
    for keys in my_dict.copy():
        if my_dict[keys] == value:
            del my_dict[keys]
    return my_dict
