bunker = {category: [] for category in input().split(', ')}

n = int(input())
bunker['all_items_count'] = 0
bunker['all_items_quantity'] = 0
for _ in range(n):

    category, item_name, item_params = input().split(' - ')

    quantity, quality = [int(el.split(":")[1]) for el in item_params.split(';')]

    item_data = {item_name: {'quantity': quantity, 'quality': quality}}

    bunker[category].append(item_data)

    bunker['all_items_count'] += quantity
    bunker['all_items_quantity'] += quality


print(f'Count of items: {bunker["all_items_count"]}')
print(f'Average quality: {(bunker["all_items_quantity"]/(len(bunker)-2)):.2f}')
print(*[f'{category} -> {", ".join([list(d.keys())[0] for d in item])}' for category, item in bunker.items() if isinstance(bunker[category], list)], sep = '\n')