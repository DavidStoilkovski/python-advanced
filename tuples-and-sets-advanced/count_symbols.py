text = input()

count_symbols = {}

for ch in text:
    if ch not in count_symbols:
        count_symbols[ch] = 0
    count_symbols[ch] += 1

count_symbols = sorted(count_symbols.items(), key=lambda x: x[0])


def print_result(count_symbols):
    for (symbol, value) in count_symbols:
        print(f'{symbol}: {value} time/s')


print_result(count_symbols)