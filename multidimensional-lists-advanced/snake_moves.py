def form_matrix(rows, columns, text):

    matrix = []

    current_row = ''
    i = 0
    for row in range(rows):
        for column in range(columns):
            current_row += (text[i])
            i += 1
            if i == len(text):
                i = 0
        matrix.append(current_row)
        current_row = ''

    return matrix


def print_result(matrix):
    for i in range(len(matrix)):
        if i % 2 == 1:
            print(matrix[i][::-1])
        else:
            print(matrix[i])


(rows, columns) = (int(el) for el in input().split())
text = input()
matrix = form_matrix(rows, columns, text)
print_result(matrix)

