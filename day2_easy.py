f = open('day2_input.txt')

games = f.readlines()

f.close()

maximum = {'red': 12, 'green': 13, 'blue': 14}

s = 0

for i in range(100):
    game = games[i].replace('\n', '')
    game_index = i + 1
    sets = game[game.index(':')+2:].split('; ')
    game_is_possible = True
    for j in sets:
        curr_set = j.split(', ')
        for k in curr_set:
            if 'red' in k and int(k[:k.index(' ')]) > maximum['red']:
                game_is_possible = False
            elif 'green' in k and int(k[:k.index(' ')]) > maximum['green']:
                game_is_possible = False
            elif 'blue' in k and int(k[:k.index(' ')]) > maximum['blue']:
                game_is_possible = False
    if game_is_possible:
        s += game_index

print(s)