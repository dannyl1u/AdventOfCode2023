game_num = 1
total_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(' ')

        colors = {}

        for i in range(2, len(line)-1, 2):
            if 'red' in line[i+1]:
                colors['red'] = max(colors.get('red', 0), int(line[i]))
            elif 'green' in line[i+1]:
                colors['green'] = max(colors.get('green', 0), int(line[i]))
            elif 'blue' in line[i+1]:
                colors['blue'] = max(colors.get('blue', 0), int(line[i]))

        line_score = colors['red'] * colors['green'] * colors['blue']
        total_score += line_score

print(total_score)