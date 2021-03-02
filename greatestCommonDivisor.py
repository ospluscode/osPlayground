
# a recursive function to find GCD of two numbers
# Euclidean algorithm is used to find the GCD in mathematics
# gcd(48, 18) = 6
# 1. 48/18 = 2 (12)   2. 18/12 = 1 (6)   3. 12/6 = 2 this means gcd is 6
# Euclidean gives gcd(a, 0) = a which is the base case below

def gcd(a, b):
    # negative integer cases
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    # base case
    if b == 0:
        return a
    # recursive case
    else:
        return gcd(b, a%b)