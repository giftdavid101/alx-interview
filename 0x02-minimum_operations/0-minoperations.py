#!/usr/bin/python3
"""min operattions """


def minOperations(n):
    """calculates the fewest number of operations"""

    if (n < 2):
        return 0
    op, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            op += root
            n = n / root
            root -= 1
        root += 1
    return op
