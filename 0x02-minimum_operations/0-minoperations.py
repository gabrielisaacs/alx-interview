#!/usr/bin/python3


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n 'H' characters in a file.

    Args:
        n (int): The number of 'H' characters to achieve.

    Returns:
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
