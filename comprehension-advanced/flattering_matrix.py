n = int(input())

matrix = []

matrix = [map(int, input().split(', ')) for _ in range(n)]

flatten_matrix = [el for row in matrix for el in row]

print(flatten_matrix)