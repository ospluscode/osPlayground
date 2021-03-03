
# Find if a list has all unique characters

def isListUnique(list):
    empty_list = []
    for i in range(len(list)):
        if list[i] in empty_list:
            return false
        else:
            empty_list.append(list[i])
    return true