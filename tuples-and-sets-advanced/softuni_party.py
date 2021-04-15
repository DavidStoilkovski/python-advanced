n = int(input())
reservation_list = set()

for _ in range(n):
    reservation_list.add(input())

line = input()

guests_arrived = set()

while not line == "END":
    guests_arrived.add(line)

    line = input()

guest_not_arrived = set(reservation_list).difference(guests_arrived)

VIP_guest = []


def VIP_filter(guest):
    for guest in guest_not_arrived:
        if guest[0].isdigit():
            VIP_guest.append(guest)


regular_guests = []


def filter_regular_guests(guest):
    for guest in guest_not_arrived:
        if not guest[0].isdigit():
            regular_guests.append(guest)


def print_result(VIP_guest, regular_guests):
    VIP_guest = sorted(VIP_guest)
    regular_guests = sorted(regular_guests)

    print(len(guest_not_arrived))

    for guest in VIP_guest:
        print(guest)

    for guest in regular_guests:
        print(guest)


VIP_filter(guests_arrived)
filter_regular_guests(guests_arrived)

print_result(VIP_guest, regular_guests)