#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    index = 0
    for char in str:
        if (index != n):
            new_string += char
        index += 1
    return new_string
