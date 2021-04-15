def read_input():
    (rows, columns) = map(int, input().split(", "))
    matrix = []

    for row in range(rows):
        line= input().split(" ")
        row = []

        for column in range(columns):
            row.append(int(line[column]))

        matrix.append(row)

    return matrix


def sum_matrix_columns(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    sum_of_matrix = []

    for column in range(columns):
        sum = 0
        for row in range(rows):
            sum += matrix[row][column]

        sum_of_matrix.append(sum)

    return sum_of_matrix


def print_result(sum_of_matrix):

    for sum in sum_of_matrix:
        print(sum)


matrix = read_input()
sum_of_matrix = sum_matrix_columns(matrix)
print_result(sum_of_matrix)