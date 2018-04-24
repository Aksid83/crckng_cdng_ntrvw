"""
Reverse an array/list with looping only through half of given array/list
"""


def reverse(input_list):
    for i in xrange(len(input_list)/2):
        other = len(input_list) - i - 1
        temp = input_list[i]
        input_list[i] = input_list[other]
        input_list[other] = temp
    return input_list


list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list3 = ['re', 'ver', 'se']

print 'Example 1:'
print list1
print reverse(list1), '\n'
print 'Example 2:'
print list2
print reverse(list2), '\n'
print 'Example 3:'
print list3
print reverse(list3), '\n'
