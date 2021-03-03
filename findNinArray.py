
# Find a number in an array
# Usually we use different libraries to find a number in an array
# But here I am implementing my own find function - linear search
# This has time complexity of O(n)

def findN(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return i