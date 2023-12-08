f = open('day7_input.txt')

five = []
four = []
full_house = []
three = []
two_pair = []
one_pair = []
high_card = []

possibilities = 'AKQJT98765432'

for i in range(1000):
    current_set = f.readline()
    cards, bid = current_set.split()
    
    for j in range(13):
        cards = cards.replace(possibilities[j], chr(ord('a')+j))
    
    different = []
    numbers = []
    
    for j in cards:
        if not j in different:
            different.append(j)
            numbers.append(cards.count(j))
    
    if 5 in numbers:
        five.append([cards, int(bid)])
    elif 4 in numbers:
        four.append([cards, int(bid)])
    elif 3 in numbers and 2 in numbers:
        full_house.append([cards, int(bid)])
    elif 3 in numbers:
        three.append([cards, int(bid)])
    elif numbers.count(2) == 2:
        two_pair.append([cards, int(bid)])
    elif 2 in numbers:
        one_pair.append([cards, int(bid)])
    elif len(numbers) == 5:
        high_card.append([cards, int(bid)])
    
five.sort(key=lambda x: x[0])
four.sort(key=lambda x: x[0])
full_house.sort(key=lambda x: x[0])
three.sort(key=lambda x: x[0])
two_pair.sort(key=lambda x: x[0])
one_pair.sort(key=lambda x: x[0])
high_card.sort(key=lambda x: x[0])

all_sets = []
all_sets.extend(five)
all_sets.extend(four)
all_sets.extend(full_house)
all_sets.extend(three)
all_sets.extend(two_pair)
all_sets.extend(one_pair)
all_sets.extend(high_card)

s = 0

for i in range(1000):
    s += (1000 - i) * all_sets[i][1]

print(s)


f.close()