"""
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only call
to is_substring method (e.g. 'waterbottle' is a rotation of 'erbottlewat').
"""


def is_substring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False


def is_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    return False


print(is_rotation('waterbottle', 'erbottlewat'))
