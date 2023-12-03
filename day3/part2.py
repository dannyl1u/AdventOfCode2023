from collections import defaultdict


def is_adjacent_to_gear(matrix, row, column_coords):
    for coord in column_coords:
        # up
        if row > 0 and matrix[row-1][coord] == '*':
            return [row-1, coord]
        # up left
        if row > 0 and coord > 0 and matrix[row-1][coord-1] == '*':
            return [row-1, coord-1]
        # left
        if coord > 0 and matrix[row][coord-1] == '*':
            return [row, coord-1]
        # left down
        if coord > 0 and row < len(matrix)-1 and matrix[row+1][coord-1] == '*':
            return [row+1, coord-1]
        # down
        if row < len(matrix)-1 and matrix[row+1][coord] == '*':
            return [row+1, coord]
        # right
        if coord < len(matrix[row])-1 and matrix[row][coord+1] == '*':
            return [row, coord+1]
        # down right
        if row < len(matrix)-1 and coord < len(matrix[row])-1 and matrix[row+1][coord+1] == '*':
            return [row+1, coord+1]
        # right up
        if coord < len(matrix[row])-1 and row > 0 and matrix[row-1][coord+1] == '*':
            return [row-1, coord+1]
    return -1

nums_with_gears = []
gears = defaultdict(list)
with open('input.txt', 'r') as file:
    input = file.read()
    input = input.strip()
    matrix = input.split("\n")

    for row in range(len(matrix)):
        cur_num = []
        column_coords = []
        for column in range(len(matrix[row])):
            if matrix[row][column].isnumeric():
                cur_num.append(matrix[row][column])
                column_coords.append(column)
            else:
                adjacent_coords = is_adjacent_to_gear(matrix, row, column_coords)
                if cur_num and adjacent_coords != -1:
                    number = int(''.join(cur_num))
                    gears[tuple(adjacent_coords)].append(number)
                cur_num = []
                column_coords = []

        adjacent_coords = is_adjacent_to_gear(matrix, row, column_coords)
        if cur_num and adjacent_coords != -1:
            number = int(''.join(cur_num))
            gears[tuple(adjacent_coords)].append(number)

for gear in gears:
    if len(gears[gear]) > 1:
        nums_with_gears.append(gears[gear])

cur_sum = 0
for nums in nums_with_gears:
    cur_product =1 
    for num in nums:
        cur_product *= num
    cur_sum += cur_product

print(cur_sum)