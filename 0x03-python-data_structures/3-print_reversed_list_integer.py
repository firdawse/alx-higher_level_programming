#!/usr/bin/python3

def print_reversed_list_string(my_list=[]):
    if isinstance(my_list, list):
        for e in reversed(my_list):
            print("{}".format(e))
