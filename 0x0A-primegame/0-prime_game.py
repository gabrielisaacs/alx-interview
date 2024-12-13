#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    Args:
        x (int): Number of rounds
        nums (list): Array of n for each round
    Returns:
        str: Name of the player that won the most rounds (Maria or Ben)
        None: If the winner cannot be determined
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0
    # Find the maximum value in nums to optimize prime calculation
    n = max(nums)
    # Create a list of primes up to max(nums)
    # Using Sieve of Eratosthenes
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0] = primes[1] = False
    for i in range(2, int(pow(n, 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Count primes up to each number in nums
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if primes[i])
        # If the count of primes is even, Ben wins
        # If the count of primes is odd, Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
