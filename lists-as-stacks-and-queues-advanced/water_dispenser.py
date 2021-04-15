from collections import deque

liters_in_dispenser = int(input())

START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = "refill"

waiting_list = deque()

command = input()

while not command == START_COMMAND:
    waiting_list.append(command)
    command = input()

while True:

    command = input()

    if command.startswith(REFILL_COMMAND):
        liters = int((command.split())[1])
        liters_in_dispenser += liters

    elif command == END_COMMAND:
        print(f'{liters_in_dispenser} liters left')
        break

    else:
        needed = int(command)

        if needed > liters_in_dispenser:
            print(f'{waiting_list.popleft()} must wait')
        else:
            print(f'{waiting_list.popleft()} got water')
            liters_in_dispenser -= needed
