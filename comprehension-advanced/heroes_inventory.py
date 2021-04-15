heroes = {name: {} for name in input().split(', ')}

line = input()

while not line == "End":

    name, item, price = line.split('-')

    if item not in heroes[name]:
        heroes[name][item] = int(price)

    line = input()

print(*[f'{hero} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}' for hero, inventory in heroes.items()], sep='\n')