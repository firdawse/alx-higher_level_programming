#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args != 1 :
        ending = "s" 
    else :
        ending = ""

    print("{} argument{}".format(num_args, ending), end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(args):
            print("{}: {}".format(i+1, arg))
