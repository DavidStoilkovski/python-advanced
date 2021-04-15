example = input()

stack = []
balance = True

mirror = {'{': '}', '[': ']', '(': ')'}

for el in example:

    if el in "{[(":
        stack.append(el)
    else:
        if not stack:
            balance = False
            break
        last = stack.pop()
        if not mirror[last] == el:
            balance = False
            break

if balance:
    print('YES')
else:
    print('NO')