game_num = 1
total_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(' ')

        isValid = True

        for i in range(2, len(line)-1, 2):
            if int(line[i]) > 12 and 'red' in line[i+1]:
                isValid = False
            elif int(line[i]) > 13 and 'green' in line[i+1]:
                isValid = False
            elif int(line[i]) > 14 and 'blue' in line[i+1]:
                isValid = False
        
        if isValid:
            total_score += game_num

        game_num += 1

print(total_score)