n = int(input())

parking_lot = set()


def print_result(registration):
    if parking_lot:
        for registration in parking_lot:
            print(registration)
    else:
        print('Parking Lot is Empty')


for _ in range(n):
    command, registration = input().split(", ")

    if command == "IN":
        parking_lot.add(registration)
    else:
        parking_lot.remove(registration)

print_result(parking_lot)
