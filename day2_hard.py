f = open('day2_input.txt')

games = f.readlines()

f.close()

s = 0

for i in range(100):
    game = games[i].replace('\n', '')
    game_index = i + 1
    sets = game[game.index(':')+2:].split('; ')
    game_is_possible = True
    blues, greens, reds = [], [], []
    for j in sets:
        curr_set = j.split(', ')
        for k in curr_set:
            if 'red' in k:
                reds.append(int(k[:k.index(' ')]))
            elif 'green' in k:
                greens.append(int(k[:k.index(' ')]))
            elif 'blue' in k:
                blues.append(int(k[:k.index(' ')]))
    power = max(greens)*max(reds)*max(blues)
    s += power

print(s)