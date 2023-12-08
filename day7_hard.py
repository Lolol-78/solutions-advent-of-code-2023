f = open('day7_input.txt')

five = []
four = []
full_house = []
three = []
two_pair = []
one_pair = []
high_card = []

possibilities = 'AKQT98765432J'


def check_four(different, numbers):
    if 4 in numbers:
        return True
    elif 'm' in different:
        numbers_d = numbers[different.index('m')]
        if numbers_d == 1:
            if 3 in numbers:
                return True
        elif numbers_d == 2:
            if numbers.count(2) == 2:
                return True
        elif numbers_d == 3:
            return True
    return False

def check_full_house(different, numbers):
    if 3 in numbers and 2 in numbers:
        return True
    elif 'm' in different:
        number_d = numbers[different.index('m')]
        if number_d == 1:
            if 3 in numbers or (numbers.count(2) == 2):
                return True
        elif number_d == 2:
            if numbers.count(2) == 2:
                return True
        elif number_d == 3:
            return True
    return False

def check_three(diff, numb):
    if 3 in numb:
        return True
    elif 'm' in diff:
        numbers_d = numb[diff.count('m')]
        if numbers_d == 1:
            if 2 in numb:
                return True
        elif numbers_d == 2:
            return True
    return False

def check_two_pair(diff, numb):
    if numb.count(2) == 2:
        return True
    elif 'm' in diff:
        numbers_d = numb[different.index('m')]
        if numbers_d == 1:
            if 2 in numb:
                return True
        elif numbers_d == 2:
            return True
    return False

def check_one_pair(diff, numb):
    if 2 in numbers:
        return True
    elif 'm' in diff:
        return True
    return False


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
    
    if 5 in numbers or ('m' in different and len(numbers)==2):
        five.append([cards, int(bid)])
    elif check_four(different, numbers):
        four.append([cards, int(bid)])
    elif check_full_house(different, numbers):
        full_house.append([cards, int(bid)])
    elif check_three(different, numbers):
        three.append([cards, int(bid)])
    elif check_two_pair(different, numbers):
        two_pair.append([cards, int(bid)])
    elif check_one_pair(different, numbers):
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

#print(five, four, full_house, three, two_pair, one_pair, high_card, sep='\n')


s = 0

for i in range(1000):
    s += (1000 - i) * all_sets[i][1]

print(s)


f.close()