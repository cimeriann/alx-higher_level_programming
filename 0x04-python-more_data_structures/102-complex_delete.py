#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp_dict = my_dict.copy()
    for k, v in my_dict.items():
        if v == value:
            del tmp_dict[k]
    return tmp_dict
