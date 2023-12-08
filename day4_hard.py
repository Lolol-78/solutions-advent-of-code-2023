f = open("day4_input.txt")

cards = f.readlines()

f.close()

total = 0

cards_number = [1 for _ in range(205)]

for i in range(len(cards)):
    card = cards[i]
    winning = list(map(int, card[card.index(':')+2: card.index('|')-1].split()))
    discovered = list(map(int, card[card.index('|')+2:-1].split()))
    number_matching = 0
    for c in winning:
        if c in discovered:
            number_matching += 1
    for j in range(number_matching):
        cards_number[i+j+1] += cards_number[i]

print(sum(cards_number))