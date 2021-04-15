n = int(input())

odd_set = set()
even_set = set()

for current_line in range(1, n+1):
    name = input()
    current_sum = sum(ord(el) for el in name) // current_line

    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)


even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    modified_set = [str(el) for el in even_set.union(odd_set)]
    print(', '.join(modified_set))
elif odd_set_sum > even_set_sum:
    modified_set = [str(el) for el in odd_set.difference(even_set)]
    print(', '.join(modified_set))
else:
    modified_set = [str(el) for el in odd_set.symmetric_difference(even_set)]
    print(', '.join(modified_set))