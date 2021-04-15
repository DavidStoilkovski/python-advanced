rows, columns = [int(num) for num in input().split()]

matrix = [[f'{chr(el)}{chr(ch)}{chr(el)}' for ch in range(el, el + columns)] for el in range(97, 97 + rows)]

[print(' '.join(row)) for row in matrix]