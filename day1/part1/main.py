nums_list = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        num_count = 0
        nums_in_line = []
        for character in line:
            try:
                value = int(character)
                nums_in_line.append(value)
            except ValueError:
                pass
        nums_list.append(nums_in_line[0]*10 + nums_in_line[-1])

print(sum(nums_list))