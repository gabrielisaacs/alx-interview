#!/usr/bin/python3

"""
    Function to determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result
    in exactly n 'H' characters in a file.
    args:
        n (int): The number of 'H' characters to achieve.
    returns:
        int: The minimum number of operations needed to achieve n 'H'.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Keep dividing n by the smallest possible divisors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
