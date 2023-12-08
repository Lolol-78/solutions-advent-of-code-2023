f = open("day1_input.txt")

lines = f.readlines()

f.close()

s=0

numbers = ("one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine')

for line in lines:
    left_nbr = -1
    right_nbr = -1
    for i in range(len(line)):
        if left_nbr==-1:
            if line[i].isdigit():
                left_nbr = line[i]
            else:
                for number in numbers:
                    if line[i:i+len(number)] == number:
                        left_nbr = str(numbers.index(number) + 1)
        if right_nbr==-1:
            if line[-i-1].isdigit():
                right_nbr = line[-1-i]
            else:
                for number in numbers:
                    if len(line)-1-i-len(number) >= 0 and line[-i-1-len(number):-i-1] == number:
                        right_nbr = str(numbers.index(number) + 1)
    s += int(str(left_nbr)+str(right_nbr))

print(s)



