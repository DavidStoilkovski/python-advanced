n = int(input())

set_elements = set()


def forming_set(n):

    for _ in range(n):
        line = input().split()

        for el in line:
            set_elements.add(el)


def print_result(set_elements):

    for el in set_elements:
        print(el)


forming_set(n)
print_result(set_elements)