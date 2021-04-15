expression = input()

stack = []

for i in range(len(expression)):

    if expression[i] == "(":
        stack.append(i)

    elif expression[i] == ")":
        j = stack.pop()
        print(expression[j:i + 1])