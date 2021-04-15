def read_input():
    matrix = []

    for row in range(rows):
        matrix.append(input().split())

    return matrix


def print_result(matrix, rows):
    for row in range(rows):
        print(" ".join(matrix[row]))

def shuffle(matrix, rows, columns):
    line = input()
    while not line == "END":
        line = line.split()
        temp = ""
        if len(line) == 5:
            command = line[0]
            if command == "swap":
                first_el_index_x = int(line[1])
                first_el_index_y = int(line[2])
                second_el_index_x = int(line[3])
                second_el_index_y = int(line[4])
                if 0 <= first_el_index_x < rows \
                   and 0 <= second_el_index_x < rows \
                    and 0 <= first_el_index_y < columns \
                    and 0 <= second_el_index_y < columns:
                    temp_el = matrix[first_el_index_x][first_el_index_y]
                    matrix[first_el_index_x][first_el_index_y] = matrix[second_el_index_x][second_el_index_y]
                    matrix[second_el_index_x][second_el_index_y] = temp_el
                    print_result(matrix, rows)
                else:
                    print('Invalid input!')
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')


        line = input()


(rows, columns) = (int(el) for el in input().split())
matrix = read_input()
result = shuffle(matrix, rows, columns)