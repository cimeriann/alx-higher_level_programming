#!/usr/bin/python3
def roman_to_int(roman_string):
    default_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    next = 0
    for i in range(len(stringtoconvert)):
        next = i+1 
        try: 
            if default_values[stringtoconvert[next]] > default_values[stringtoconvert[i]]:
                total += -1 * default_values[stringtoconvert[i]]
            else:
                total += default_values[stringtoconvert[i]]
        except IndexError:
            total += default_values[[-1]]
    return total
