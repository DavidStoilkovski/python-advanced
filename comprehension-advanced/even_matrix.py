def read_input():
    n = int(input())

    matrix = []
    matrix = [map(int, input().split(', ')) for _ in range(n)]

    return matrix


def find_even(matrix):
    find_even = [[el for el in row if el % 2 == 0] for row in matrix]
    return find_even


matrix = read_input()
even = find_even(matrix)

print(even)

