#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number n using recursion.

    Parameters:
    n (int): The non-negative integer to calculate the factorial of.

    Returns:
    int: The factorial of the given number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the integer from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
# Print the result
print(f)



