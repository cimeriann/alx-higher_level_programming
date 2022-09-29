#!/usr/bin/python3
def roman_to_int(roman_string):
    default_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    next = 0
    if type(roman_string) != str or roman_string == None:
        return 0
    for i in range(len(roman_string)):
        next = i+1
        try:
            if default_values[roman_string[next]] > default_values[roman_string[i]]:
                total += -1 * default_values[roman_string[i]]
            else:
                total += default_values[roman_string[i]]
        except IndexError:
            total += default_values[[-1]]
    return total
