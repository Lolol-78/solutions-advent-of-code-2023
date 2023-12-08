f = open("input.txt")

lines = f.readlines()

s = 0

for line in lines:
    left_nbr = -1
    right_nbr = -1
    for i in range(len(line)):
        if line[i].isdigit() and left_nbr==-1:
            left_nbr = line[i]
        if line[-i-1].isdigit() and right_nbr==-1:
            right_nbr = line[-i-1]
    s += int(str(left_nbr)+str(right_nbr))

f.close()

print(s)