def read_input(rows):
    matrix = []

    for row in range(rows):
        line = [el for el in input().split()]
        matrix.append(line)

    return matrix


def find_square(matrix, rows, columns):
    column_border = columns - 1
    row_border = rows - 1
    count_set = set()
    count = 0

    for row in range(row_border):
        for column in range(column_border):
            count_set.add(matrix[row][column])
            count_set.add(matrix[row][column + 1])
            count_set.add(matrix[row + 1][column])
            count_set.add(matrix[row + 1][column + 1])
            if len(count_set) == 1:
                count += 1
            count_set = set()
    return count


(rows, columns) = (int(el) for el in input().split())

matrix = read_input(rows)
count = find_square(matrix, rows, columns)
print(count)
