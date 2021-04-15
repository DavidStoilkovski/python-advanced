line = input()

phonebook = {}

while not line.isdigit():
    user, number = line.split("-")

    phonebook[user] = number

    line = input()

n = int(line)

for _ in range(n):

    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")

    else:
        print(f'Contact {name} does not exist.')