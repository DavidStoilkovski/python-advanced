line = input().split('|')[::-1]

result = [el.split() for el in line]

[print(*el, end=" ") for el in result if len(el) > 0]