#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
    
def uppercase(s):
    output = ""
    for i in range(len(s)):
        if islower(s[i]):
            output += chr(ord(s[i]) - 32)  # Fixed this line
        else:
            output += s[i]  # Fixed this line
    print("{}".format(output))
