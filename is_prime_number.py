"""
Check if given number is prime or not and return True or False.
"""


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in xrange(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for n in xrange(100):
    print 'Number:', n, 'Is prime?', is_prime(n)
