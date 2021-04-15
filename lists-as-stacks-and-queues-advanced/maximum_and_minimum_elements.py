n = int(input())

stack = []

for i in range(n):

    command = input()

    if command.startswith('1'):
        element = int(command.split()[1])
        stack.append(element)

    if len(stack) > 0:
        if command.startswith('2'):
            stack.pop()

        elif command.startswith('3'):
            print(max(stack))

        elif command.startswith('4'):
            print(min(stack))
result = []

while stack:
    result.append(str(stack.pop()))

print(", ".join(result))

