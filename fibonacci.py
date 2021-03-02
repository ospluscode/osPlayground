
# a recursive function to find fibonacci sequence of n
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Make sure n is a positive integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)