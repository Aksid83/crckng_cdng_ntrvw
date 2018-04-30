"""
Implement an algorithm to check if given string has only unique characters
"""


def is_unique_char(string):
    char_set = set()
    for char in string:
        if char in char_set:
            print('String does not have all unique characters.')
            return False
        else:
            char_set.add(char)
    print('Great! All unique!')
    return True


print('Test 1')
print(is_unique_char('This is not unique string!'))

print('Test 2')
print(is_unique_char('qwertyuiopasdfghjklzxcvbnm'))

