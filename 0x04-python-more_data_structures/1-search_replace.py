#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = []
    i = len(tmp)
    for x in my_list:
        tmp.append(x)
        i += 1
    n_list = tmp
    z = 0
    for y in n_list:
        if n_list[z] == search:
            n_list[z] = replace
        z += 1
    return n_list
    #return (list(map(lambda x: replace if x is search else x, my_list)))        
