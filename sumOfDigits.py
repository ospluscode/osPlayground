
# a recursive function to calculate sum of digits of a positive integer
def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))