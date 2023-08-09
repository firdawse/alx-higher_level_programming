#!/usr/bin/python3

for i in range(0, 90):
    if i == 89:
        print("{}".format(i))
    elif int(i/10) == i%10 or int(i/10)> i%10:
        continue
    else:
        print("{:02d}".format(i), end=", ")
