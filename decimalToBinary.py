
# a recursive function to convert decimal to binary
# we divide decimal by 2 to convert
# f(n) = n mod 2 + 10*f(n/2)

def decimalToBinary(n):
    if n == 0:
        return 1
    else:
        return n%2 + 10 * decimalToBinary(n/2)
