


# a recursive function to calculate factorial of n
def factorial(n):
    assert n >= 0 and int(n) == n, 'Make sure n is positive integer'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)
