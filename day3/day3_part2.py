def get_item_type_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


GROUP_SIZE = 3

groups = []
current_group = []

with open("input.txt", "r") as file:
    for line in file:
        current_group.append(line.strip())
        if len(current_group) == GROUP_SIZE:
            groups.append(current_group.copy())
            current_group = []

priorities_sum = 0


def all_other_groups_contains(item_type, group):
    for i in range(1, len(group)):
        if item_type not in group[i]:
            return False

    return True


def get_badge_item_type(group):
    first_sack = group[0]
    for i in range(len(first_sack)):
        if all_other_groups_contains(first_sack[i], group):
            return first_sack[i]


for group in groups:
    badge_item_type = get_badge_item_type(group)
    priorities_sum += get_item_type_priority(badge_item_type)

print(f'Priorities sum: {priorities_sum}')
