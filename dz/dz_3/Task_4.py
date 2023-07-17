all_items = {
    "тент":2,
    "Спальник":1.5,
    "еда":1,
    "вода":2,
    "ручка":0.1,
    "тетрадь":0.2

}

def first_items_in_back(items, max_x):
    box = []
    all_weight = 0

    sorted_items = sorted(items.items(), key= lambda x : x[1], reverse=True)

    for thing, weight in sorted_items:
        if all_weight + weight <= max_x:
            box.append(thing)
            all_weight += weight

    return box, all_weight

max_weight = 5
backpack, total_weight = first_items_in_back(all_items,max_weight)
print (" В рюкзак уместиться")
for item in backpack:
    print(item)
print(f"Загрузка {total_weight}/{max_weight}")