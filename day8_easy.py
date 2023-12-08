f = open('day8_input.txt')

sequence = f.readline()[:-1]

print(sequence)

f.readline()

connections = {}

current = 'AAA'

for i in range(750):
    line = f.readline()
    
    left_and_right = tuple(line[line.index('(')+1:line.index(')')].split(', '))
    
    connections[line[:3]] = left_and_right

notArrived = True
i = -1

#print(connections)


while notArrived:
    i += 1
    #print(current, connections[current])
    current = connections[current][int(sequence[i%len(sequence)] == 'R')]
    
    
    if current == 'ZZZ':
        notArrived = False
        print(i)


print(current)

f.close()