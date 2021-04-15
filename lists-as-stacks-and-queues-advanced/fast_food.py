from collections import deque

capacity = int(input())

q = deque(input().split())

is_completed = True
find_max = []

for el in q:
    find_max.append(int(el))

print(max(find_max))

while q:
    current = q.popleft()

    if capacity < int(current):
        is_completed = False
        break

    capacity -= int(current)

if is_completed:
    print('Orders complete')

else:
    left = []
    left.append(current)

    while q:
        left.append(q.popleft())

    print(f'Orders left: {" ".join(left)}')