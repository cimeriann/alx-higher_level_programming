#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp_dict = my_dict.copy()
    for k, v in my_dict.items():
        if v == value:
            del tmp_dict[k]
    return tmp_dict
