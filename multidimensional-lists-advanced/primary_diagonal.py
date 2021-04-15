def read_input():
    size = int(input())

    matrix = []

    for row in range(size):
        line = input().split()
        row = []
        for column in line:
            row.append(int(column))
        matrix.append(row)

    return matrix


def sum_primary_diagonal(matrix):
    size = len(matrix)
    sum_diagonal = []

    for row in range(size):
        current = matrix[row][row]

        sum_diagonal.append(current)
    return sum_diagonal


matrix = read_input()
sum_diagonal = sum_primary_diagonal(matrix)
print(sum(sum_diagonal))