priorities_sum = 0


def split_items(line):
    return [line[i] for i in range(len(line.strip()) // 2)], \
        [line[i] for i in range(len(line.strip()) // 2, len(line.strip()))]


def get_duplicated_item_types(first_compartment_items, second_compartment_items):
    duplicates = set()

    for item in first_compartment_items:
        if item in second_compartment_items:
            duplicates.add(item)

    return duplicates


def get_item_type_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def get_priorities_sum(duplicated_item_types):
    priorities_sum = 0

    for item in duplicated_item_types:
        priorities_sum += get_item_type_priority(item)

    return priorities_sum


with open("input.txt", "r") as file:
    for line in file:
        first_compartment_items, second_compartment_items = split_items(line)
        duplicated_item_types = get_duplicated_item_types(first_compartment_items,
                                                          second_compartment_items)
        priorities_sum += get_priorities_sum(duplicated_item_types)

print(f'Priorities sum: {priorities_sum}')
