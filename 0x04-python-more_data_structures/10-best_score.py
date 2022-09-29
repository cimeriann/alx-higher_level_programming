#!/usr/bin/python3
def best_score(my_dict):
    highest_score = 0
    name = ""
    for key in my_dict:
        if my_dict[key] > highest_score:
            highest_score = my_dict[key]
            name = key
    if highest_score == 0:
        return None
    return name
