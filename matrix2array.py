def matrix_to_array(matrix):
    new_array = [None] * (len(matrix) * len(matrix[0]))

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new_array[i * len(matrix[0]) + j] = matrix[i][j]

    return new_array


def array_to_matrix(array_1d, width):  # width = n cols
    new_matrix = [[None for x in range(0, len(array_1d)/width)] for y in range(0, width)]

    for i in range(0, len(array_1d)):
        new_matrix[i/width][i%width] = array_1d[i]

    return new_matrix
