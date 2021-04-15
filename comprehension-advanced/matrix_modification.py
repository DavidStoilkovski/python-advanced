n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n) ]

line = input()


while not line == "END":

    command, initial_row, initial_column, value = line.split()
    initial_row = int(initial_row)
    initial_column = int(initial_column)
    value = int(value)

    if 0 <= initial_row < n and 0 <= initial_column < n:

        if command == "Add":
            matrix[initial_row][initial_column] += value
        elif command == "Subtract":
            matrix[initial_row][initial_column] -= value

    else:
        print("Invalid coordinates")

    line = input()

matrix = [[str(num) for num in row] for row in matrix]

[print(' '.join(row)) for row in matrix]