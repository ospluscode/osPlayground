
# Rotate a given NxN matrix 90 degrees - this has a O(n*n) time complexity

# 1 2 3     7 4 1     as you can see columns become rows when we rotate 90 degrees
# 4 5 6  => 8 5 2     and we need to take into consideration the layers of matrix
# 7 8 9     9 6 3

def rotateMatrix(matrix):
    # Matrix is a two dimensional array, so need to find its length
    n = len(matrix)
    # Matrix las 2 layers (len divided by 2 floor gives this)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        # Doing the rotation of matrix layer
        for i in range(first, last):
            # save top left
            top = matrix[layer][i]

            # move top left to top right
            matrix[i][-layer-1] = top

            # move bottom left to top left
            matrix[layer][i] = matrix[-i-1][layer]

            # move bottom right to bottom left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            # move top right to bottom right
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

    return matrix