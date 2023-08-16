#!/usr/bin/python3

def best_score(a_dict):
    if not a_dict:
        return None
    return max(a_dict, key=a_dict.get)
