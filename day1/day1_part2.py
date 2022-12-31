cals = []
curr_sum = 0

with open("input.txt", "r") as f:
    for line in f:
        if line != '\n':
            curr_sum += int(line)
        else:
            cals.append(curr_sum)
            curr_sum = 0

cals.sort(reverse=True)
print(sum(cals[:3]))
