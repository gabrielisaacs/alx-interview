#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    Args:
        coins (list): List of coin values available
        total (int): Target amount to make change for
    Returns:
        int: Fewest number of coins needed, -1 if total cannot be met
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0
    # Sort coins in descending order for optimization
    coins.sort(reverse=True)
    # Initialize dp array with total + 1 (impossible value)
    # dp[i] represents the minimum coins needed for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    # Fill dp array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # Return result
    return dp[total] if dp[total] != float('inf') else -1
