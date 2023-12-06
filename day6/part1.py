times = [int(item) for item in open('input.txt').read().split("\n")[0].split()[1:]]
distance = [int(item) for item in open('input.txt').read().split("\n")[1].split()[1:]]

num_ways = []

for i in range(len(times)):
    time = times[i]
    distance_to_beat = distance[i]

    num_ways_per_boat = 0

    for button_time in range(time):
        travelled_distance = button_time * (time - button_time)
        if travelled_distance > distance_to_beat:
            num_ways_per_boat += 1
    
    num_ways.append(num_ways_per_boat)

result = 1
for x in num_ways:
    result *= x

print(result)