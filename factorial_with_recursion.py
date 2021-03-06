"""
Calculate factorial of the given number using recursion
"""


def factorial_recursion(num):
    if num < 0:
        return -1
    elif num == 0:
        return 1
    else:
        return num * factorial_recursion(num - 1)


print factorial_recursion(6)
