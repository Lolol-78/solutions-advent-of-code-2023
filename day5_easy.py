f = open('day5_input.txt')

seeds_line = f.readline()

seeds = [list(map(int, seeds_line[seeds_line.index(':')+2:seeds_line.index('\n')].split()))]

print(seeds)

f.readline()

maps = []

for i in range(7):
    seeds.append([-1 for _ in range(len(seeds[0]))])
    f.readline()
    current_line = f.readline()
    while current_line != '\n' and current_line != '':
        current_line = tuple(map(int, current_line.split()))
        for j in range(len(seeds[0])):
            if current_line[1] <= seeds[i][j] <= current_line[1]+current_line[2]:
                seeds[i+1][j] = current_line[0] + seeds[i][j] - current_line[1]
        for j in range(len(seeds[0])):
            if seeds[i+1][j] == -1:
                seeds[i+1][j] = seeds[i][j]
        current_line = f.readline()

print(min(seeds[-1]))

f.close()