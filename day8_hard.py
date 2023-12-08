f = open('day8_input.txt')

sequence = f.readline()[:-1]

f.readline()

connections = {}

currents = []

for i in range(750):
    line = f.readline()
    
    left_and_right = tuple(line[line.index('(')+1:line.index(')')].split(', '))
    
    connections[line[:3]] = left_and_right
    
    if line[2] == 'A':
        currents.append(line[:3])


print(currents)

notArrived = True
i = 0

while notArrived:
    
    notArrived = False
    i += 1
    
    for j in range(len(currents)):
        currents[j] = connections[currents[j]][int(sequence[(i-1)%len(sequence)] == 'R')]
        if currents[j][2] != 'Z':
            notArrived = True
    #print(currents, sequence[(i-1)%len(sequence)])

print(i)

f.close()