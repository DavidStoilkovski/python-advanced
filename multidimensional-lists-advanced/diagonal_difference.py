def read_input(rows):
    matrix = []

    for row in range(rows):
        line = [int(el) for el in input().split()]
        matrix.append(line)

    return matrix


def diagonal_sum(matrix, rows):
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(rows):
        primary_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][rows - 1 - i]

    return abs(primary_diagonal - secondary_diagonal)


rows = int(input())
matrix = read_input(rows)
diagonal_difference = diagonal_sum(matrix, rows)
print(diagonal_difference)
