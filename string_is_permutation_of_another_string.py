"""
Given two strings, write a method to check if one is a permutation of another
"""


# Solution 1: sort strings and compare
def is_string_permutation_sorting(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)


print('Test Solution 1')
print(is_string_permutation_sorting('god', 'dog'))
