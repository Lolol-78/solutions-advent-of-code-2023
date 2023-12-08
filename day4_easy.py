f = open("day4_input.txt")

cards = f.readlines()

f.close()

total = 0

for i in range(len(cards)):
    card = cards[i]
    winning = list(map(int, card[card.index(':')+2: card.index('|')-1].split()))
    discovered = list(map(int, card[card.index('|')+2:-1].split()))
    score = 0
    for c in winning:
        if c in discovered:
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score

print(total)