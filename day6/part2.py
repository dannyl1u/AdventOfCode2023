times = int("".join(open('input.txt').read().split("\n")[0].split()[1:]))
distance = int("".join(open('input.txt').read().split("\n")[1].split()[1:]))

print(times)
print(distance)

num_ways = []

num_ways_per_boat = 0

for button_time in range(times):
    travelled_distance = button_time * (times - button_time)
    if travelled_distance > distance:
        num_ways_per_boat += 1

num_ways.append(num_ways_per_boat)

result = 1
for x in num_ways:
    result *= x

print(result)