#!/usr/bin/python3

def multiply_by_2(a_dict):
    new_dict = {}
    for key in a_dict.keys():
        new_dict[key] = a_dict[key] * 2
    return new_dict
