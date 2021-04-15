from collections import deque

q = deque()

stations = int(input())

petrol_in_tank = 0

for _ in range(stations):
    petrol_distance_input = input()
    q.append(petrol_distance_input)

station_index = 0

our = q.copy()

while our:

    current = our.popleft()
    petrol, distance = current.split()
    petrol = int(petrol)
    distance = int(distance)
    petrol_in_tank += petrol

    if distance > petrol_in_tank:
        to_be_last = q.popleft()
        q.append(to_be_last)
        our = q.copy()
        station_index += 1
        petrol_in_tank = 0

    else:
        petrol_in_tank -= distance

print(station_index)
