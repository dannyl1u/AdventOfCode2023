from collections import defaultdict

nums_list = []

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

word_to_int = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9
}

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
    
        nums_in_line = defaultdict(list)

        for digit in digits:
            start = 0
            if digit in line:
                while start < len(line):
                    index = line.find(digit, start)
                    if index == -1:
                        break
                    else:
                        nums_in_line[word_to_int[digit]].append(index)
                        start = index + 1

        for index, character in enumerate(line):
            if character.isdigit():
                nums_in_line[int(character)].append(index) 

        min_value = 9223372036854775807
        max_value = -1
        min_key = 10
        max_key = -1

        for key, value in nums_in_line.items():
            for num in value:
                if num < min_value:
                    min_value = num
                    min_key = key
                if num > max_value:
                    max_value = num
                    max_key = key

        print(min_key, max_key)
        nums_list.append(min_key*10 + max_key)
        
print(sum(nums_list))