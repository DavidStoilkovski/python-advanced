line = tuple(map(float, input().split()))

occurance_of_numbers = {}

for num in line:
    if num not in occurance_of_numbers:
        occurance_of_numbers[num] = 0
    occurance_of_numbers[num] += 1

for (number, occurance) in occurance_of_numbers.items():
    print(f'{number} - {occurance} times')