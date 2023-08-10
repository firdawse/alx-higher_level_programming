#!/usr/bin/python3

import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    add = 0

    for i, arg in enumerate(args):
        add += int(arg)
    
    print("{}".format(add))
