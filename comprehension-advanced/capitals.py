countries = input().split(', ')
capitals = input().split(', ')

result = [f'{countries[i]} -> {capitals[i]}' for i in range(len(capitals))]

[print(res) for res in result]
