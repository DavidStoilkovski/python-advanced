box = input().split()

capacity = int(input())
racks = 1
room_left = capacity

while box:

    current_piece = int(box.pop())

    if current_piece > room_left:
        racks += 1
        room_left = capacity

    room_left -= current_piece

print(racks)

