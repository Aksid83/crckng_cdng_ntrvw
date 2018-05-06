"""
There are three types of edits that can be performed on string: insert a character, remove a character,
or replace a character. Given two strings, write a function if they are one edit or 0 edits away.
"""


def one_away(string1, string2):
    if string1 == string2:
        return True
    if abs(len(string1) - len(string2)) > 1:
        return False
    if len(string1) > len(string2):
        s1, s2 = string1, string2
    else:
        s1, s2 = string2, string1
    index1, index2 = 0, 0
    found_difference = False
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if found_difference:
                return False
            found_difference = True
            if len(s1) == len(s2):
                index2 += 1
        else:
            index2 += 1
        index1 += 1
    return True


print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))

