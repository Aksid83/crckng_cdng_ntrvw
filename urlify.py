"""
Write a method to replace all the spaces in the given string with '%20'
"""


def urlify(string):
    if not isinstance(string, str):
        print('Input data is not a string.')
        return False
    return string.strip().replace(' ', '%20')


print(urlify('http://www.someaddress.com/some test link goes here      '))
