n, m = input().split()
n = int(n)
m = int(m)

set_n = set()
set_m = set()


def forming(n, m):

    for _ in range(n):
        set_n.add(input())

    for _ in range(m):
        set_m.add(input())


def print_result(set_n, set_m):
    union = set_n.intersection(set_m)
    for el in union:
        print(el)


forming(n, m)
print_result(set_n, set_m)