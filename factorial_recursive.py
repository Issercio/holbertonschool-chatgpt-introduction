#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number. Returns 1 if n is 0 (base case).
    """
    if n == 0:  # Base case: the factorial of 0 is 1
        return 1
    else:  # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Get the integer input from the command line arguments, calculate the factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
