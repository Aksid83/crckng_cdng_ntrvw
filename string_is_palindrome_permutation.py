"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
"""


def is_palindrome_permutation(phrase):
    if not isinstance(phrase, str):
        return False
    chars_frequency = count_char_frequency(phrase)
    return check_max_one_odd(chars_frequency)


def count_char_frequency(string):
    char_freq = {}
    for c in string:
        if c == ' ':
            continue
        char_freq[c] = string.count(c)
    return char_freq


def check_max_one_odd(table):
    found_odd = False
    for count in table.keys():
        if table[count] % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


print(is_palindrome_permutation('taco cat'))



