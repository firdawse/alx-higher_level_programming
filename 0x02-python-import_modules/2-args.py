#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    ending = "s" if num_args != 1 else ""

    print("{} argument{}".format(num_args, ending), end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(args):
            print("{}: {}".format(i+1, arg))                      
