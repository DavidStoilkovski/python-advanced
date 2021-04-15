from collections import deque

all_kids = input().split()
step = int(input())

q = deque(all_kids)

while len(q) > 1:
    for _ in range(step - 1):
        q.append(q.popleft())
    print(f'Removed {q.popleft()}')

print(f'Last is {q.popleft()}')
