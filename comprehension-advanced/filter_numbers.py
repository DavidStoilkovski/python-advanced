start_number = int(input())
end_number = int(input())

filter = [j for j in range(2, 11)]

filtered_numbers = [i for i in range(start_number, end_number + 1) if any(i % x == 0 for x in filter)]

print(filtered_numbers)
