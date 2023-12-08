#
#  NE FONCTIONNE PAS
#


f = open('day5_input.txt')

seeds_line = f.readline()

first_line = list(map(int, seeds_line[seeds_line.index(':')+2:seeds_line.index('\n')].split()))

seeds = []

f.readline()

maps = []

for i in range(7):
    current_map = []
    f.readline()
    current_line = f.readline()
    while current_line != '\n' and current_line != '':
        current_line = tuple(map(int, current_line.split()))
        current_map.append(current_line)
        current_line = f.readline()
    maps.append(current_map)


def main():
    min_destination = 51580674
    notFound = True
    while notFound:
        min_destination += 1
        min_dest_found = False
        for i in range(len(maps[-1])):
            if maps[-1][i][0] <= min_destination <= maps[-1][i][0] + maps[-1][i][2] and not min_dest_found:
                min_source = min_destination - maps[-1][i][0] + maps[-1][i][1]
                min_dest_found = True

        source = min_source
        
        for i in range(6):
            has_changed = False
            for j in range(len(maps[-2-i])):
                if maps[-2-i][j][0] <= source <= maps[-2-i][j][0] + maps[-2-i][j][2] and not has_changed:
                    source += maps[-2-i][j][1] - maps[-2-i][j][0]
                    has_changed = True

        for i in range(len(first_line)//2):
            if first_line[i*2] <= source <= first_line[i*2]+first_line[i*2+1]:
                notFound = False
        
        #print(min_destination, min_source) 

    print(min_destination)

main()

f.close()