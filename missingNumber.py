
# Find the missing number in an integer array of 1 to 100
# Here I utilize n*(n+1) / 2 formula to calculate sum of n numbers

def findMissingNumber(list, n):
    sumWithFormula = n * (n+1) / 2
    sumList = sum(list)
    return sumWithFormula - sumList