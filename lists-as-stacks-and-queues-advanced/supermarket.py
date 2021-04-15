from collections import deque

PAID_COMMAND = "Paid"
END_COMMAND = "End"

queue = deque()

while True:
    command = input()

    if command == PAID_COMMAND:
        while queue:
            print(queue.popleft())

    elif command == END_COMMAND:
        print(f'{len(queue)} people remaining.')
        break

    else:
        queue.append(command)