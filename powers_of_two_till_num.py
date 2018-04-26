"""
Print powers of 2 from 2 till input number inclusively with recursion
"""


def powers_of_two(num):
    if num < 1:
        return 0
    elif num == 1:
        print 1
        return 1
    else:
        prev = powers_of_two(num / 2)
        curr = prev * 2
        print curr
        return curr


powers_of_two(128)