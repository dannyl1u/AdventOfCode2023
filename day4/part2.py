nums_list = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        nums_list.append(line.split(' ')[2:])

winnings_list = []

for row in nums_list:
    row[:] = [x for x in row if x]
    winning_nums = []
    my_nums = []
    i = 0
    num_matches = 0
    while row[i] != '|':
        winning_nums.append(row[i])
        i += 1
    while i < len(row):
        my_nums.append(row[i])
        i += 1
    for num in my_nums:
        if num in winning_nums:
            num_matches += 1
            winning_nums.remove(num)
    winnings_list.append(num_matches)

copies = [1] * len(winnings_list)

for i, number in enumerate(winnings_list):
    for j in range(i + 1, i + number + 1):
        copies[j] += copies[i]

print(sum(copies))