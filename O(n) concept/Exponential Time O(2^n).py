# Exponential Time: O(2^n)
# The operation time doubles with each additional element in the input.
# Example: Solving the traveling salesman problem using brute force.

def fibonacci_exponential(n):
    if n <= 1:
        return n
    else:
        return fibonacci_exponential(n-1) + fibonacci_exponential(n-2)


