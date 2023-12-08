times = (41, 77, 70, 96)
distances = (249, 1362, 1127, 1011)

total = 1

for i in range(4):
    s = 0
    for j in range(times[i]):
        if (times[i]-j)*j > distances[i]:
            s += 1
    total *= s

print(total)