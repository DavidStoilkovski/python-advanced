def read_input():
    size = int(input())

    matrix = []

    for _ in range(size):
        line = input()
        row = [el for el in line]
        matrix.append(row)

    return matrix


def find_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            el = matrix[row][column]
            if el == symbol:
                coordinates = (row, column)
                return coordinates


def print_result(coordinates, symbol):
    if coordinates:
        print(coordinates)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_input()
symbol = input()
coordinates = find_symbol(matrix, symbol)
print_result(coordinates, symbol)