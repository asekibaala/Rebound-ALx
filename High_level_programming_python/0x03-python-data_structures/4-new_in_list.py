#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_in_list = my_list[:]
    if 0<= idx < length:
        new_in_list[idx] = element
        return new_in_list