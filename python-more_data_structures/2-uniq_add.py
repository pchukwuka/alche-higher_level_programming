#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert list to a set to remove duplicates, then sum the set
    return sum(set(my_list))
