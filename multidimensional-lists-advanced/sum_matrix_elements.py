def read_input():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for row in range(rows):
        line = list(map(int, input().split(", ")))
        matrix.append(line)

    return matrix


def sum_matrix(matrix):
    our_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            our_sum += matrix[i][j]

    return our_sum


matrix = read_input()
our_sum = sum_matrix(matrix)

print(our_sum)
print(matrix)
