f = open("day3_input.txt")

lines = f.readlines()

f.close()

all_numbers = []

def analyse_around_character(x: int, y: int) -> list:
    numbers = []
    # check a droite du caractere
    if lines[y][x+1].isdigit():
        nb = lines[y][x+1]
        a = 2
        while x+a < len(lines[0]) and lines[y][x+a].isdigit():
            nb += lines[y][x+a]
            a += 1
        numbers.append(int(nb))
    # check a gauche du caractere
    if lines[y][x-1].isdigit():
        nb = lines[y][x-1]
        a = 2
        while x-a >= 0 and lines[y][x-a].isdigit():
            nb = lines[y][x-a] + nb
            a += 1
        numbers.append(int(nb))
    # check le caractere au dessus
    if lines[y-1][x].isdigit():
        nb = lines[y-1][x]
        a = 1
        while x+a < len(lines[0]) and lines[y-1][x+a].isdigit():
            nb += lines[y-1][x+a]
            a += 1
        a = 1
        while x-a >= 0 and lines[y-1][x-a].isdigit():
            nb = lines[y-1][x-a] + nb
            a += 1
        numbers.append(int(nb))
    else:
        # check le caractere au dessus a gauche
        if lines[y-1][x-1].isdigit():
            nb = lines[y-1][x-1]
            a = 2
            while x-a >= 0 and lines[y-1][x-a].isdigit():
                nb = lines[y-1][x-a] + nb
                a += 1
            numbers.append(int(nb))
        # check le caractere au dessus a droite
        if lines[y-1][x+1].isdigit():
            nb = lines[y-1][x+1]
            a = 2
            while x+a < len(lines[0]) and lines[y-1][x+a].isdigit():
                nb += lines[y-1][x+a]
                a += 1
            numbers.append(int(nb))
    # check le caractere en dessous
    if lines[y+1][x].isdigit():
        nb = lines[y+1][x]
        a = 1
        while x+a < len(lines[0]) and lines[y+1][x+a].isdigit():
            nb += lines[y+1][x+a]
            a += 1
        a = 1
        while x-a >= 0 and lines[y+1][x-a].isdigit():
            nb = lines[y+1][x-a] + nb
            a += 1
        numbers.append(int(nb))
    else:
        # check le caractere en dessous a gauche
        if lines[y+1][x-1].isdigit():
            nb = lines[y+1][x-1]
            a = 2
            while x-a >= 0 and lines[y+1][x-a].isdigit():
                nb = lines[y+1][x-a] + nb
                a += 1
            numbers.append(int(nb))
        # check le caractere en dessous a droite
        if lines[y+1][x+1].isdigit():
            nb = lines[y+1][x+1]
            a = 2
            while x+a < len(lines[0]) and lines[y+1][x+a].isdigit():
                nb += lines[y+1][x+a]
                a += 1
            numbers.append(int(nb))
    return numbers

for line in range(len(lines)):
    for character in range(len(lines[line])):
        if lines[line][character] in "#$%&*+-/=@":
            all_numbers.extend(analyse_around_character(character, line))

print(sum(all_numbers))