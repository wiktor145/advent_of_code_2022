max_cal = -1
curr_sum = 0

with open("input.txt", "r") as f:
    for line in f:
        if line != '\n':
            curr_sum += int(line)
        else:
            if max_cal < curr_sum:
                max_cal = curr_sum
            curr_sum = 0

print(max_cal)
