n = int(input())

set_1 = set()
set_2 = set()

longest_intersection = []

for _ in range(n):

    set_1 = set()
    set_2 = set()

    line = input().split("-")

    first = line[0].split(',')

    first_start = int(first[0])
    first_end = int(first[1])

    second = line[1].split(',')

    second_start = int(second[0])
    second_end = int(second[1])

    for i in range(first_start, first_end + 1):
        set_1.add(i)

    for j in range(second_start, second_end + 1):
        set_2.add(j)

    current_intersection = set_1.intersection(set_2)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = []
        for el in current_intersection:
            longest_intersection.append(el)

print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')