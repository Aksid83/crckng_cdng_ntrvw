"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, 'aabcccccaaa' -> 'a2b1c5a3'. If the compressed string would not become smaller, should
return original string.
"""


def compress_string(string):
    compressed = []
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed.append(string[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    if len(compressed) > len(string):
        return string
    else:
        return ''.join(compressed)


print(compress_string('aabcccccaaa'))
print(compress_string('qwertyasdf'))
