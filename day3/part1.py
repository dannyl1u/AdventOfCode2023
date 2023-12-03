def is_adjacent_to_symbol(matrix, row, column_coords):
    for coord in column_coords:
        # up
        if row > 0 and not matrix[row-1][coord].isnumeric() and matrix[row-1][coord] != '.':
            return True
        # up left
        if row > 0 and coord > 0 and not matrix[row-1][coord-1].isnumeric() and matrix[row-1][coord-1] != '.':
            return True
        # left
        if coord > 0 and not matrix[row][coord-1].isnumeric() and matrix[row][coord-1] != '.':
            return True
        # left down
        if coord > 0 and row < len(matrix)-1 and not matrix[row+1][coord-1].isnumeric() and matrix[row+1][coord-1] != '.':
            return True
        # down
        if row < len(matrix)-1 and not matrix[row+1][coord].isnumeric() and matrix[row+1][coord] != '.':
            return True
        # right
        if coord < len(matrix[row])-1 and not matrix[row][coord+1].isnumeric() and matrix[row][coord+1] != '.':
            return True
        # down right
        if row < len(matrix)-1 and coord < len(matrix[row])-1 and not matrix[row+1][coord+1].isnumeric() and matrix[row+1][coord+1] != '.':
            return True
        # right up
        if coord < len(matrix[row])-1 and row > 0 and not matrix[row-1][coord+1].isnumeric() and matrix[row-1][coord+1] != '.':
            return True
    return False

nums_list = []
with open('input.txt', 'r') as file:
    input = file.read()
    input = input.strip()
    matrix = input.split("\n")

    for row in range(len(matrix)):
        nums_in_line = []
        cur_num = []
        column_coords = []
        for column in range(len(matrix[row])):
            if matrix[row][column].isnumeric():
                cur_num.append(matrix[row][column])
                column_coords.append(column)
            else:
                if cur_num and is_adjacent_to_symbol(matrix, row, column_coords):
                    nums_in_line.extend([int(''.join(cur_num))])
                cur_num = []
                column_coords = []

        if cur_num and is_adjacent_to_symbol(matrix, row, column_coords):
            nums_in_line.extend([int(''.join(cur_num))])

        nums_list.extend(nums_in_line)

print(sum(nums_list))