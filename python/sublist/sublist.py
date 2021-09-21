"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    if is_suplist(list_one, list_two) and is_suplist(list_two, list_one):
        return EQUAL
    elif is_suplist(list_one, list_two):
        return SUPERLIST
    elif is_suplist(list_two, list_one):
        return SUBLIST
    elif not (list_one or list_two):
        return EQUAL
    else:
        return UNEQUAL

def is_suplist(l1, l2):
    if any([l2 == l1[i:i+len(l2)] for i in range(len(l1))]):
        return True