words = input().split(', ')

# result = [f'{word} -> {len(word)}' for word in words]

print(*[f'{word} -> {len(word)}' for word in words], sep=', ')