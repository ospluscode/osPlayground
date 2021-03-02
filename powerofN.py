
# a recursive function to calculate power(x) of a number(n)
def powerOfNumber(n, x):
    if x == 0:
        return 1
    if x == 1:
        return n
    else:
        return n * powerOfNumber(n, x-1)