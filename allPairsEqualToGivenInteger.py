
# Find all pairs in array of integers whose sum is equal to given integer
# The solution has O(n*n) time complexity

def findAllPairs(list, sum):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == sum:
                print(list[i] + list[j])