
# Find maximum products if two integers in all positive array
# The solution time complexity is O(n*n)

def findMaxProduct(array):
    max = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
           if array[i] * array[j] > max:
               max = array[i] * array[j]
    return max