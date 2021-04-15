n = int(input())

username_list = set()

for _ in range(n):
    username = input()
    username_list.add(username)


def print_result(username_list):
    for user in username_list:
        print(user)

print_result(username_list)