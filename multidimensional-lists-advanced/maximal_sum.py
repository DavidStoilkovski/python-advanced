import sys


def read_input(rows):
    matrix = []

    for row in range(rows):
        line = [int(el) for el in input().split()]
        matrix.append(line)

    return matrix


def find_maximal_sum(matrix, rows, columns):
    column_border = columns - 2
    row_border = rows - 2
    sum_list = []
    max_sum = -sys.maxsize
    max_matrix = []

    for row in range(row_border):
        for column in range(column_border):
            sum_list.append(matrix[row][column])
            sum_list.append(matrix[row][column + 1])
            sum_list.append(matrix[row][column + 2])
            sum_list.append(matrix[row + 1][column])
            sum_list.append(matrix[row + 1][column + 1])
            sum_list.append(matrix[row + 1][column + 2])
            sum_list.append(matrix[row + 2][column])
            sum_list.append(matrix[row + 2][column + 1])
            sum_list.append(matrix[row + 2][column + 2])

            if sum(sum_list) > max_sum:
                max_sum = sum(sum_list)
                max_matrix = sum_list
            sum_list = []

    return (max_sum, max_matrix)


def print_result(max_sum_coordinates):
    print(f'Sum = {max_sum_coordinates[0]}')
    my_matrix = max_sum_coordinates[1]

    for i in range(len(my_matrix)):
        if i % 3 == 0 and i > 0:
            print()
        print(my_matrix[i], end=' ')


(rows, columns) = (int(el) for el in input().split())

matrix = read_input(rows)
max_sum_coordinates = find_maximal_sum(matrix, rows, columns)
print_result(max_sum_coordinates)
